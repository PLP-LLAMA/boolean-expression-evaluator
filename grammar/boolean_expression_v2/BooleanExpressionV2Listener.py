# Generated from BooleanExpressionV2.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BooleanExpressionV2Parser import BooleanExpressionV2Parser
else:
    from BooleanExpressionV2Parser import BooleanExpressionV2Parser

# This class defines a complete listener for a parse tree produced by BooleanExpressionV2Parser.
class BooleanExpressionV2Listener(ParseTreeListener):

    # Enter a parse tree produced by BooleanExpressionV2Parser#TermExpr.
    def enterTermExpr(self, ctx:BooleanExpressionV2Parser.TermExprContext):
        pass

    # Exit a parse tree produced by BooleanExpressionV2Parser#TermExpr.
    def exitTermExpr(self, ctx:BooleanExpressionV2Parser.TermExprContext):
        pass


    # Enter a parse tree produced by BooleanExpressionV2Parser#AndExpr.
    def enterAndExpr(self, ctx:BooleanExpressionV2Parser.AndExprContext):
        pass

    # Exit a parse tree produced by BooleanExpressionV2Parser#AndExpr.
    def exitAndExpr(self, ctx:BooleanExpressionV2Parser.AndExprContext):
        pass


    # Enter a parse tree produced by BooleanExpressionV2Parser#OrExpr.
    def enterOrExpr(self, ctx:BooleanExpressionV2Parser.OrExprContext):
        pass

    # Exit a parse tree produced by BooleanExpressionV2Parser#OrExpr.
    def exitOrExpr(self, ctx:BooleanExpressionV2Parser.OrExprContext):
        pass


    # Enter a parse tree produced by BooleanExpressionV2Parser#NotTerm.
    def enterNotTerm(self, ctx:BooleanExpressionV2Parser.NotTermContext):
        pass

    # Exit a parse tree produced by BooleanExpressionV2Parser#NotTerm.
    def exitNotTerm(self, ctx:BooleanExpressionV2Parser.NotTermContext):
        pass


    # Enter a parse tree produced by BooleanExpressionV2Parser#ComparisonTerm.
    def enterComparisonTerm(self, ctx:BooleanExpressionV2Parser.ComparisonTermContext):
        pass

    # Exit a parse tree produced by BooleanExpressionV2Parser#ComparisonTerm.
    def exitComparisonTerm(self, ctx:BooleanExpressionV2Parser.ComparisonTermContext):
        pass


    # Enter a parse tree produced by BooleanExpressionV2Parser#TrueTerm.
    def enterTrueTerm(self, ctx:BooleanExpressionV2Parser.TrueTermContext):
        pass

    # Exit a parse tree produced by BooleanExpressionV2Parser#TrueTerm.
    def exitTrueTerm(self, ctx:BooleanExpressionV2Parser.TrueTermContext):
        pass


    # Enter a parse tree produced by BooleanExpressionV2Parser#FalseTerm.
    def enterFalseTerm(self, ctx:BooleanExpressionV2Parser.FalseTermContext):
        pass

    # Exit a parse tree produced by BooleanExpressionV2Parser#FalseTerm.
    def exitFalseTerm(self, ctx:BooleanExpressionV2Parser.FalseTermContext):
        pass


    # Enter a parse tree produced by BooleanExpressionV2Parser#VariableTerm.
    def enterVariableTerm(self, ctx:BooleanExpressionV2Parser.VariableTermContext):
        pass

    # Exit a parse tree produced by BooleanExpressionV2Parser#VariableTerm.
    def exitVariableTerm(self, ctx:BooleanExpressionV2Parser.VariableTermContext):
        pass


    # Enter a parse tree produced by BooleanExpressionV2Parser#ParenExpr.
    def enterParenExpr(self, ctx:BooleanExpressionV2Parser.ParenExprContext):
        pass

    # Exit a parse tree produced by BooleanExpressionV2Parser#ParenExpr.
    def exitParenExpr(self, ctx:BooleanExpressionV2Parser.ParenExprContext):
        pass


    # Enter a parse tree produced by BooleanExpressionV2Parser#EqualExpr.
    def enterEqualExpr(self, ctx:BooleanExpressionV2Parser.EqualExprContext):
        pass

    # Exit a parse tree produced by BooleanExpressionV2Parser#EqualExpr.
    def exitEqualExpr(self, ctx:BooleanExpressionV2Parser.EqualExprContext):
        pass


    # Enter a parse tree produced by BooleanExpressionV2Parser#NotEqualExpr.
    def enterNotEqualExpr(self, ctx:BooleanExpressionV2Parser.NotEqualExprContext):
        pass

    # Exit a parse tree produced by BooleanExpressionV2Parser#NotEqualExpr.
    def exitNotEqualExpr(self, ctx:BooleanExpressionV2Parser.NotEqualExprContext):
        pass


    # Enter a parse tree produced by BooleanExpressionV2Parser#LessThanExpr.
    def enterLessThanExpr(self, ctx:BooleanExpressionV2Parser.LessThanExprContext):
        pass

    # Exit a parse tree produced by BooleanExpressionV2Parser#LessThanExpr.
    def exitLessThanExpr(self, ctx:BooleanExpressionV2Parser.LessThanExprContext):
        pass


    # Enter a parse tree produced by BooleanExpressionV2Parser#GreaterThanExpr.
    def enterGreaterThanExpr(self, ctx:BooleanExpressionV2Parser.GreaterThanExprContext):
        pass

    # Exit a parse tree produced by BooleanExpressionV2Parser#GreaterThanExpr.
    def exitGreaterThanExpr(self, ctx:BooleanExpressionV2Parser.GreaterThanExprContext):
        pass


    # Enter a parse tree produced by BooleanExpressionV2Parser#LessEqualExpr.
    def enterLessEqualExpr(self, ctx:BooleanExpressionV2Parser.LessEqualExprContext):
        pass

    # Exit a parse tree produced by BooleanExpressionV2Parser#LessEqualExpr.
    def exitLessEqualExpr(self, ctx:BooleanExpressionV2Parser.LessEqualExprContext):
        pass


    # Enter a parse tree produced by BooleanExpressionV2Parser#GreaterEqualExpr.
    def enterGreaterEqualExpr(self, ctx:BooleanExpressionV2Parser.GreaterEqualExprContext):
        pass

    # Exit a parse tree produced by BooleanExpressionV2Parser#GreaterEqualExpr.
    def exitGreaterEqualExpr(self, ctx:BooleanExpressionV2Parser.GreaterEqualExprContext):
        pass


    # Enter a parse tree produced by BooleanExpressionV2Parser#VariableFactor.
    def enterVariableFactor(self, ctx:BooleanExpressionV2Parser.VariableFactorContext):
        pass

    # Exit a parse tree produced by BooleanExpressionV2Parser#VariableFactor.
    def exitVariableFactor(self, ctx:BooleanExpressionV2Parser.VariableFactorContext):
        pass


    # Enter a parse tree produced by BooleanExpressionV2Parser#NumberFactor.
    def enterNumberFactor(self, ctx:BooleanExpressionV2Parser.NumberFactorContext):
        pass

    # Exit a parse tree produced by BooleanExpressionV2Parser#NumberFactor.
    def exitNumberFactor(self, ctx:BooleanExpressionV2Parser.NumberFactorContext):
        pass



del BooleanExpressionV2Parser