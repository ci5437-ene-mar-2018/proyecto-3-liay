def appendable(rule1, rule2):
	for var1 in rule1:
		for var2 in rule2:
			if abs(var1) >= abs(var2):
				return False

	return True


def joinRules(ruleList1, ruleList2):
	joinedRules = []

	for rule1 in ruleList1:
		for rule2 in ruleList2:
			if appendable(rule1, rule2):
				joinedRules.append(rule1+rule2)

	return joinedRules


def fillSlots(rule, variableList):
	totalVariables = [-x for x in variableList]

	for var1 in rule:
		for var2 in totalVariables:
			if abs(var1) == abs(var2):
				totalVariables.remove(var2)
				break

	finalRule = rule + totalVariables

	return finalRule


def createRule(hints, variableList):

	length = len(variableList)
	rulesList = []

	for hint in hints:
		hintRules = []
		for num in range(length-hint+1):
			tmpRule = []
			for x in range(num, num+hint):
				tmpRule.append(variableList[x])

			if (num < length-hint):
				tmpRule.append(-variableList[(num+hint)])

			hintRules.append(tmpRule)

		rulesList.append(hintRules)

	try:
		joinedRules = rulesList[0]
	except:
		joinedRules = []

	for i in range(1, len(rulesList)):
		joinedRules = joinRules(joinedRules, rulesList[i])

	for i in range(len(joinedRules)):
		joinedRules[i] = fillSlots(joinedRules[i], variableList)

	return joinedRules


def rulesFromBoard(board, colHints, rowHints):
	totalRulesDNF = []
	for i in range(len(board)):
		totalRulesDNF.append(createRule(rowHints[i], board[i]))

	boardColumns = [list(i) for i in zip(*board)]

	for i in range(len(boardColumns)):
		totalRulesDNF.append(createRule(colHints[i], boardColumns[i]))


	return totalRulesDNF


def dnfToCNF(dnfRules, lastVar):
	length = dnfRules

	auxVar = lastVar+1
	cnfRules = []
	for rules in dnfRules:
		ruleList = []
		step = auxVar
		for rule in rules:
			tmp = [auxVar]
			for var in rule:
				tmp.append(-var)
				ruleList.append([-auxVar, var])

			ruleList.append(tmp)
			auxVar += 1

		endRule = []
		for i in range(step, auxVar):
			endRule.append(i)

		ruleList.append(endRule)


		cnfRules.append(ruleList)

	# tmp = []
	# for i in range(lastVar+1, auxVar):
	# 	tmp.append(i)

	# cnfRules.append(tmp)

	cnfRules = [x for rule in cnfRules for x in rule]

	return cnfRules, auxVar-1


def printToFile(cnfRules, numVariables, file):

	f = open(file, "w")

	clauses = len(cnfRules)
	f.write("p cnf "+str(numVariables)+" "+str(clauses)+"\n")

	for rule in cnfRules:
		f.write(" ".join([str(i) for i in rule])+" 0\n")

	f.close()



def main():
	testDNF = rulesFromBoard([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], [[4],[1,1],[1,1],[1,1]], [[3],[1,1],[3],[1,1]])

	cnfRules, numVariables = dnfToCNF(testDNF, 16)

	print(cnfRules)
	print("\n\n")
	print(testDNF)

	printToFile(cnfRules, numVariables, "test.sat")



if __name__ == '__main__':
	main()