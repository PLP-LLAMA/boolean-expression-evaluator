# Generated from BooleanExpressionV2.g4 by ANTLR 4.13.2
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
        4,1,16,65,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,5,0,18,8,0,10,0,12,0,21,9,0,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,3,1,33,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,
        59,8,2,1,3,1,3,3,3,63,8,3,1,3,0,1,0,4,0,2,4,6,0,0,73,0,8,1,0,0,0,
        2,32,1,0,0,0,4,58,1,0,0,0,6,62,1,0,0,0,8,9,6,0,-1,0,9,10,3,2,1,0,
        10,19,1,0,0,0,11,12,10,3,0,0,12,13,5,3,0,0,13,18,3,2,1,0,14,15,10,
        2,0,0,15,16,5,4,0,0,16,18,3,2,1,0,17,11,1,0,0,0,17,14,1,0,0,0,18,
        21,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,1,1,0,0,0,21,19,1,0,0,
        0,22,23,5,5,0,0,23,33,3,2,1,0,24,33,3,4,2,0,25,33,5,12,0,0,26,33,
        5,13,0,0,27,33,5,14,0,0,28,29,5,1,0,0,29,30,3,0,0,0,30,31,5,2,0,
        0,31,33,1,0,0,0,32,22,1,0,0,0,32,24,1,0,0,0,32,25,1,0,0,0,32,26,
        1,0,0,0,32,27,1,0,0,0,32,28,1,0,0,0,33,3,1,0,0,0,34,35,3,6,3,0,35,
        36,5,6,0,0,36,37,3,6,3,0,37,59,1,0,0,0,38,39,3,6,3,0,39,40,5,7,0,
        0,40,41,3,6,3,0,41,59,1,0,0,0,42,43,3,6,3,0,43,44,5,8,0,0,44,45,
        3,6,3,0,45,59,1,0,0,0,46,47,3,6,3,0,47,48,5,9,0,0,48,49,3,6,3,0,
        49,59,1,0,0,0,50,51,3,6,3,0,51,52,5,10,0,0,52,53,3,6,3,0,53,59,1,
        0,0,0,54,55,3,6,3,0,55,56,5,11,0,0,56,57,3,6,3,0,57,59,1,0,0,0,58,
        34,1,0,0,0,58,38,1,0,0,0,58,42,1,0,0,0,58,46,1,0,0,0,58,50,1,0,0,
        0,58,54,1,0,0,0,59,5,1,0,0,0,60,63,5,14,0,0,61,63,5,15,0,0,62,60,
        1,0,0,0,62,61,1,0,0,0,63,7,1,0,0,0,5,17,19,32,58,62
    ]

