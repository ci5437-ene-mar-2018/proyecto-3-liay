import sys, os

def decoder(file, lastVar):
	try:
		f = open(file, "r")
	except IOError:
		print("Cant open '"+file+"'.: Perhaps you should run with -m flag to get the result first.\n")
		sys.exit(-1)

	line = f.readline()

	if line == "SAT\n":
		line = f.readline().split()

		f.close()

		result = []
		i = 0
		while abs(int(line[i])) <= lastVar:
			result.append(int(line[i]))
			i += 1


		return result

	else:

		f.close()

		raise ValueError('Unsatisfiable Solution. Cannot decode.')


def createImage(solution, rows, columns, file):
	assert(len(solution) == rows*columns)

	f = open(file, "w")

	f.write("P1\n"+str(columns)+" "+str(rows)+"\n")

	i = 0
	for x in range(rows):
		for y in range(columns):
			if solution[i] > 0:
				f.write("1 ")
			else:
				f.write("0 ")
			i += 1
		f.write("\n")

	f.close()

	print("IMAGE SAVED!")


def imageFilename(file):

	saveFile = file.split("/")[-1]

	saveFile = saveFile.split(".")[0] + ".pbm"

	saveFile = os.getcwd() + "/images/" + saveFile

	return saveFile