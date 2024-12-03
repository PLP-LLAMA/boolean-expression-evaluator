# Generated from ./BooleanExpression.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BooleanExpressionParser import BooleanExpressionParser
else:
    from BooleanExpressionParser import BooleanExpressionParser

# This class defines a complete listener for a parse tree produced by BooleanExpressionParser.
class BooleanExpressionListener(ParseTreeListener):

    # Enter a parse tree produced by BooleanExpressionParser#program.
    def enterProgram(self, ctx:BooleanExpressionParser.ProgramContext):
        pass

    # Exit a parse tree produced by BooleanExpressionParser#program.
    def exitProgram(self, ctx:BooleanExpressionParser.ProgramContext):
        pass


    # Enter a parse tree produced by BooleanExpressionParser#statement.
    def enterStatement(self, ctx:BooleanExpressionParser.StatementContext):
        pass

    # Exit a parse tree produced by BooleanExpressionParser#statement.
    def exitStatement(self, ctx:BooleanExpressionParser.StatementContext):
        pass


    # Enter a parse tree produced by BooleanExpressionParser#declaration.
    def enterDeclaration(self, ctx:BooleanExpressionParser.DeclarationContext):
        pass

    # Exit a parse tree produced by BooleanExpressionParser#declaration.
    def exitDeclaration(self, ctx:BooleanExpressionParser.DeclarationContext):
        pass


    # Enter a parse tree produced by BooleanExpressionParser#expression.
    def enterExpression(self, ctx:BooleanExpressionParser.ExpressionContext):
        pass

    # Exit a parse tree produced by BooleanExpressionParser#expression.
    def exitExpression(self, ctx:BooleanExpressionParser.ExpressionContext):
        pass


    # Enter a parse tree produced by BooleanExpressionParser#comparisonOp.
    def enterComparisonOp(self, ctx:BooleanExpressionParser.ComparisonOpContext):
        pass

    # Exit a parse tree produced by BooleanExpressionParser#comparisonOp.
    def exitComparisonOp(self, ctx:BooleanExpressionParser.ComparisonOpContext):
        pass



del BooleanExpressionParser