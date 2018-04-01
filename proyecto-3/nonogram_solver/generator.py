import sys, os

def appendable(rule1, rule2):
	for var1 in rule1:
		for var2 in rule2:
			if abs(var1) >= abs(var2):
				return False

	return True


def filterRules(ruleDic1, ruleDic2):
	orderRules = {}
	appendableRules = {}

	keys = []
	for key1 in ruleDic1:
		for key2 in ruleDic2:

			if not appendable(ruleDic1[key1], ruleDic2[key2]):
				try:
					orderRules[key1].append(-key2)
				except:
					orderRules[key1] = [-key2]

			else:
				appendableRules[key1] = True
				appendableRules[key2] = True


	# delete impossible rules
	for key in list(ruleDic1):
		if not appendableRules.get(key, False):
			del ruleDic1[key]
			orderRules.pop(key, None)

			for key2 in orderRules:
				if -key in orderRules[key2]:
					orderRules[key2].remove(-key)

	for key in list(ruleDic2):
		if not appendableRules.get(key, False):
			del ruleDic2[key]
			orderRules.pop(key, None)

			for key2 in orderRules:
				if -key in orderRules[key2]:
					orderRules[key2].remove(-key)			

	# add order rules
	for key in orderRules:
		try:
			ruleDic1[key] += orderRules[key]
		except:
			ruleDic2[key] += orderRules[key]

	return [list(ruleDic1.keys()), list(ruleDic2.keys())]


def createRule(hints, variableList, lastVar):

	length = len(variableList)
	rulesList = []

	auxVar = lastVar + 1

	for hint in hints:
		hintRules = {}
		if hint > 0:
			for num in range(length-hint+1):
				tmpRule = []
				for x in range(num, num+hint):
					tmpRule.append(variableList[x])

				if (num < length-hint):
					tmpRule.append(-variableList[(num+hint)])

				hintRules[auxVar] = tmpRule
				auxVar += 1

			rulesList.append(hintRules)
		else:
			hintRules[auxVar] = [-x for x in variableList]
			auxVar += 1

	keys = []
	for i in range(1, len(rulesList)):
		keys += filterRules(rulesList[i-1], rulesList[i])

	if len(keys) != 0:
		# remove duplicates
		cleanKeys = []
		for key in keys:
			if not key in cleanKeys:
				cleanKeys.append(key)

		rulesList.append({-i: cleanKeys[i-1] for i in range(1, len(cleanKeys)+1)})
	else:
		try:
			rulesList.append({-1: list(rulesList[0].keys())})
		except:
			None

	# Add necessary conditions
	necessaryConditions = addNecessaryConditions(rulesList)
	if len(necessaryConditions) > 0:
		rulesList.append(addNecessaryConditions(rulesList))

	return rulesList, auxVar-1


def rulesFromBoard(board, rowHints, colHints, lastVar):
	totalRules = []
	realLastVar = lastVar
	for i in range(len(board)):
		tmpRules, realLastVar = createRule(rowHints[i], board[i], realLastVar)
		totalRules += tmpRules


	boardColumns = [list(i) for i in zip(*board)]

	for i in range(len(boardColumns)):
		tmpRules, realLastVar = createRule(colHints[i], boardColumns[i], realLastVar)
		totalRules += tmpRules

	return totalRules, realLastVar


def addNecessaryConditions(rulesList):
	necessaryConditions = {}

	for block in rulesList:
		for rule in block:
			if rule >= 0:
				# Necessary Conditions
				for var in block[rule]:
					if var > 0:
						try:
							necessaryConditions[var].append(rule)
						except:
							necessaryConditions[var] = [rule]


	return necessaryConditions


def addUnicityRules(rulesList, realLastVar):
	counter = 0

	for block in rulesList:
		for rule in block:
			if rule >= 0 and rule > realLastVar:
				# Unicity Rules
				for rule2 in block:
					if rule != rule2 and rule2 > realLastVar:
						block[rule].append(-rule2)

				counter += len(block[rule])

			else:
				counter += 1

	return counter


def printToFile(ruleList, numVariables, numClauses, realLastVar, file):

	f = open(file, "w")

	f.write("p cnf "+str(numVariables)+" "+str(numClauses)+"\n")

	for block in ruleList:
		for rule in block:
			if rule >= 0 and rule > realLastVar:
				for var in block[rule]:
					f.write(str(-rule)+" "+str(var)+" 0\n")

			elif rule > 0 and rule <= realLastVar:
				f.write(str(-rule)+" "+" ".join([str(i) for i in block[rule]])+" 0\n")
			else:
				f.write(" ".join([str(i) for i in block[rule]])+" 0\n")

	f.close()


def createBoard(rows, columns):

	board = []

	i = 1
	for x in range(rows):
		tmp = []
		for y in range(columns):
			tmp.append(i)
			i = i + 1

		board.append(tmp)

	return board


def readHints(fileD, stop = ""):
	line = fileD.readline()
	hints = []

	if stop != "":
		while not stop in line:
			hint = [int(x) for x in line.split(',')]
			hints.append(hint)
			line = fileD.readline()

	else:
		while line:
			hint = [int(x) for x in line.split(',')]
			hints.append(hint)
			line = fileD.readline()

	return hints


def readFromFile(file):
	try:
		f = open(file, "r")
	except IOError:
		print("Cant open '"+file+"'.\n")
		sys.exit(-1)


	line = f.readline()

	if "width" in line:
		columns = int(line.split(' ')[-1])

		line = f.readline()
		rows = int(line.split(' ')[-1])

	elif "height" in line:
		rows = int(line.split(' ')[-1])

		line = f.readline()
		columns = int(line.split(' ')[-1])


	line = f.readline()

	if "columns" in line:
		colHints = readHints(f, "rows")
		rowHints = readHints(f)

	else:
		rowHints = readHints(f, "columns")
		colHints = readHints(f)


	board = createBoard(rows, columns)

	f.close()

	return board, rowHints, colHints


def encoder(file, saveFile):

	board, rowHints, colHints = readFromFile(file)
	print("READ NON FILE")

	lastBoardVar = len(board) * len(board[0])

	test, variableNumber = rulesFromBoard(board, rowHints, colHints, lastBoardVar)
	print("GOT RULES")

	clauseNumber = addUnicityRules(test, lastBoardVar)
	print("ADDED UNICITY RULES")

	printToFile(test, variableNumber, clauseNumber, lastBoardVar, saveFile)
	print("SAT FILE PRINTED. BYE!")

	return board


def satFilename(file):

	saveFile = file.split("/")[-1]

	saveFile = saveFile.split(".")[0] + ".sat"

	saveFile = os.getcwd() + "/satFiles/" + saveFile

	return saveFile


def main():

	file = sys.argv[1]

	encoder(file, satFilename(file))

	# print(variableNumber)
	# print()
	# print(clauseNumber)
	# print()
	# print(test)


if __name__ == '__main__':
	main()
