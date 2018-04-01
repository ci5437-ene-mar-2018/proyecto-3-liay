import sys, os

def decoder(file, lastVar):

	f = open(file, "r")

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


def createSolution(solution, rows, columns, file):
	assert(len(solution) == rows*columns)

	f = open(file, "w")

	f.write("P1\n"+str(rows)+" "+str(columns)+"\n")

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


def imageFilename(file):

	saveFile = file.split("/")[-1]

	saveFile = saveFile.split(".")[0] + ".pbm"

	saveFile = os.getcwd() + "/images/" + saveFile

	return saveFile

def main():

	file = sys.argv[1]

	solution = decoder(file, 25)

	saveFile = imageFilename(file)

	createSolution(solution, 5, 5, saveFile)
	print("DONE!")



if __name__ == '__main__':
	main()


