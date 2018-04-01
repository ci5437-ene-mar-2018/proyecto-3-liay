import generator, translator, getopt, sys, os

def resultFilename(file):
	saveFile = file.split("/")[-1]

	saveFile = "result" + saveFile.split(".")[0] + ".txt"

	saveFile = os.getcwd() + "/results/" + saveFile

	return saveFile


def statFilename(file):
	saveFile = file.split("/")[-1]

	saveFile = "statistics" + saveFile.split(".")[0] + ".txt"

	saveFile = os.getcwd() + "/statistics/" + saveFile

	return saveFile


def main():
	# Handle options and arguments
	try:
		opts, args = getopt.gnu_getopt(sys.argv[1:], "mi", ["minisat", "image"])
	
	except:
		print("Usage: .non-file [-i, --image |-m, --minisat]")
		sys.exit(2)

	try:
		nonFile = args[0]

	except:
		print("Usage: .non-file [-i, --image |-m, --minisat]")
		sys.exit(2)

	image = False
	minisat = False

	for o, a in opts:
		if o in ("-i", "--image"):
			image = True


		elif o in ("-m", "--minisat"):
			minisat = True

		else:
			print("Usage: .non-file [-i, --image |-m, --minisat]")
			sys.exit(3)


	# Obtain filenames and run Generator to save .sat file

	satFile = generator.satFilename(nonFile)

	resultFile = resultFilename(nonFile)

	statFile = statFilename(nonFile)

	imageFile = translator.imageFilename(nonFile)

	board = generator.encoder(nonFile, satFile)

	rows = len(board)

	columns = len(board[0])

	lastVar = rows*columns

	# If minisat option enabled, runs minisat with parameters satFile, resultFile >> statFile
	if minisat:
		# LLAMADA A MINISAT CON PARAMETROS: SATFILE, RESULTFILE >> STATFILE
		None

	# If image option enabled, runs result decoder to obtain solution, and saves solution image
	if image:
		solution = translator.decoder(resultFile, lastVar)
		translator.createImage(solution, rows, columns, imageFile)



if __name__ == '__main__':
	main()