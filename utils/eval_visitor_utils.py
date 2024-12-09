from grammar.boolean_expression_v2.BooleanExpressionV2Visitor import (
    BooleanExpressionV2Visitor,
)


class EvalVisitor(BooleanExpressionV2Visitor):
    def __init__(self):
        self.variables = {}

    def visitAndExpr(self, ctx):
        print("Evaluating AND expression")
        left = self.visit(ctx.expr(0))
        if not left:
            return False
        right = self.visit(ctx.expr(1))
        return left and right

    def visitOrExpr(self, ctx):
        print("Evaluating OR expression")
        left = self.visit(ctx.expr(0))
        if left:
            return True
        right = self.visit(ctx.expr(1))
        return left or right

    def visitNotExpr(self, ctx):
        return not self.visit(ctx.expr())

    def visitLessThanExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left < right

    def visitGreaterThanExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left > right

    def visitEqualsExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left == right

    def visitNotEqualsExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left != right

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitVarExpr(self, ctx):
        var_name = ctx.getText()
        if var_name not in self.variables:
            raise ValueError(f"Variable '{var_name}' is not defined.")
        return self.variables[var_name]

    def visitBoolExpr(self, ctx):
        return ctx.getText() == 'true'

    def visitNumberExpr(self, ctx):
        return int(ctx.getText())

    def declare_variable(self, name, value):
        self.variables[name] = value