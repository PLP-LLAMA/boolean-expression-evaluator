# Generated from grammar/boolean_expression_v2/BooleanExpressionV2.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,38,2,0,7,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,13,
        8,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
        1,0,1,0,1,0,5,0,33,8,0,10,0,12,0,36,9,0,1,0,0,1,0,1,0,0,0,46,0,12,
        1,0,0,0,2,3,6,0,-1,0,3,4,5,9,0,0,4,13,3,0,0,9,5,6,5,5,0,0,6,7,3,
        0,0,0,7,8,5,6,0,0,8,13,1,0,0,0,9,13,5,11,0,0,10,13,5,10,0,0,11,13,
        5,12,0,0,12,2,1,0,0,0,12,5,1,0,0,0,12,9,1,0,0,0,12,10,1,0,0,0,12,
        11,1,0,0,0,13,34,1,0,0,0,14,15,10,11,0,0,15,16,5,8,0,0,16,33,3,0,
        0,12,17,18,10,10,0,0,18,19,5,7,0,0,19,33,3,0,0,11,20,21,10,8,0,0,
        21,22,5,1,0,0,22,33,3,0,0,9,23,24,10,7,0,0,24,25,5,2,0,0,25,33,3,
        0,0,8,26,27,10,6,0,0,27,28,5,3,0,0,28,33,3,0,0,7,29,30,10,5,0,0,
        30,31,5,4,0,0,31,33,3,0,0,6,32,14,1,0,0,0,32,17,1,0,0,0,32,20,1,
        0,0,0,32,23,1,0,0,0,32,26,1,0,0,0,32,29,1,0,0,0,33,36,1,0,0,0,34,
        32,1,0,0,0,34,35,1,0,0,0,35,1,1,0,0,0,36,34,1,0,0,0,3,12,32,34
    ]

