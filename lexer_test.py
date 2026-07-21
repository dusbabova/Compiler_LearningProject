from lexer import Lexer
from TokenType import TokenType


def main():
	#ops tokenisation test
	"""source = "+- */ >>= = !="
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
