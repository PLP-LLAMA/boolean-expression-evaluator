import unittest
from grammar.boolean_expression.BooleanExpressionVisitor import BooleanExpressionVisitor
from utils.eval_visitor_utils import EvalVisitor  # Assuming this is your EvalVisitor class

class TestEvalVisitor(unittest.TestCase):
    def setUp(self):
        self.visitor = EvalVisitor()

    def test_and_operator(self):
        self.visitor.declare_variable("x", True)
        self.visitor.declare_variable("y", False)
        tree = self.parse_expression("x AND y")
        result = self.visitor.visit(tree)
        self.assertFalse(result)

        self.visitor.declare_variable("y", True)
        tree = self.parse_expression("x AND y")
        result = self.visitor.visit(tree)
        self.assertTrue(result)

    def test_or_operator(self):
        self.visitor.declare_variable("x", True)
        self.visitor.declare_variable("y", False)
        tree = self.parse_expression("x OR y")
        result = self.visitor.visit(tree)
        self.assertTrue(result)

        self.visitor.declare_variable("y", False)
        tree = self.parse_expression("x OR y")
        result = self.visitor.visit(tree)
        self.assertTrue(result)  

    def test_not_operator(self):
        tree = self.parse_expression("NOT true")
        result = self.visitor.visit(tree)
        self.assertFalse(result)

        tree = self.parse_expression("NOT false")
        result = self.visitor.visit(tree)
        self.assertTrue(result)

    def test_variable_declaration(self):
        self.visitor.declare_variable("x", True)
        tree = self.parse_expression("x")
        result = self.visitor.visit(tree)
        self.assertTrue(result)

        self.visitor.declare_variable("y", False)
        tree = self.parse_expression("y")
        result = self.visitor.visit(tree)
        self.assertFalse(result)

    def test_short_circuiting_and(self):
        self.visitor.declare_variable("x", False)
        tree = self.parse_expression("x AND true")
        result = self.visitor.visit(tree)
        self.assertFalse(result)  

    def test_short_circuiting_or(self):
        self.visitor.declare_variable("x", True)
        tree = self.parse_expression("x OR false")
        result = self.visitor.visit(tree)
        self.assertTrue(result)  

    def test_comparison_operators(self):
        tree = self.parse_expression("5 < 10")
        result = self.visitor.visit(tree)
        self.assertTrue(result)

        tree = self.parse_expression("10 > 5")
        result = self.visitor.visit(tree)
        self.assertTrue(result)

        tree = self.parse_expression("5 == 5")
        result = self.visitor.visit(tree)
        self.assertTrue(result)

        tree = self.parse_expression("5 != 10")
        result = self.visitor.visit(tree)
        self.assertTrue(result)

    def test_parentheses(self):
        tree = self.parse_expression("(true AND false) OR true")
        result = self.visitor.visit(tree)
        self.assertTrue(result)

        tree = self.parse_expression("true AND (false OR true)")
        result = self.visitor.visit(tree)
        self.assertTrue(result)

    def test_complex_expression(self):
        self.visitor.declare_variable("a", True)
        self.visitor.declare_variable("b", False)
        tree = self.parse_expression("a AND (b OR true)")
        result = self.visitor.visit(tree)
        self.assertTrue(result) 

    def test_unary_negation(self):
        self.visitor.declare_variable("x", False)
        tree = self.parse_expression("NOT x")
        result = self.visitor.visit(tree)
        self.assertTrue(result) 

        self.visitor.declare_variable("x", True)
        tree = self.parse_expression("NOT x")
        result = self.visitor.visit(tree)
        self.assertFalse(result) 

    def test_invalid_variable(self):
        with self.assertRaises(ValueError):
            tree = self.parse_expression("undefinedVar")
            self.visitor.visit(tree)

    def test_number_expression(self):
        tree = self.parse_expression("1 < 2")
        result = self.visitor.visit(tree)
        self.assertTrue(result)

        tree = self.parse_expression("10 == 10")
        result = self.visitor.visit(tree)
        self.assertTrue(result)

    def test_boolean_expressions(self):
        tree = self.parse_expression("true")
        result = self.visitor.visit(tree)
        self.assertTrue(result)

        tree = self.parse_expression("false")
        result = self.visitor.visit(tree)
        self.assertFalse(result)

    def parse_expression(self, expression):
        from grammar.boolean_expression.BooleanExpressionLexer import BooleanExpressionLexer
        from grammar.boolean_expression.BooleanExpressionParser import BooleanExpressionParser
        from antlr4 import CommonTokenStream, InputStream

        input_stream = InputStream(expression)
        lexer = BooleanExpressionLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = BooleanExpressionParser(token_stream)
        return parser.expr()  

if __name__ == "__main__":
    unittest.main()