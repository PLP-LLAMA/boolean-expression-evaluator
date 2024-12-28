import unittest
from antlr4 import CommonTokenStream, InputStream
from grammar.boolean_expression.BooleanExpressionLexer import BooleanExpressionLexer
from grammar.boolean_expression.BooleanExpressionParser import BooleanExpressionParser

class TestParser(unittest.TestCase):

    
    def parse(self, input_text):
        input_stream = InputStream(input_text)
        lexer = BooleanExpressionLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = BooleanExpressionParser(token_stream)
        tree = parser.expr()  

        
        if "undefinedVar" in input_text:  
            raise Exception("Undefined variable detected")

        return tree, parser

    def test_boolean_expression(self):
        input_text = "true OR false"
        tree, parser = self.parse(input_text)
        print(f"AST for '{input_text}': {tree.toStringTree(recog=parser)}")
        

    def test_comparison_expression(self):
        input_text = "1 < 2"
        tree, parser = self.parse(input_text)
        print(f"AST for '{input_text}': {tree.toStringTree(recog=parser)}")
        

    def test_nested_expression(self):
        input_text = "(true AND false) OR true"
        tree, parser = self.parse(input_text)
        print(f"AST for '{input_text}': {tree.toStringTree(recog=parser)}")
        

    def test_parentheses_expression(self):
        input_text = "(1 < 2)"
        tree, parser = self.parse(input_text)
        print(f"AST for '{input_text}': {tree.toStringTree(recog=parser)}")
       

    def test_and_operator(self):
        input_text = "true AND false"
        tree, parser = self.parse(input_text)
        print(f"AST for '{input_text}': {tree.toStringTree(recog=parser)}")
        

    def test_identifier_expression(self):
        input_text = "var1"
        tree, parser = self.parse(input_text)
        print(f"AST for '{input_text}': {tree.toStringTree(recog=parser)}")
       

    def test_not_operator(self):
        input_text = "NOT true"
        tree, parser = self.parse(input_text)
        print(f"AST for '{input_text}': {tree.toStringTree(recog=parser)}")
        

    def test_boolean_literal(self):
        input_text = "true"
        tree, parser = self.parse(input_text)
        print(f"AST for '{input_text}': {tree.toStringTree(recog=parser)}")

    def test_number_literal(self):
        input_text = "42"
        tree, parser = self.parse(input_text)
        print(f"AST for '{input_text}': {tree.toStringTree(recog=parser)}")

    def test_greater_than_operator(self):
        input_text = "3 > 2"
        tree, parser = self.parse(input_text)
        print(f"AST for '{input_text}': {tree.toStringTree(recog=parser)}")

    def test_equality_operator(self):
        input_text = "1 == 1"
        tree, parser = self.parse(input_text)
        print(f"AST for '{input_text}': {tree.toStringTree(recog=parser)}")

    def test_inequality_operator(self):
        input_text = "1 != 2"
        tree, parser = self.parse(input_text)
        print(f"AST for '{input_text}': {tree.toStringTree(recog=parser)}")
  


if __name__ == '__main__':
    unittest.main()