class BooleanExpressionV2Parser ( Parser ):

    grammarFileName = "BooleanExpressionV2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<'", "'>'", "'=='", "'!='", "'('", "')'", 
                     "'AND'", "'OR'", "'NOT'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "AND", "OR", 
                      "NOT", "BOOL", "IDENTIFIER", "NUMBER", "WS" ]

    RULE_expr = 0

    ruleNames =  [ "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    AND=7
    OR=8
    NOT=9
    BOOL=10
    IDENTIFIER=11
    NUMBER=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BooleanExpressionV2Parser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AndExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BooleanExpressionV2Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BooleanExpressionV2Parser.ExprContext)
            else:
                return self.getTypedRuleContext(BooleanExpressionV2Parser.ExprContext,i)

        def AND(self):
            return self.getToken(BooleanExpressionV2Parser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpr" ):
                listener.enterAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpr" ):
                listener.exitAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)


    class BoolExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BooleanExpressionV2Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(BooleanExpressionV2Parser.BOOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolExpr" ):
                listener.enterBoolExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolExpr" ):
                listener.exitBoolExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolExpr" ):
                return visitor.visitBoolExpr(self)
            else:
                return visitor.visitChildren(self)


    class GreaterThanExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BooleanExpressionV2Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BooleanExpressionV2Parser.ExprContext)
            else:
                return self.getTypedRuleContext(BooleanExpressionV2Parser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreaterThanExpr" ):
                listener.enterGreaterThanExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreaterThanExpr" ):
                listener.exitGreaterThanExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGreaterThanExpr" ):
                return visitor.visitGreaterThanExpr(self)
            else:
                return visitor.visitChildren(self)


    class EqualsExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BooleanExpressionV2Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BooleanExpressionV2Parser.ExprContext)
            else:
                return self.getTypedRuleContext(BooleanExpressionV2Parser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualsExpr" ):
                listener.enterEqualsExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualsExpr" ):
                listener.exitEqualsExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualsExpr" ):
                return visitor.visitEqualsExpr(self)
            else:
                return visitor.visitChildren(self)


    class NumberExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BooleanExpressionV2Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(BooleanExpressionV2Parser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpr" ):
                listener.enterNumberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpr" ):
                listener.exitNumberExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExpr" ):
                return visitor.visitNumberExpr(self)
            else:
                return visitor.visitChildren(self)


    class VarExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BooleanExpressionV2Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(BooleanExpressionV2Parser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarExpr" ):
                listener.enterVarExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarExpr" ):
                listener.exitVarExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarExpr" ):
                return visitor.visitVarExpr(self)
            else:
                return visitor.visitChildren(self)


    class NotExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BooleanExpressionV2Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(BooleanExpressionV2Parser.NOT, 0)
        def expr(self):
            return self.getTypedRuleContext(BooleanExpressionV2Parser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpr" ):
                listener.enterNotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpr" ):
                listener.exitNotExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BooleanExpressionV2Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(BooleanExpressionV2Parser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class LessThanExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BooleanExpressionV2Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BooleanExpressionV2Parser.ExprContext)
            else:
                return self.getTypedRuleContext(BooleanExpressionV2Parser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLessThanExpr" ):
                listener.enterLessThanExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLessThanExpr" ):
                listener.exitLessThanExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLessThanExpr" ):
                return visitor.visitLessThanExpr(self)
            else:
                return visitor.visitChildren(self)


    class NotEqualsExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BooleanExpressionV2Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BooleanExpressionV2Parser.ExprContext)
            else:
                return self.getTypedRuleContext(BooleanExpressionV2Parser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotEqualsExpr" ):
                listener.enterNotEqualsExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotEqualsExpr" ):
                listener.exitNotEqualsExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotEqualsExpr" ):
                return visitor.visitNotEqualsExpr(self)
            else:
                return visitor.visitChildren(self)


    class OrExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BooleanExpressionV2Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BooleanExpressionV2Parser.ExprContext)
            else:
                return self.getTypedRuleContext(BooleanExpressionV2Parser.ExprContext,i)

        def OR(self):
            return self.getToken(BooleanExpressionV2Parser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpr" ):
                listener.enterOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpr" ):
                listener.exitOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BooleanExpressionV2Parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                localctx = BooleanExpressionV2Parser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 3
                self.match(BooleanExpressionV2Parser.NOT)
                self.state = 4
                self.expr(9)
                pass
            elif token in [5]:
                localctx = BooleanExpressionV2Parser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 5
                self.match(BooleanExpressionV2Parser.T__4)
                self.state = 6
                self.expr(0)
                self.state = 7
                self.match(BooleanExpressionV2Parser.T__5)
                pass
            elif token in [11]:
                localctx = BooleanExpressionV2Parser.VarExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 9
                self.match(BooleanExpressionV2Parser.IDENTIFIER)
                pass
            elif token in [10]:
                localctx = BooleanExpressionV2Parser.BoolExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 10
                self.match(BooleanExpressionV2Parser.BOOL)
                pass
            elif token in [12]:
                localctx = BooleanExpressionV2Parser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 11
                self.match(BooleanExpressionV2Parser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 34
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 32
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = BooleanExpressionV2Parser.OrExprContext(self, BooleanExpressionV2Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 14
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 15
                        self.match(BooleanExpressionV2Parser.OR)
                        self.state = 16
                        self.expr(12)
                        pass

                    elif la_ == 2:
                        localctx = BooleanExpressionV2Parser.AndExprContext(self, BooleanExpressionV2Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 17
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 18
                        self.match(BooleanExpressionV2Parser.AND)
                        self.state = 19
                        self.expr(11)
                        pass

                    elif la_ == 3:
                        localctx = BooleanExpressionV2Parser.LessThanExprContext(self, BooleanExpressionV2Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 20
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 21
                        self.match(BooleanExpressionV2Parser.T__0)
                        self.state = 22
                        self.expr(9)
                        pass

                    elif la_ == 4:
                        localctx = BooleanExpressionV2Parser.GreaterThanExprContext(self, BooleanExpressionV2Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 23
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 24
                        self.match(BooleanExpressionV2Parser.T__1)
                        self.state = 25
                        self.expr(8)
                        pass

                    elif la_ == 5:
                        localctx = BooleanExpressionV2Parser.EqualsExprContext(self, BooleanExpressionV2Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 26
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 27
                        self.match(BooleanExpressionV2Parser.T__2)
                        self.state = 28
                        self.expr(7)
                        pass

                    elif la_ == 6:
                        localctx = BooleanExpressionV2Parser.NotEqualsExprContext(self, BooleanExpressionV2Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 29
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 30
                        self.match(BooleanExpressionV2Parser.T__3)
                        self.state = 31
                        self.expr(6)
                        pass

             
                self.state = 36
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 5)
         




