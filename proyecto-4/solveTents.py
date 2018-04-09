#!/usr/bin/env python3

# solveTents.py
# Universidad Simon Bolivar
# CI5437: Inteligencia Artificial I

# Autores: 
#   - Yarima Luciani 13-10770
#   - Lautaro Villalon 12-10427

# Equipo: LIAY
# Prof. Blai Bonet
# Ene-Mar 2018

import getopt, sys, os, subprocess

def resultFilename(file):
	saveFile = file.split("/")[-1]

	if saveFile.split(".")[-1] != "dzn":
		print("Usage: game_file [-h, --help]\n\nPlease use a .dzn file as the game_file.")
		sys.exit(2)

	saveFile = saveFile.split(".")[0] + ".result"

	saveFile = os.getcwd() + "/results/" + saveFile

	return saveFile

def printHelp():
	print("solveTents.py\n\nUsage: game_file [-h, --help]\n\n\
Options:\n\t-h, --help: Shows help.\n\n\
Argument: .dzn file with the Tents board specification.\n\n\
Requirements:\n\tMiniZinc installed as global environment variables. Download at: http://www.minizinc.org/\n\t\
Python 3.x.\n\nOutput: Result file in results folder. Matrix with values: 1=Tent, 2=Tree, 0=Blank.\n")
	sys.exit(1)


def printUsage():
	print("Usage: game_file [-h, --help]")
	sys.exit(2)

def outputString(output):

	legend = "LEGEND: 1=Tent, 2=Tree, 0=Blank.\n\n"

	return legend+output


def main():
	# Handle options and arguments
	try:
		opts, args = getopt.gnu_getopt(sys.argv[1:], "h", ["help"])
	
	except:
		printUsage()

	try:
		gameFile = args[0]

	except:
		printUsage()


	for o, a in opts:

		if o in ("-h", "--help"):
			printHelp()

		else:
			printUsage()


	# Obtain output filename and run Minizinc to save .result file

	resultFile = resultFilename(gameFile)

	# Run MiniZinc with parameters gameFile >> resultFile

	args = ("minizinc", "tentSolver.mzn", gameFile)
	
	popen = subprocess.Popen(args, stdout=subprocess.PIPE)
	popen.wait()
	output = popen.stdout.read()

	# Write result file
	res = open(resultFile, "w")
	res.write(outputString(output.decode()))
	res.close()

	# Show result in stdout
	print(outputString(output.decode()))


if __name__ == '__main__':
	main()