# example: calculator - main
# reference: https://medium.com/@kv391/antlr4-grammar-a-quick-tutorial-e1f0fb6ca4ff

import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, parent_dir)

from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from grammar.calculator.CalculatorLexer import CalculatorLexer
from grammar.calculator.CalculatorParser import CalculatorParser
from evaluator.calculator import CalcEvaluator


def main():
    expression = input("Enter an expression: ")
    input_stream = InputStream(expression)
    lexer = CalculatorLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CalculatorParser(token_stream)
    tree = parser.expr()

    calc_evaluator = CalcEvaluator()
    walker = ParseTreeWalker()
    walker.walk(calc_evaluator, tree)

    print("Result:", calc_evaluator.getValue())


if __name__ == "__main__":
    main()
