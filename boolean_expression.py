# boolean expression evaluator v1

from antlr4 import InputStream, CommonTokenStream
from grammar.boolean_expression.BooleanExpressionLexer import BooleanExpressionLexer
from grammar.boolean_expression.BooleanExpressionParser import BooleanExpressionParser

input_text = input("> ")
lexer = BooleanExpressionLexer(InputStream(input_text))
stream = CommonTokenStream(lexer)
parser = BooleanExpressionParser(stream)

tree = parser.program()

print(tree.toStringTree(recog=parser))
