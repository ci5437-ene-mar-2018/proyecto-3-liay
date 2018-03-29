def appendable(rule1, rule2):
	for var1 in rule1:
		for var2 in rule2:
			if abs(var1) >= abs(var2):
				return False

	return True


def joinRules(ruleList1, ruleList2):
	joinedRules = []

	for rules1 in ruleList1:
		for rules2 in ruleList2:
			flatRule1 = list({x for rule in rules1 for x in rule})
			flatRule2 = list({x for rule in rules2 for x in rule})


			if appendable(flatRule1, flatRule2):
				joinedRules.append(rules1+rules2)

	joinedRules = set(tuple(x) for rules in joinedRules for x in rules)

	joinedRules = list(list(tupleRule) for tupleRule in joinedRules)

	list((x for x in joinedRules))

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
		totalRulesDNF += createRule(rowHints[i], board[i])

	boardColumns = [list(i) for i in zip(*board)]

	for i in range(len(boardColumns)):
		totalRulesDNF += createRule(colHints[i], boardColumns[i])


	return totalRulesDNF


def dnfToCNF(dnfRules, lastVar):
	length = dnfRules

	auxVar = lastVar+1
	cnfRules = []
	for rule in dnfRules:
		tmp = [auxVar]
		for var in rule:
			tmp.append(-var)
			cnfRules.append([-auxVar, var])

		cnfRules.append(tmp)
		auxVar += 1

	tmp = []
	for i in range(lastVar+1, auxVar):
		tmp.append(i)

	cnfRules.append(tmp)

	return cnfRules, auxVar-1

def printToFile(cnfRules, numVariables, file):

	f = open(file, "w")

	clauses = len(cnfRules)
	f.write("p cnf "+str(numVariables)+" "+str(clauses)+"\n")

	for rule in cnfRules:
		f.write(" ".join([str(i) for i in rule])+" 0\n")

	f.close()



def main():
	#testDNF = rulesFromBoard([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], [[4],[1,1],[1,1],[1,1]], [[3],[2],[3],[1,1]])

	#cnfRules, numVariables = dnfToCNF(testDNF, 16)

	print(joinRules([[[-1,2],[-1,-3]], [[-2,3],[-2,-4]], [[-3,4],[-3,-5]], [[-4,5],[-4,-6]], [[-5,6],[-5,-7]], [[-6,7]]], [[[-1,2], [-1,3], [-1,-4]], [[-2,3], [-2,4], [-2,-5]], [[-3,4], [-3,5], [-3,-6]], [[-4,5], [-4,6], [-4,-7]], [[-5,6],[-5,7]]]))

	#printToFile(cnfRules, numVariables, "test.sat")



if __name__ == '__main__':
	main()