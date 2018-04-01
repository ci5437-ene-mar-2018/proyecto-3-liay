import generator, translator, getopt, sys, os, subprocess

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
		opts, args = getopt.gnu_getopt(sys.argv[1:], "mih", ["minisat", "image", "help"])
	
	except:
		print("Usage: .non-file [-i, --image |-m, --minisat |-h, --help]")
		sys.exit(2)

	try:
		nonFile = args[0]

	except:
		print("Usage: .non-file [-i, --image |-m, --minisat |-h, --help]")
		sys.exit(2)

	image = False
	minisat = False

	for o, a in opts:
		if o in ("-i", "--image"):
			image = True


		elif o in ("-m", "--minisat"):
			minisat = True

		elif o in ("-h", "--help"):
			print("solveNonogram.py\n\n\
Usage: .non-file [-i, --image |-m, --minisat |-h, --help]\n\n\
Options:\n\t-i, --image: Creates image based on results from minisat solver on the .non file\
(run option -m before in order to have results).\n\t\
-m, --minisat: Runs minisat solver on the .non file.\n\n\
Argument: .non file with the nonogram specification.")
			sys.exit(1)

		else:
			print("Usage: .non-file [-i, --image |-m, --minisat |-h, --help]")
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
		# Run minisat subprocess
		args = ("minisat", satFile, resultFile)
		
		popen = subprocess.Popen(args, stdout=subprocess.PIPE)
		popen.wait()
		output = popen.stdout.read()

		# Write statistics files
		stat = open(statFile, "w")
		stat.write(output.decode())
		stat.close()

		# Show statistics in stdout
		print(output.decode())


	# If image option enabled, runs result decoder to obtain solution, and saves solution image
	if image:
		solution = translator.decoder(resultFile, lastVar)
		translator.createImage(solution, rows, columns, imageFile)



if __name__ == '__main__':
	main()