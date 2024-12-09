import sys
from antlr4 import *
from grammar.boolean_expression_v2.BooleanExpressionV2Lexer import (
    BooleanExpressionV2Lexer,
)
from grammar.boolean_expression_v2.BooleanExpressionV2Parser import (
    BooleanExpressionV2Parser,
)
from utils.eval_visitor_utils import EvalVisitor

def get_user_action():
    return input("\nAction (assign/eval/exit): ").strip().lower()


def assign_variable(visitor):
    try:
        var = input("Variable (e.g., x or y): ").strip()
        if not var.isidentifier():
            raise ValueError("Invalid variable name. Use valid identifiers (e.g., a, b1).")

        value = input("Value (True/False/Number): ").strip()
        
        # Determine the type of the variable
        if value.lower() == "true":
            visitor.declare_variable(var, True)
        elif value.lower() == "false":
            visitor.declare_variable(var, False)
        elif value.isdigit():
            visitor.declare_variable(var, int(value))
        else:
            raise ValueError("Value must be 'true', 'false', or a number.")
        print(f"Assigned: {var} = {visitor.variables[var]}")
    except ValueError as e:
        print(e)

def evaluate_expression(visitor):
    expression = input("Enter a Boolean or comparison expression: ")
    try:
        input_stream = InputStream(expression)
        lexer = BooleanExpressionV2Lexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = BooleanExpressionV2Parser(stream)
        tree = parser.expr()

        result = visitor.visit(tree)
        print("Result:", result)
    except Exception as e:
        print(f"Error: {e}")


def main():
    print("Boolean Expression Evaluator")
    visitor = EvalVisitor()

    while True:
        action = get_user_action()

        if action == "assign":
            assign_variable(visitor)
        elif action == "eval":
            evaluate_expression(visitor)
        elif action == "exit":
            print("Exiting the program.")
            break
        else:
            print("Invalid action. Please choose from 'assign', 'eval', or 'exit'.")


if __name__ == "__main__":
    main()