# Generated from grammar/boolean_expression_v2/BooleanExpressionV2.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BooleanExpressionV2Parser import BooleanExpressionV2Parser
else:
    from BooleanExpressionV2Parser import BooleanExpressionV2Parser

# This class defines a complete listener for a parse tree produced by BooleanExpressionV2Parser.
class BooleanExpressionV2Listener(ParseTreeListener):

    # Enter a parse tree produced by BooleanExpressionV2Parser#AndExpr.
    def enterAndExpr(self, ctx:BooleanExpressionV2Parser.AndExprContext):
        pass

    # Exit a parse tree produced by BooleanExpressionV2Parser#AndExpr.
    def exitAndExpr(self, ctx:BooleanExpressionV2Parser.AndExprContext):
        pass


    # Enter a parse tree produced by BooleanExpressionV2Parser#BoolExpr.
    def enterBoolExpr(self, ctx:BooleanExpressionV2Parser.BoolExprContext):
        pass

    # Exit a parse tree produced by BooleanExpressionV2Parser#BoolExpr.
    def exitBoolExpr(self, ctx:BooleanExpressionV2Parser.BoolExprContext):
        pass


    # Enter a parse tree produced by BooleanExpressionV2Parser#GreaterThanExpr.
    def enterGreaterThanExpr(self, ctx:BooleanExpressionV2Parser.GreaterThanExprContext):
        pass

    # Exit a parse tree produced by BooleanExpressionV2Parser#GreaterThanExpr.
    def exitGreaterThanExpr(self, ctx:BooleanExpressionV2Parser.GreaterThanExprContext):
        pass


    # Enter a parse tree produced by BooleanExpressionV2Parser#EqualsExpr.
    def enterEqualsExpr(self, ctx:BooleanExpressionV2Parser.EqualsExprContext):
        pass

    # Exit a parse tree produced by BooleanExpressionV2Parser#EqualsExpr.
    def exitEqualsExpr(self, ctx:BooleanExpressionV2Parser.EqualsExprContext):
        pass


    # Enter a parse tree produced by BooleanExpressionV2Parser#NumberExpr.
    def enterNumberExpr(self, ctx:BooleanExpressionV2Parser.NumberExprContext):
        pass

    # Exit a parse tree produced by BooleanExpressionV2Parser#NumberExpr.
    def exitNumberExpr(self, ctx:BooleanExpressionV2Parser.NumberExprContext):
        pass


    # Enter a parse tree produced by BooleanExpressionV2Parser#VarExpr.
    def enterVarExpr(self, ctx:BooleanExpressionV2Parser.VarExprContext):
        pass

    # Exit a parse tree produced by BooleanExpressionV2Parser#VarExpr.
    def exitVarExpr(self, ctx:BooleanExpressionV2Parser.VarExprContext):
        pass


    # Enter a parse tree produced by BooleanExpressionV2Parser#NotExpr.
    def enterNotExpr(self, ctx:BooleanExpressionV2Parser.NotExprContext):
        pass

    # Exit a parse tree produced by BooleanExpressionV2Parser#NotExpr.
    def exitNotExpr(self, ctx:BooleanExpressionV2Parser.NotExprContext):
        pass


    # Enter a parse tree produced by BooleanExpressionV2Parser#ParenExpr.
    def enterParenExpr(self, ctx:BooleanExpressionV2Parser.ParenExprContext):
        pass

    # Exit a parse tree produced by BooleanExpressionV2Parser#ParenExpr.
    def exitParenExpr(self, ctx:BooleanExpressionV2Parser.ParenExprContext):
        pass


    # Enter a parse tree produced by BooleanExpressionV2Parser#LessThanExpr.
    def enterLessThanExpr(self, ctx:BooleanExpressionV2Parser.LessThanExprContext):
        pass

    # Exit a parse tree produced by BooleanExpressionV2Parser#LessThanExpr.
    def exitLessThanExpr(self, ctx:BooleanExpressionV2Parser.LessThanExprContext):
        pass


    # Enter a parse tree produced by BooleanExpressionV2Parser#NotEqualsExpr.
    def enterNotEqualsExpr(self, ctx:BooleanExpressionV2Parser.NotEqualsExprContext):
        pass

    # Exit a parse tree produced by BooleanExpressionV2Parser#NotEqualsExpr.
    def exitNotEqualsExpr(self, ctx:BooleanExpressionV2Parser.NotEqualsExprContext):
        pass


    # Enter a parse tree produced by BooleanExpressionV2Parser#OrExpr.
    def enterOrExpr(self, ctx:BooleanExpressionV2Parser.OrExprContext):
        pass

    # Exit a parse tree produced by BooleanExpressionV2Parser#OrExpr.
    def exitOrExpr(self, ctx:BooleanExpressionV2Parser.OrExprContext):
        pass



del BooleanExpressionV2Parser