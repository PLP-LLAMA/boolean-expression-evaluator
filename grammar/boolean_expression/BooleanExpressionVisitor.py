# Generated from grammar/boolean_expression/BooleanExpression.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BooleanExpressionParser import BooleanExpressionParser
else:
    from BooleanExpressionParser import BooleanExpressionParser

# This class defines a complete generic visitor for a parse tree produced by BooleanExpressionParser.

class BooleanExpressionVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BooleanExpressionParser#AndExpr.
    def visitAndExpr(self, ctx:BooleanExpressionParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BooleanExpressionParser#BoolExpr.
    def visitBoolExpr(self, ctx:BooleanExpressionParser.BoolExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BooleanExpressionParser#GreaterThanExpr.
    def visitGreaterThanExpr(self, ctx:BooleanExpressionParser.GreaterThanExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BooleanExpressionParser#EqualsExpr.
    def visitEqualsExpr(self, ctx:BooleanExpressionParser.EqualsExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BooleanExpressionParser#NumberExpr.
    def visitNumberExpr(self, ctx:BooleanExpressionParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BooleanExpressionParser#VarExpr.
    def visitVarExpr(self, ctx:BooleanExpressionParser.VarExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BooleanExpressionParser#NotExpr.
    def visitNotExpr(self, ctx:BooleanExpressionParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BooleanExpressionParser#ParenExpr.
    def visitParenExpr(self, ctx:BooleanExpressionParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BooleanExpressionParser#LessThanExpr.
    def visitLessThanExpr(self, ctx:BooleanExpressionParser.LessThanExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BooleanExpressionParser#NotEqualsExpr.
    def visitNotEqualsExpr(self, ctx:BooleanExpressionParser.NotEqualsExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BooleanExpressionParser#OrExpr.
    def visitOrExpr(self, ctx:BooleanExpressionParser.OrExprContext):
        return self.visitChildren(ctx)



del BooleanExpressionParser