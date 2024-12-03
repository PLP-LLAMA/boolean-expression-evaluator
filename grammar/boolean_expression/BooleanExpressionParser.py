# Generated from ./BooleanExpression.g4 by ANTLR 4.13.2
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
        4,1,16,56,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,5,0,12,8,0,
        10,0,12,0,15,9,0,1,1,1,1,3,1,19,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,37,8,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,5,3,49,8,3,10,3,12,3,52,9,3,1,4,1,4,1,4,0,
        1,6,5,0,2,4,6,8,0,1,1,0,11,14,59,0,13,1,0,0,0,2,18,1,0,0,0,4,20,
        1,0,0,0,6,36,1,0,0,0,8,53,1,0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,
        15,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,1,1,0,0,0,15,13,1,0,0,
        0,16,19,3,4,2,0,17,19,3,6,3,0,18,16,1,0,0,0,18,17,1,0,0,0,19,3,1,
        0,0,0,20,21,5,1,0,0,21,22,5,15,0,0,22,23,5,2,0,0,23,24,3,6,3,0,24,
        25,5,3,0,0,25,5,1,0,0,0,26,27,6,3,-1,0,27,28,5,6,0,0,28,37,3,6,3,
        6,29,30,5,7,0,0,30,31,3,6,3,0,31,32,5,8,0,0,32,37,1,0,0,0,33,37,
        5,15,0,0,34,37,5,9,0,0,35,37,5,10,0,0,36,26,1,0,0,0,36,29,1,0,0,
        0,36,33,1,0,0,0,36,34,1,0,0,0,36,35,1,0,0,0,37,50,1,0,0,0,38,39,
        10,8,0,0,39,40,5,4,0,0,40,49,3,6,3,9,41,42,10,7,0,0,42,43,5,5,0,
        0,43,49,3,6,3,8,44,45,10,5,0,0,45,46,3,8,4,0,46,47,3,6,3,6,47,49,
        1,0,0,0,48,38,1,0,0,0,48,41,1,0,0,0,48,44,1,0,0,0,49,52,1,0,0,0,
        50,48,1,0,0,0,50,51,1,0,0,0,51,7,1,0,0,0,52,50,1,0,0,0,53,54,7,0,
        0,0,54,9,1,0,0,0,5,13,18,36,48,50
    ]

class BooleanExpressionParser ( Parser ):

    grammarFileName = "BooleanExpression.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'bool'", "'='", "';'", "'AND'", "'OR'", 
                     "'NOT'", "'('", "')'", "'true'", "'false'", "'=='", 
                     "'!='", "'<'", "'>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_declaration = 2
    RULE_expression = 3
    RULE_comparisonOp = 4

    ruleNames =  [ "program", "statement", "declaration", "expression", 
                   "comparisonOp" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    ID=15
    WS=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BooleanExpressionParser.StatementContext)
            else:
                return self.getTypedRuleContext(BooleanExpressionParser.StatementContext,i)


        def getRuleIndex(self):
            return BooleanExpressionParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = BooleanExpressionParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34498) != 0):
                self.state = 10
                self.statement()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(BooleanExpressionParser.DeclarationContext,0)


        def expression(self):
            return self.getTypedRuleContext(BooleanExpressionParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BooleanExpressionParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = BooleanExpressionParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 18
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                self.declaration()
                pass
            elif token in [6, 7, 9, 10, 15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 17
                self.expression(0)
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


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BooleanExpressionParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(BooleanExpressionParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BooleanExpressionParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = BooleanExpressionParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.match(BooleanExpressionParser.T__0)
            self.state = 21
            self.match(BooleanExpressionParser.ID)
            self.state = 22
            self.match(BooleanExpressionParser.T__1)
            self.state = 23
            self.expression(0)
            self.state = 24
            self.match(BooleanExpressionParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BooleanExpressionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BooleanExpressionParser.ExpressionContext,i)


        def ID(self):
            return self.getToken(BooleanExpressionParser.ID, 0)

        def comparisonOp(self):
            return self.getTypedRuleContext(BooleanExpressionParser.ComparisonOpContext,0)


        def getRuleIndex(self):
            return BooleanExpressionParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BooleanExpressionParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.state = 27
                self.match(BooleanExpressionParser.T__5)
                self.state = 28
                self.expression(6)
                pass
            elif token in [7]:
                self.state = 29
                self.match(BooleanExpressionParser.T__6)
                self.state = 30
                self.expression(0)
                self.state = 31
                self.match(BooleanExpressionParser.T__7)
                pass
            elif token in [15]:
                self.state = 33
                self.match(BooleanExpressionParser.ID)
                pass
            elif token in [9]:
                self.state = 34
                self.match(BooleanExpressionParser.T__8)
                pass
            elif token in [10]:
                self.state = 35
                self.match(BooleanExpressionParser.T__9)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 50
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 48
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = BooleanExpressionParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 38
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 39
                        self.match(BooleanExpressionParser.T__3)
                        self.state = 40
                        self.expression(9)
                        pass

                    elif la_ == 2:
                        localctx = BooleanExpressionParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 41
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 42
                        self.match(BooleanExpressionParser.T__4)
                        self.state = 43
                        self.expression(8)
                        pass

                    elif la_ == 3:
                        localctx = BooleanExpressionParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 44
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 45
                        self.comparisonOp()
                        self.state = 46
                        self.expression(6)
                        pass

             
                self.state = 52
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ComparisonOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BooleanExpressionParser.RULE_comparisonOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonOp" ):
                listener.enterComparisonOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonOp" ):
                listener.exitComparisonOp(self)




    def comparisonOp(self):

        localctx = BooleanExpressionParser.ComparisonOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_comparisonOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30720) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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
        self._predicates[3] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         




