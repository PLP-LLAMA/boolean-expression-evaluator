# example: calculator - evaluator
# reference: https://medium.com/@kv391/antlr4-grammar-a-quick-tutorial-e1f0fb6ca4ff


from grammar.calculator.CalculatorListener import CalculatorListener


class CalcEvaluator(CalculatorListener):
    def __init__(self):
        self.stack = []

    def exitExpr(self, ctx):
        if ctx.getChildCount() == 3:
            right = self.stack.pop()
            left = self.stack.pop()
            op = ctx.getChild(1).getText()
            if op == "+":
                self.stack.append(left + right)
            elif op == "-":
                self.stack.append(left - right)

    def exitTerm(self, ctx):
        if ctx.getChildCount() == 3:
            right = self.stack.pop()
            left = self.stack.pop()
            op = ctx.getChild(1).getText()
            if op == "*":
                self.stack.append(left * right)
            elif op == "/":
                self.stack.append(left / right)

    def exitFactor(self, ctx):
        if ctx.getChildCount() == 1:
            self.stack.append(float(ctx.getText()))
        elif ctx.getChildCount() == 2:
            self.stack.append(-self.stack.pop())

    def getValue(self):
        return self.stack[0]
