# boolean expression evaluator v2

from antlr4 import InputStream, CommonTokenStream
from grammar.boolean_expression_v2.BooleanExpressionV2Lexer import (
    BooleanExpressionV2Lexer,
)
from grammar.boolean_expression_v2.BooleanExpressionV2Parser import (
    BooleanExpressionV2Parser,
)

input_text = input("> ")
lexer = BooleanExpressionV2Lexer(InputStream(input_text))
stream = CommonTokenStream(lexer)
parser = BooleanExpressionV2Parser(stream)

tree = parser.expr()

print(tree.toStringTree(recog=parser))
