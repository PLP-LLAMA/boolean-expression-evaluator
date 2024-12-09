# Generated from grammar/boolean_expression_v2/BooleanExpressionV2.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BooleanExpressionV2Parser import BooleanExpressionV2Parser
else:
    from BooleanExpressionV2Parser import BooleanExpressionV2Parser

# This class defines a complete generic visitor for a parse tree produced by BooleanExpressionV2Parser.

class BooleanExpressionV2Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by BooleanExpressionV2Parser#AndExpr.
    def visitAndExpr(self, ctx:BooleanExpressionV2Parser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BooleanExpressionV2Parser#BoolExpr.
    def visitBoolExpr(self, ctx:BooleanExpressionV2Parser.BoolExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BooleanExpressionV2Parser#GreaterThanExpr.
    def visitGreaterThanExpr(self, ctx:BooleanExpressionV2Parser.GreaterThanExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BooleanExpressionV2Parser#EqualsExpr.
    def visitEqualsExpr(self, ctx:BooleanExpressionV2Parser.EqualsExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BooleanExpressionV2Parser#NumberExpr.
    def visitNumberExpr(self, ctx:BooleanExpressionV2Parser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BooleanExpressionV2Parser#VarExpr.
    def visitVarExpr(self, ctx:BooleanExpressionV2Parser.VarExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BooleanExpressionV2Parser#NotExpr.
    def visitNotExpr(self, ctx:BooleanExpressionV2Parser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BooleanExpressionV2Parser#ParenExpr.
    def visitParenExpr(self, ctx:BooleanExpressionV2Parser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BooleanExpressionV2Parser#LessThanExpr.
    def visitLessThanExpr(self, ctx:BooleanExpressionV2Parser.LessThanExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BooleanExpressionV2Parser#NotEqualsExpr.
    def visitNotEqualsExpr(self, ctx:BooleanExpressionV2Parser.NotEqualsExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BooleanExpressionV2Parser#OrExpr.
    def visitOrExpr(self, ctx:BooleanExpressionV2Parser.OrExprContext):
        return self.visitChildren(ctx)



del BooleanExpressionV2Parser