# Generated from grammar/boolean_expression/BooleanExpression.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BooleanExpressionParser import BooleanExpressionParser
else:
    from BooleanExpressionParser import BooleanExpressionParser

# This class defines a complete listener for a parse tree produced by BooleanExpressionParser.
class BooleanExpressionListener(ParseTreeListener):

    # Enter a parse tree produced by BooleanExpressionParser#AndExpr.
    def enterAndExpr(self, ctx:BooleanExpressionParser.AndExprContext):
        pass

    # Exit a parse tree produced by BooleanExpressionParser#AndExpr.
    def exitAndExpr(self, ctx:BooleanExpressionParser.AndExprContext):
        pass


    # Enter a parse tree produced by BooleanExpressionParser#BoolExpr.
    def enterBoolExpr(self, ctx:BooleanExpressionParser.BoolExprContext):
        pass

    # Exit a parse tree produced by BooleanExpressionParser#BoolExpr.
    def exitBoolExpr(self, ctx:BooleanExpressionParser.BoolExprContext):
        pass


    # Enter a parse tree produced by BooleanExpressionParser#GreaterThanExpr.
    def enterGreaterThanExpr(self, ctx:BooleanExpressionParser.GreaterThanExprContext):
        pass

    # Exit a parse tree produced by BooleanExpressionParser#GreaterThanExpr.
    def exitGreaterThanExpr(self, ctx:BooleanExpressionParser.GreaterThanExprContext):
        pass


    # Enter a parse tree produced by BooleanExpressionParser#EqualsExpr.
    def enterEqualsExpr(self, ctx:BooleanExpressionParser.EqualsExprContext):
        pass

    # Exit a parse tree produced by BooleanExpressionParser#EqualsExpr.
    def exitEqualsExpr(self, ctx:BooleanExpressionParser.EqualsExprContext):
        pass


    # Enter a parse tree produced by BooleanExpressionParser#NumberExpr.
    def enterNumberExpr(self, ctx:BooleanExpressionParser.NumberExprContext):
        pass

    # Exit a parse tree produced by BooleanExpressionParser#NumberExpr.
    def exitNumberExpr(self, ctx:BooleanExpressionParser.NumberExprContext):
        pass


    # Enter a parse tree produced by BooleanExpressionParser#VarExpr.
    def enterVarExpr(self, ctx:BooleanExpressionParser.VarExprContext):
        pass

    # Exit a parse tree produced by BooleanExpressionParser#VarExpr.
    def exitVarExpr(self, ctx:BooleanExpressionParser.VarExprContext):
        pass


    # Enter a parse tree produced by BooleanExpressionParser#NotExpr.
    def enterNotExpr(self, ctx:BooleanExpressionParser.NotExprContext):
        pass

    # Exit a parse tree produced by BooleanExpressionParser#NotExpr.
    def exitNotExpr(self, ctx:BooleanExpressionParser.NotExprContext):
        pass


    # Enter a parse tree produced by BooleanExpressionParser#ParenExpr.
    def enterParenExpr(self, ctx:BooleanExpressionParser.ParenExprContext):
        pass

    # Exit a parse tree produced by BooleanExpressionParser#ParenExpr.
    def exitParenExpr(self, ctx:BooleanExpressionParser.ParenExprContext):
        pass


    # Enter a parse tree produced by BooleanExpressionParser#LessThanExpr.
    def enterLessThanExpr(self, ctx:BooleanExpressionParser.LessThanExprContext):
        pass

    # Exit a parse tree produced by BooleanExpressionParser#LessThanExpr.
    def exitLessThanExpr(self, ctx:BooleanExpressionParser.LessThanExprContext):
        pass


    # Enter a parse tree produced by BooleanExpressionParser#NotEqualsExpr.
    def enterNotEqualsExpr(self, ctx:BooleanExpressionParser.NotEqualsExprContext):
        pass

    # Exit a parse tree produced by BooleanExpressionParser#NotEqualsExpr.
    def exitNotEqualsExpr(self, ctx:BooleanExpressionParser.NotEqualsExprContext):
        pass


    # Enter a parse tree produced by BooleanExpressionParser#OrExpr.
    def enterOrExpr(self, ctx:BooleanExpressionParser.OrExprContext):
        pass

    # Exit a parse tree produced by BooleanExpressionParser#OrExpr.
    def exitOrExpr(self, ctx:BooleanExpressionParser.OrExprContext):
        pass



del BooleanExpressionParser