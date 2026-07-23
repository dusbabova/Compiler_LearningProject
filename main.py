from lexer import *
from parser import *
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

	parser.program() # Start the parser.
	print("Parsing completed.")

	#ops tokenisation test
	"""source = "+- */ >>= = !="
	lexer = Lexer(source)

	token = lexer.getToken()
	while token.kind != TokenType.EOF:
		print(token.kind)
		token = lexer.getToken()"""
	
	#string + comment check
	"""source = "+- \"This is a string\" # This is a comment!\n */" 
	lexer = Lexer(source)

	token = lexer.getToken()
	while token.kind != TokenType.EOF:
		print(token.kind)
		token = lexer.getToken()"""
	#numbers test
	"""source = "+-123 9.8654*/"  
	lexer = Lexer(source)

	token = lexer.getToken()
	while token.kind != TokenType.EOF:
		print(token.kind)
		token = lexer.getToken()"""
	
	#keywords test
	"""source = "IF+-123 foo*THEN/" 
	lexer = Lexer(source)

	token = lexer.getToken()
	while token.kind != TokenType.EOF:
		print(token.kind)
		token = lexer.getToken()"""
	
    #lexer.peek + lexer.nextChar test
	"""source = "LET foobar = 123" 
	lexer = Lexer(source)

	while lexer.peek() != '\0':
		print(lexer.curChar)
		lexer.nextChar()"""

main()
