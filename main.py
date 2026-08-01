from lexer import *
from parser import *
from emitter import *
from TokenType import TokenType
import sys

def main():
	print("Teeny Tiny Compiler")
	if len(sys.argv) != 2:
		sys.exit("Error: Compiler needs source file as argument.")
	with open(sys.argv[1], 'r') as inputFile:
		source = inputFile.read()

    # Initialize the lexer and parser.
	lexer = Lexer(source)
	parser = Parser(lexer)
	emitter = Emitter("out.c")

	parser.program() # Start the parser.
	print("Parsing completed.")
	emitter.writeFile() # Write the output to file.
	print("Compiling completed.")

main()