class BooleanExpressionV2Parser ( Parser ):

    grammarFileName = "BooleanExpressionV2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'AND'", "'OR'", "'NOT'", 
                     "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'True'", 
                     "'False'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "AND", "OR", 
                      "NOT", "EQ", "NEQ", "LT", "GT", "LE", "GE", "TRUE", 
                      "FALSE", "ID", "NUMBER", "WS" ]

    RULE_expr = 0
    RULE_term = 1
    RULE_comparison = 2
    RULE_factor = 3

    ruleNames =  [ "expr", "term", "comparison", "factor" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    AND=3
    OR=4
    NOT=5
    EQ=6
    NEQ=7
    LT=8
    GT=9
    LE=10
    GE=11
    TRUE=12
    FALSE=13
    ID=14
    NUMBER=15
    WS=16

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


    class TermExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BooleanExpressionV2Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(BooleanExpressionV2Parser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermExpr" ):
                listener.enterTermExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermExpr" ):
                listener.exitTermExpr(self)


    class AndExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BooleanExpressionV2Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(BooleanExpressionV2Parser.ExprContext,0)

        def AND(self):
            return self.getToken(BooleanExpressionV2Parser.AND, 0)
        def term(self):
            return self.getTypedRuleContext(BooleanExpressionV2Parser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpr" ):
                listener.enterAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpr" ):
                listener.exitAndExpr(self)


    class OrExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BooleanExpressionV2Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(BooleanExpressionV2Parser.ExprContext,0)

        def OR(self):
            return self.getToken(BooleanExpressionV2Parser.OR, 0)
        def term(self):
            return self.getTypedRuleContext(BooleanExpressionV2Parser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpr" ):
                listener.enterOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpr" ):
                listener.exitOrExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BooleanExpressionV2Parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = BooleanExpressionV2Parser.TermExprContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 9
            self.term()
            self._ctx.stop = self._input.LT(-1)
            self.state = 19
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 17
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        localctx = BooleanExpressionV2Parser.AndExprContext(self, BooleanExpressionV2Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 11
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 12
                        self.match(BooleanExpressionV2Parser.AND)
                        self.state = 13
                        self.term()
                        pass

                    elif la_ == 2:
                        localctx = BooleanExpressionV2Parser.OrExprContext(self, BooleanExpressionV2Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 14
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 15
                        self.match(BooleanExpressionV2Parser.OR)
                        self.state = 16
                        self.term()
                        pass

             
                self.state = 21
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BooleanExpressionV2Parser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FalseTermContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BooleanExpressionV2Parser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FALSE(self):
            return self.getToken(BooleanExpressionV2Parser.FALSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFalseTerm" ):
                listener.enterFalseTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFalseTerm" ):
                listener.exitFalseTerm(self)


    class NotTermContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BooleanExpressionV2Parser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(BooleanExpressionV2Parser.NOT, 0)
        def term(self):
            return self.getTypedRuleContext(BooleanExpressionV2Parser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotTerm" ):
                listener.enterNotTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotTerm" ):
                listener.exitNotTerm(self)


    class ComparisonTermContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BooleanExpressionV2Parser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def comparison(self):
            return self.getTypedRuleContext(BooleanExpressionV2Parser.ComparisonContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonTerm" ):
                listener.enterComparisonTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonTerm" ):
                listener.exitComparisonTerm(self)


    class VariableTermContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BooleanExpressionV2Parser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(BooleanExpressionV2Parser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableTerm" ):
                listener.enterVariableTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableTerm" ):
                listener.exitVariableTerm(self)


    class ParenExprContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BooleanExpressionV2Parser.TermContext
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


    class TrueTermContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BooleanExpressionV2Parser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(BooleanExpressionV2Parser.TRUE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrueTerm" ):
                listener.enterTrueTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrueTerm" ):
                listener.exitTrueTerm(self)



    def term(self):

        localctx = BooleanExpressionV2Parser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_term)
        try:
            self.state = 32
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = BooleanExpressionV2Parser.NotTermContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.match(BooleanExpressionV2Parser.NOT)
                self.state = 23
                self.term()
                pass

            elif la_ == 2:
                localctx = BooleanExpressionV2Parser.ComparisonTermContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.comparison()
                pass

            elif la_ == 3:
                localctx = BooleanExpressionV2Parser.TrueTermContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.match(BooleanExpressionV2Parser.TRUE)
                pass

            elif la_ == 4:
                localctx = BooleanExpressionV2Parser.FalseTermContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 26
                self.match(BooleanExpressionV2Parser.FALSE)
                pass

            elif la_ == 5:
                localctx = BooleanExpressionV2Parser.VariableTermContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 27
                self.match(BooleanExpressionV2Parser.ID)
                pass

            elif la_ == 6:
                localctx = BooleanExpressionV2Parser.ParenExprContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 28
                self.match(BooleanExpressionV2Parser.T__0)
                self.state = 29
                self.expr(0)
                self.state = 30
                self.match(BooleanExpressionV2Parser.T__1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BooleanExpressionV2Parser.RULE_comparison

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class EqualExprContext(ComparisonContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BooleanExpressionV2Parser.ComparisonContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BooleanExpressionV2Parser.FactorContext)
            else:
                return self.getTypedRuleContext(BooleanExpressionV2Parser.FactorContext,i)

        def EQ(self):
            return self.getToken(BooleanExpressionV2Parser.EQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualExpr" ):
                listener.enterEqualExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualExpr" ):
                listener.exitEqualExpr(self)


    class GreaterThanExprContext(ComparisonContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BooleanExpressionV2Parser.ComparisonContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BooleanExpressionV2Parser.FactorContext)
            else:
                return self.getTypedRuleContext(BooleanExpressionV2Parser.FactorContext,i)

        def GT(self):
            return self.getToken(BooleanExpressionV2Parser.GT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreaterThanExpr" ):
                listener.enterGreaterThanExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreaterThanExpr" ):
                listener.exitGreaterThanExpr(self)


    class GreaterEqualExprContext(ComparisonContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BooleanExpressionV2Parser.ComparisonContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BooleanExpressionV2Parser.FactorContext)
            else:
                return self.getTypedRuleContext(BooleanExpressionV2Parser.FactorContext,i)

        def GE(self):
            return self.getToken(BooleanExpressionV2Parser.GE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreaterEqualExpr" ):
                listener.enterGreaterEqualExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreaterEqualExpr" ):
                listener.exitGreaterEqualExpr(self)


    class NotEqualExprContext(ComparisonContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BooleanExpressionV2Parser.ComparisonContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BooleanExpressionV2Parser.FactorContext)
            else:
                return self.getTypedRuleContext(BooleanExpressionV2Parser.FactorContext,i)

        def NEQ(self):
            return self.getToken(BooleanExpressionV2Parser.NEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotEqualExpr" ):
                listener.enterNotEqualExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotEqualExpr" ):
                listener.exitNotEqualExpr(self)


    class LessThanExprContext(ComparisonContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BooleanExpressionV2Parser.ComparisonContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BooleanExpressionV2Parser.FactorContext)
            else:
                return self.getTypedRuleContext(BooleanExpressionV2Parser.FactorContext,i)

        def LT(self):
            return self.getToken(BooleanExpressionV2Parser.LT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLessThanExpr" ):
                listener.enterLessThanExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLessThanExpr" ):
                listener.exitLessThanExpr(self)


    class LessEqualExprContext(ComparisonContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BooleanExpressionV2Parser.ComparisonContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BooleanExpressionV2Parser.FactorContext)
            else:
                return self.getTypedRuleContext(BooleanExpressionV2Parser.FactorContext,i)

        def LE(self):
            return self.getToken(BooleanExpressionV2Parser.LE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLessEqualExpr" ):
                listener.enterLessEqualExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLessEqualExpr" ):
                listener.exitLessEqualExpr(self)



    def comparison(self):

        localctx = BooleanExpressionV2Parser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_comparison)
        try:
            self.state = 58
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = BooleanExpressionV2Parser.EqualExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.factor()
                self.state = 35
                self.match(BooleanExpressionV2Parser.EQ)
                self.state = 36
                self.factor()
                pass

            elif la_ == 2:
                localctx = BooleanExpressionV2Parser.NotEqualExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.factor()
                self.state = 39
                self.match(BooleanExpressionV2Parser.NEQ)
                self.state = 40
                self.factor()
                pass

            elif la_ == 3:
                localctx = BooleanExpressionV2Parser.LessThanExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 42
                self.factor()
                self.state = 43
                self.match(BooleanExpressionV2Parser.LT)
                self.state = 44
                self.factor()
                pass

            elif la_ == 4:
                localctx = BooleanExpressionV2Parser.GreaterThanExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 46
                self.factor()
                self.state = 47
                self.match(BooleanExpressionV2Parser.GT)
                self.state = 48
                self.factor()
                pass

            elif la_ == 5:
                localctx = BooleanExpressionV2Parser.LessEqualExprContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 50
                self.factor()
                self.state = 51
                self.match(BooleanExpressionV2Parser.LE)
                self.state = 52
                self.factor()
                pass

            elif la_ == 6:
                localctx = BooleanExpressionV2Parser.GreaterEqualExprContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 54
                self.factor()
                self.state = 55
                self.match(BooleanExpressionV2Parser.GE)
                self.state = 56
                self.factor()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BooleanExpressionV2Parser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class VariableFactorContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BooleanExpressionV2Parser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(BooleanExpressionV2Parser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableFactor" ):
                listener.enterVariableFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableFactor" ):
                listener.exitVariableFactor(self)


    class NumberFactorContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BooleanExpressionV2Parser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(BooleanExpressionV2Parser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberFactor" ):
                listener.enterNumberFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberFactor" ):
                listener.exitNumberFactor(self)



    def factor(self):

        localctx = BooleanExpressionV2Parser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_factor)
        try:
            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                localctx = BooleanExpressionV2Parser.VariableFactorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.match(BooleanExpressionV2Parser.ID)
                pass
            elif token in [15]:
                localctx = BooleanExpressionV2Parser.NumberFactorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.match(BooleanExpressionV2Parser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




