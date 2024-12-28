import unittest
from antlr4 import CommonTokenStream, InputStream
from grammar.boolean_expression.BooleanExpressionLexer import (
    BooleanExpressionLexer,
)

class TestLexer(unittest.TestCase):

    def get_tokens(self, input_text):
        input_stream = InputStream(input_text)
        lexer = BooleanExpressionLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        token_stream.fill()
        return token_stream.tokens

    def test_boolean_tokens(self):
        input_text = "true AND false"  
        tokens = self.get_tokens(input_text)
        
        
        for token in tokens:
            print(f"Token: {token.text}, Type: {token.type}")
        
        
        self.assertEqual(tokens[0].type, BooleanExpressionLexer.BOOL)  
        self.assertEqual(tokens[1].type, BooleanExpressionLexer.AND)   
        self.assertEqual(tokens[2].type, BooleanExpressionLexer.BOOL) 



    def test_identifier_token(self):
        input_text = "var1"
        tokens = self.get_tokens(input_text)
        self.assertEqual(tokens[0].type, BooleanExpressionLexer.IDENTIFIER)  

    def test_comparison_operators(self):
        input_text = "1 < 2"
        tokens = self.get_tokens(input_text)
        self.assertEqual(tokens[0].type, BooleanExpressionLexer.NUMBER)  
        self.assertEqual(tokens[0].text, "1")
        self.assertEqual(tokens[1].type, BooleanExpressionLexer.T__0)  
        self.assertEqual(tokens[2].type, BooleanExpressionLexer.NUMBER)  
        self.assertEqual(tokens[2].text, "2")

    def test_logical_operators(self):
        input_text = "true AND false"
        tokens = self.get_tokens(input_text)
        self.assertEqual(tokens[0].type, BooleanExpressionLexer.BOOL)  
        self.assertEqual(tokens[0].text, "true")
        self.assertEqual(tokens[1].type, BooleanExpressionLexer.AND)  
        self.assertEqual(tokens[2].type, BooleanExpressionLexer.BOOL)  
        self.assertEqual(tokens[2].text, "false")

        input_text = "true OR false"
        tokens = self.get_tokens(input_text)
        self.assertEqual(tokens[0].type, BooleanExpressionLexer.BOOL)  
        self.assertEqual(tokens[0].text, "true")
        self.assertEqual(tokens[1].type, BooleanExpressionLexer.OR)  
        self.assertEqual(tokens[2].type, BooleanExpressionLexer.BOOL)  
        self.assertEqual(tokens[2].text, "false")

        input_text = "NOT true"
        tokens = self.get_tokens(input_text)
        self.assertEqual(tokens[0].type, BooleanExpressionLexer.NOT) 
        self.assertEqual(tokens[0].text, "NOT")
        self.assertEqual(tokens[1].type, BooleanExpressionLexer.BOOL) 
        self.assertEqual(tokens[1].text, "true")


    def test_parentheses(self):
        input_text = "(1 < 2)"
        tokens = self.get_tokens(input_text)
        self.assertEqual(tokens[0].type, BooleanExpressionLexer.T__4)  
        self.assertEqual(tokens[1].type, BooleanExpressionLexer.NUMBER) 
        self.assertEqual(tokens[1].text, "1")
        self.assertEqual(tokens[2].type, BooleanExpressionLexer.T__0)  
        self.assertEqual(tokens[3].type, BooleanExpressionLexer.NUMBER)  
        self.assertEqual(tokens[3].text, "2")
        self.assertEqual(tokens[4].type, BooleanExpressionLexer.T__5)  

    def test_whitespace(self):
        input_text = " true  OR false "
        tokens = self.get_tokens(input_text)
        self.assertEqual(tokens[0].type, BooleanExpressionLexer.BOOL) 
        self.assertEqual(tokens[0].text, "true")
        self.assertEqual(tokens[1].type, BooleanExpressionLexer.OR)  
        self.assertEqual(tokens[2].type, BooleanExpressionLexer.BOOL)  
        self.assertEqual(tokens[2].text, "false")

    

    def test_greater_than_operator(self):
        input_text = "3 > 2"
        tokens = self.get_tokens(input_text)
        self.assertEqual(tokens[0].type, BooleanExpressionLexer.NUMBER)  
        self.assertEqual(tokens[1].type, BooleanExpressionLexer.T__1)  
        self.assertEqual(tokens[2].type, BooleanExpressionLexer.NUMBER)  

    def test_equality_operator(self):
        input_text = "1 == 1"
        tokens = self.get_tokens(input_text)
        self.assertEqual(tokens[0].type, BooleanExpressionLexer.NUMBER)  
        self.assertEqual(tokens[1].type, BooleanExpressionLexer.T__2)  
        self.assertEqual(tokens[2].type, BooleanExpressionLexer.NUMBER) 

    def test_inequality_operator(self):
        input_text = "1 != 2"
        tokens = self.get_tokens(input_text)
        self.assertEqual(tokens[0].type, BooleanExpressionLexer.NUMBER)  
        self.assertEqual(tokens[1].type, BooleanExpressionLexer.T__3) 
        self.assertEqual(tokens[2].type, BooleanExpressionLexer.NUMBER) 





if __name__ == '__main__':
    unittest.main()
