import sys
from antlr4 import *
from grammar.boolean_expression.BooleanExpressionLexer import (
    BooleanExpressionLexer,
)
from grammar.boolean_expression.BooleanExpressionParser import (
    BooleanExpressionParser,
)
from grammar.error_handlers.custom_error_listener import CustomErrorListener
from utils.eval_visitor_utils import EvalVisitor

def print_rules():
    print(""" 
          1. Comparison Operator
                ==  : Checks if two values are equal.
                !=  : Checks if two values are not equal.
                <   : Checks if the left value is less than the right.
                >   : Checks if the left value is greater than the right.
          2. Logical Operators:
                AND : True if both operands are True.
                OR  : True if at least one operand is True.
                NOT : Inverts the truth value.
          
          Priority Order (From Top to Bottom)
            1. Parentheses - ():
            2. Comparison Operators - ==, !=, <, >
            3. Logical NOT - NOT
            4. Logical AND - AND
            5. Logical OR - OR
          
          Example:
            (5 > 3 AND 2 != 2) OR (4 == 4 AND NOT (1 > 2))
            1. Evaluate 5 > 3       → True.
            2. Evaluate 2 != 2      → False.
            3. True and False       → False.
            4. Evaluate 4 == 4      → True.
            5. Evaluate 1 > 2       → False, 
            6. Evaluate NOT (False) → True.
            6. True and True        → True.
            7. False or True        → True.
            RESULT = TRUE.
          
            (True or False) and False
            1. Evaluate True or False   → True.
            2. Evaluate True and False  → False.
            RESULT = FALSE
          
            False and True or True
            1. Evaluate False and True  → False.
            2. Evaluate False or True   → True.
            RESULT = TRUE
    """)

def get_user_action():
    return input("\nAction (assign/eval/exit): ").strip().lower()


def assign_variable(visitor):
    try:
        var = input("Variable (e.g., x or y): ").strip()
        if not var.isidentifier():
            CustomErrorListener.handle_custom_error("Invalid variable name. Use valid identifiers (e.g., a, b1).")

        value = input("Value (True/False/Number): ").strip()
        
        # Determine the type of the variable
        if value.lower() == "true":
            visitor.declare_variable(var, True)
        elif value.lower() == "false":
            visitor.declare_variable(var, False)
        elif value.isdigit():
            visitor.declare_variable(var, int(value))
        else:
            CustomErrorListener.handle_custom_error("Value must be 'true', 'false', or a number.")
            return
        print(f"Assigned: {var} = {visitor.variables[var]}")
    except ValueError as e:
        CustomErrorListener.handle_custom_error(e)

def evaluate_expression(visitor):
    expression = input("Enter a Boolean or comparison expression: ")
    try:
        input_stream = InputStream(expression)
        lexer = BooleanExpressionLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(CustomErrorListener())
        stream = CommonTokenStream(lexer)
        parser = BooleanExpressionParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(CustomErrorListener())
        tree = parser.expr()
        result = visitor.visit(tree)
        print(tree.toStringTree(recog=parser))
        print("Result:", result)
    except Exception as e:
        CustomErrorListener.handle_custom_error(f"Error: {e}")


def main():
    print("Boolean Expression Evaluator")
    print_rules()
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
            CustomErrorListener.handle_custom_error("Invalid action. Please choose from 'assign', 'eval', or 'exit'.")


if __name__ == "__main__":
    main()