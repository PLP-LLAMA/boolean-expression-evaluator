# Generated from grammar/boolean_expression/BooleanExpression.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,13,82,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,
        1,0,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,6,
        1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,3,9,62,8,9,1,10,1,10,5,10,66,8,10,10,10,12,10,69,9,10,1,11,4,
        11,72,8,11,11,11,12,11,73,1,12,4,12,77,8,12,11,12,12,12,78,1,12,
        1,12,0,0,13,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,
        23,12,25,13,1,0,4,3,0,65,90,95,95,97,122,4,0,48,57,65,90,95,95,97,
        122,1,0,48,57,3,0,9,10,13,13,32,32,85,0,1,1,0,0,0,0,3,1,0,0,0,0,
        5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,
        1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,
        1,0,0,0,1,27,1,0,0,0,3,29,1,0,0,0,5,31,1,0,0,0,7,34,1,0,0,0,9,37,
        1,0,0,0,11,39,1,0,0,0,13,41,1,0,0,0,15,45,1,0,0,0,17,48,1,0,0,0,
        19,61,1,0,0,0,21,63,1,0,0,0,23,71,1,0,0,0,25,76,1,0,0,0,27,28,5,
        60,0,0,28,2,1,0,0,0,29,30,5,62,0,0,30,4,1,0,0,0,31,32,5,61,0,0,32,
        33,5,61,0,0,33,6,1,0,0,0,34,35,5,33,0,0,35,36,5,61,0,0,36,8,1,0,
        0,0,37,38,5,40,0,0,38,10,1,0,0,0,39,40,5,41,0,0,40,12,1,0,0,0,41,
        42,5,65,0,0,42,43,5,78,0,0,43,44,5,68,0,0,44,14,1,0,0,0,45,46,5,
        79,0,0,46,47,5,82,0,0,47,16,1,0,0,0,48,49,5,78,0,0,49,50,5,79,0,
        0,50,51,5,84,0,0,51,18,1,0,0,0,52,53,5,116,0,0,53,54,5,114,0,0,54,
        55,5,117,0,0,55,62,5,101,0,0,56,57,5,102,0,0,57,58,5,97,0,0,58,59,
        5,108,0,0,59,60,5,115,0,0,60,62,5,101,0,0,61,52,1,0,0,0,61,56,1,
        0,0,0,62,20,1,0,0,0,63,67,7,0,0,0,64,66,7,1,0,0,65,64,1,0,0,0,66,
        69,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,22,1,0,0,0,69,67,1,0,0,
        0,70,72,7,2,0,0,71,70,1,0,0,0,72,73,1,0,0,0,73,71,1,0,0,0,73,74,
        1,0,0,0,74,24,1,0,0,0,75,77,7,3,0,0,76,75,1,0,0,0,77,78,1,0,0,0,
        78,76,1,0,0,0,78,79,1,0,0,0,79,80,1,0,0,0,80,81,6,12,0,0,81,26,1,
        0,0,0,5,0,61,67,73,78,1,6,0,0
    ]

class BooleanExpressionLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    AND = 7
    OR = 8
    NOT = 9
    BOOL = 10
    IDENTIFIER = 11
    NUMBER = 12
    WS = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'<'", "'>'", "'=='", "'!='", "'('", "')'", "'AND'", "'OR'", 
            "'NOT'" ]

    symbolicNames = [ "<INVALID>",
            "AND", "OR", "NOT", "BOOL", "IDENTIFIER", "NUMBER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "AND", 
                  "OR", "NOT", "BOOL", "IDENTIFIER", "NUMBER", "WS" ]

    grammarFileName = "BooleanExpression.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


