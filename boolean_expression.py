# boolean expression evaluator v1

from antlr4 import InputStream, CommonTokenStream
from grammar.boolean_expression.BooleanExpressionLexer import BooleanExpressionLexer
from grammar.boolean_expression.BooleanExpressionParser import BooleanExpressionParser
from grammar.error_handlers.custom_error_listener import CustomErrorListener

input_text = input("> ")
lexer = BooleanExpressionLexer(InputStream(input_text))
lexer.removeErrorListeners()
lexer.addErrorListener(CustomErrorListener())
stream = CommonTokenStream(lexer)
parser = BooleanExpressionParser(stream)
parser.removeErrorListeners()
parser.addErrorListener(CustomErrorListener())

tree = parser.program()

print(tree.toStringTree(recog=parser))
