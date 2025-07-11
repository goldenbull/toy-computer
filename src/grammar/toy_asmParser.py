# Generated from toy_asm.g4 by ANTLR 4.13.2
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
        4,1,43,270,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,1,0,4,0,53,8,0,
        11,0,12,0,54,1,1,4,1,58,8,1,11,1,12,1,59,1,2,3,2,63,8,2,1,2,1,2,
        1,2,1,3,1,3,1,3,3,3,71,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,89,8,4,1,5,3,5,92,8,5,1,5,1,5,1,5,
        3,5,97,8,5,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,3,8,107,8,8,1,8,1,8,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,136,8,9,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,153,
        8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,3,11,170,8,11,1,12,1,12,1,12,1,12,1,12,1,12,3,12,
        178,8,12,1,13,1,13,1,13,1,13,1,13,1,13,3,13,186,8,13,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,
        14,203,8,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,3,15,219,8,15,1,16,1,16,1,16,1,17,1,17,1,18,1,
        18,1,18,1,18,1,18,1,18,3,18,232,8,18,1,19,1,19,1,19,1,19,3,19,238,
        8,19,1,20,1,20,1,20,1,20,3,20,244,8,20,1,21,1,21,1,21,1,21,1,21,
        1,21,3,21,252,8,21,1,22,1,22,1,22,1,22,3,22,258,8,22,1,23,1,23,1,
        23,1,23,1,23,1,23,3,23,266,8,23,1,24,1,24,1,24,0,0,25,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,0,2,
        1,0,5,10,1,0,3,4,297,0,52,1,0,0,0,2,57,1,0,0,0,4,62,1,0,0,0,6,67,
        1,0,0,0,8,88,1,0,0,0,10,96,1,0,0,0,12,98,1,0,0,0,14,100,1,0,0,0,
        16,103,1,0,0,0,18,135,1,0,0,0,20,152,1,0,0,0,22,169,1,0,0,0,24,177,
        1,0,0,0,26,185,1,0,0,0,28,202,1,0,0,0,30,218,1,0,0,0,32,220,1,0,
        0,0,34,223,1,0,0,0,36,231,1,0,0,0,38,237,1,0,0,0,40,243,1,0,0,0,
        42,251,1,0,0,0,44,257,1,0,0,0,46,265,1,0,0,0,48,267,1,0,0,0,50,53,
        3,2,1,0,51,53,3,4,2,0,52,50,1,0,0,0,52,51,1,0,0,0,53,54,1,0,0,0,
        54,52,1,0,0,0,54,55,1,0,0,0,55,1,1,0,0,0,56,58,5,40,0,0,57,56,1,
        0,0,0,58,59,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,3,1,0,0,0,61,
        63,3,6,3,0,62,61,1,0,0,0,62,63,1,0,0,0,63,64,1,0,0,0,64,65,3,8,4,
        0,65,66,5,1,0,0,66,5,1,0,0,0,67,68,5,42,0,0,68,70,5,2,0,0,69,71,
        5,1,0,0,70,69,1,0,0,0,70,71,1,0,0,0,71,7,1,0,0,0,72,89,3,18,9,0,
        73,89,3,20,10,0,74,89,3,22,11,0,75,89,3,24,12,0,76,89,3,26,13,0,
        77,89,3,28,14,0,78,89,3,30,15,0,79,89,3,32,16,0,80,89,3,34,17,0,
        81,89,3,36,18,0,82,89,3,38,19,0,83,89,3,40,20,0,84,89,3,42,21,0,
        85,89,3,44,22,0,86,89,3,46,23,0,87,89,3,48,24,0,88,72,1,0,0,0,88,
        73,1,0,0,0,88,74,1,0,0,0,88,75,1,0,0,0,88,76,1,0,0,0,88,77,1,0,0,
        0,88,78,1,0,0,0,88,79,1,0,0,0,88,80,1,0,0,0,88,81,1,0,0,0,88,82,
        1,0,0,0,88,83,1,0,0,0,88,84,1,0,0,0,88,85,1,0,0,0,88,86,1,0,0,0,
        88,87,1,0,0,0,89,9,1,0,0,0,90,92,5,3,0,0,91,90,1,0,0,0,91,92,1,0,
        0,0,92,93,1,0,0,0,93,97,5,41,0,0,94,95,5,4,0,0,95,97,5,41,0,0,96,
        91,1,0,0,0,96,94,1,0,0,0,97,11,1,0,0,0,98,99,7,0,0,0,99,13,1,0,0,
        0,100,101,7,1,0,0,101,102,5,41,0,0,102,15,1,0,0,0,103,104,5,11,0,
        0,104,106,3,12,6,0,105,107,3,14,7,0,106,105,1,0,0,0,106,107,1,0,
        0,0,107,108,1,0,0,0,108,109,5,12,0,0,109,17,1,0,0,0,110,111,5,13,
        0,0,111,112,3,12,6,0,112,113,5,14,0,0,113,114,3,10,5,0,114,136,1,
        0,0,0,115,116,5,13,0,0,116,117,3,12,6,0,117,118,5,14,0,0,118,119,
        3,12,6,0,119,136,1,0,0,0,120,121,5,13,0,0,121,122,3,12,6,0,122,123,
        5,14,0,0,123,124,3,16,8,0,124,136,1,0,0,0,125,126,5,13,0,0,126,127,
        3,16,8,0,127,128,5,14,0,0,128,129,3,10,5,0,129,136,1,0,0,0,130,131,
        5,13,0,0,131,132,3,16,8,0,132,133,5,14,0,0,133,134,3,12,6,0,134,
        136,1,0,0,0,135,110,1,0,0,0,135,115,1,0,0,0,135,120,1,0,0,0,135,
        125,1,0,0,0,135,130,1,0,0,0,136,19,1,0,0,0,137,138,5,15,0,0,138,
        139,3,12,6,0,139,140,5,14,0,0,140,141,3,10,5,0,141,153,1,0,0,0,142,
        143,5,15,0,0,143,144,3,12,6,0,144,145,5,14,0,0,145,146,3,12,6,0,
        146,153,1,0,0,0,147,148,5,15,0,0,148,149,3,12,6,0,149,150,5,14,0,
        0,150,151,3,16,8,0,151,153,1,0,0,0,152,137,1,0,0,0,152,142,1,0,0,
        0,152,147,1,0,0,0,153,21,1,0,0,0,154,155,5,16,0,0,155,156,3,12,6,
        0,156,157,5,14,0,0,157,158,3,10,5,0,158,170,1,0,0,0,159,160,5,16,
        0,0,160,161,3,12,6,0,161,162,5,14,0,0,162,163,3,12,6,0,163,170,1,
        0,0,0,164,165,5,16,0,0,165,166,3,12,6,0,166,167,5,14,0,0,167,168,
        3,16,8,0,168,170,1,0,0,0,169,154,1,0,0,0,169,159,1,0,0,0,169,164,
        1,0,0,0,170,23,1,0,0,0,171,172,5,17,0,0,172,178,3,10,5,0,173,174,
        5,17,0,0,174,178,3,12,6,0,175,176,5,17,0,0,176,178,3,16,8,0,177,
        171,1,0,0,0,177,173,1,0,0,0,177,175,1,0,0,0,178,25,1,0,0,0,179,180,
        5,18,0,0,180,186,3,10,5,0,181,182,5,18,0,0,182,186,3,12,6,0,183,
        184,5,18,0,0,184,186,3,16,8,0,185,179,1,0,0,0,185,181,1,0,0,0,185,
        183,1,0,0,0,186,27,1,0,0,0,187,188,5,19,0,0,188,189,3,12,6,0,189,
        190,5,14,0,0,190,191,3,10,5,0,191,203,1,0,0,0,192,193,5,19,0,0,193,
        194,3,12,6,0,194,195,5,14,0,0,195,196,3,12,6,0,196,203,1,0,0,0,197,
        198,5,19,0,0,198,199,3,12,6,0,199,200,5,14,0,0,200,201,3,16,8,0,
        201,203,1,0,0,0,202,187,1,0,0,0,202,192,1,0,0,0,202,197,1,0,0,0,
        203,29,1,0,0,0,204,205,5,20,0,0,205,219,5,42,0,0,206,207,5,21,0,
        0,207,219,5,42,0,0,208,209,5,22,0,0,209,219,5,42,0,0,210,211,5,23,
        0,0,211,219,5,42,0,0,212,213,5,24,0,0,213,219,5,42,0,0,214,215,5,
        25,0,0,215,219,5,42,0,0,216,217,5,26,0,0,217,219,5,42,0,0,218,204,
        1,0,0,0,218,206,1,0,0,0,218,208,1,0,0,0,218,210,1,0,0,0,218,212,
        1,0,0,0,218,214,1,0,0,0,218,216,1,0,0,0,219,31,1,0,0,0,220,221,5,
        27,0,0,221,222,5,42,0,0,222,33,1,0,0,0,223,224,5,28,0,0,224,35,1,
        0,0,0,225,226,5,29,0,0,226,232,3,10,5,0,227,228,5,29,0,0,228,232,
        3,12,6,0,229,232,5,30,0,0,230,232,5,31,0,0,231,225,1,0,0,0,231,227,
        1,0,0,0,231,229,1,0,0,0,231,230,1,0,0,0,232,37,1,0,0,0,233,234,5,
        32,0,0,234,238,3,12,6,0,235,238,5,33,0,0,236,238,5,34,0,0,237,233,
        1,0,0,0,237,235,1,0,0,0,237,236,1,0,0,0,238,39,1,0,0,0,239,240,5,
        35,0,0,240,244,3,12,6,0,241,242,5,35,0,0,242,244,3,16,8,0,243,239,
        1,0,0,0,243,241,1,0,0,0,244,41,1,0,0,0,245,246,5,36,0,0,246,252,
        3,10,5,0,247,248,5,36,0,0,248,252,3,12,6,0,249,250,5,36,0,0,250,
        252,3,16,8,0,251,245,1,0,0,0,251,247,1,0,0,0,251,249,1,0,0,0,252,
        43,1,0,0,0,253,254,5,37,0,0,254,258,3,12,6,0,255,256,5,37,0,0,256,
        258,3,16,8,0,257,253,1,0,0,0,257,255,1,0,0,0,258,45,1,0,0,0,259,
        266,5,38,0,0,260,261,5,38,0,0,261,262,3,12,6,0,262,263,5,14,0,0,
        263,264,5,41,0,0,264,266,1,0,0,0,265,259,1,0,0,0,265,260,1,0,0,0,
        266,47,1,0,0,0,267,268,5,39,0,0,268,49,1,0,0,0,22,52,54,59,62,70,
        88,91,96,106,135,152,169,177,185,202,218,231,237,243,251,257,265
    ]

class toy_asmParser ( Parser ):

    grammarFileName = "toy_asm.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\n'", "':'", "'+'", "'-'", "'ax'", 
                     "'bx'", "'cx'", "'dx'", "'bp'", "'sp'", "'['", "']'", 
                     "'mov'", "','", "'add'", "'sub'", "'mul'", "'div'", 
                     "'cmp'", "'jmp'", "'je'", "'jne'", "'jg'", "'jge'", 
                     "'jl'", "'jle'", "'call'", "'ret'", "'push'", "'pushf'", 
                     "'pusha'", "'pop'", "'popf'", "'popa'", "'input'", 
                     "'print'", "'rand'", "'dump'", "'pause'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "Comment", "INT", "Label", "WS" ]

    RULE_program = 0
    RULE_comment = 1
    RULE_oneLineCode = 2
    RULE_opLabel = 3
    RULE_oneOp = 4
    RULE_num = 5
    RULE_reg = 6
    RULE_offset = 7
    RULE_mem = 8
    RULE_move = 9
    RULE_add = 10
    RULE_sub = 11
    RULE_mul = 12
    RULE_div = 13
    RULE_cmp = 14
    RULE_jump = 15
    RULE_call = 16
    RULE_ret = 17
    RULE_push_op = 18
    RULE_pop_op = 19
    RULE_input = 20
    RULE_print = 21
    RULE_rand = 22
    RULE_dump = 23
    RULE_pause = 24

    ruleNames =  [ "program", "comment", "oneLineCode", "opLabel", "oneOp", 
                   "num", "reg", "offset", "mem", "move", "add", "sub", 
                   "mul", "div", "cmp", "jump", "call", "ret", "push_op", 
                   "pop_op", "input", "print", "rand", "dump", "pause" ]

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
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    Comment=40
    INT=41
    Label=42
    WS=43

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

        def comment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(toy_asmParser.CommentContext)
            else:
                return self.getTypedRuleContext(toy_asmParser.CommentContext,i)


        def oneLineCode(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(toy_asmParser.OneLineCodeContext)
            else:
                return self.getTypedRuleContext(toy_asmParser.OneLineCodeContext,i)


        def getRuleIndex(self):
            return toy_asmParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = toy_asmParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 52
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [40]:
                    self.state = 50
                    self.comment()
                    pass
                elif token in [13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 42]:
                    self.state = 51
                    self.oneLineCode()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 54 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 6597069742080) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Comment(self, i:int=None):
            if i is None:
                return self.getTokens(toy_asmParser.Comment)
            else:
                return self.getToken(toy_asmParser.Comment, i)

        def getRuleIndex(self):
            return toy_asmParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComment" ):
                return visitor.visitComment(self)
            else:
                return visitor.visitChildren(self)




    def comment(self):

        localctx = toy_asmParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 56
                    self.match(toy_asmParser.Comment)

                else:
                    raise NoViableAltException(self)
                self.state = 59 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OneLineCodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def oneOp(self):
            return self.getTypedRuleContext(toy_asmParser.OneOpContext,0)


        def opLabel(self):
            return self.getTypedRuleContext(toy_asmParser.OpLabelContext,0)


        def getRuleIndex(self):
            return toy_asmParser.RULE_oneLineCode

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOneLineCode" ):
                listener.enterOneLineCode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOneLineCode" ):
                listener.exitOneLineCode(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOneLineCode" ):
                return visitor.visitOneLineCode(self)
            else:
                return visitor.visitChildren(self)




    def oneLineCode(self):

        localctx = toy_asmParser.OneLineCodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_oneLineCode)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 61
                self.opLabel()


            self.state = 64
            self.oneOp()
            self.state = 65
            self.match(toy_asmParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpLabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Label(self):
            return self.getToken(toy_asmParser.Label, 0)

        def getRuleIndex(self):
            return toy_asmParser.RULE_opLabel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpLabel" ):
                listener.enterOpLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpLabel" ):
                listener.exitOpLabel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpLabel" ):
                return visitor.visitOpLabel(self)
            else:
                return visitor.visitChildren(self)




    def opLabel(self):

        localctx = toy_asmParser.OpLabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_opLabel)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(toy_asmParser.Label)
            self.state = 68
            self.match(toy_asmParser.T__1)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 69
                self.match(toy_asmParser.T__0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OneOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def move(self):
            return self.getTypedRuleContext(toy_asmParser.MoveContext,0)


        def add(self):
            return self.getTypedRuleContext(toy_asmParser.AddContext,0)


        def sub(self):
            return self.getTypedRuleContext(toy_asmParser.SubContext,0)


        def mul(self):
            return self.getTypedRuleContext(toy_asmParser.MulContext,0)


        def div(self):
            return self.getTypedRuleContext(toy_asmParser.DivContext,0)


        def cmp(self):
            return self.getTypedRuleContext(toy_asmParser.CmpContext,0)


        def jump(self):
            return self.getTypedRuleContext(toy_asmParser.JumpContext,0)


        def call(self):
            return self.getTypedRuleContext(toy_asmParser.CallContext,0)


        def ret(self):
            return self.getTypedRuleContext(toy_asmParser.RetContext,0)


        def push_op(self):
            return self.getTypedRuleContext(toy_asmParser.Push_opContext,0)


        def pop_op(self):
            return self.getTypedRuleContext(toy_asmParser.Pop_opContext,0)


        def input_(self):
            return self.getTypedRuleContext(toy_asmParser.InputContext,0)


        def print_(self):
            return self.getTypedRuleContext(toy_asmParser.PrintContext,0)


        def rand(self):
            return self.getTypedRuleContext(toy_asmParser.RandContext,0)


        def dump(self):
            return self.getTypedRuleContext(toy_asmParser.DumpContext,0)


        def pause(self):
            return self.getTypedRuleContext(toy_asmParser.PauseContext,0)


        def getRuleIndex(self):
            return toy_asmParser.RULE_oneOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOneOp" ):
                listener.enterOneOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOneOp" ):
                listener.exitOneOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOneOp" ):
                return visitor.visitOneOp(self)
            else:
                return visitor.visitChildren(self)




    def oneOp(self):

        localctx = toy_asmParser.OneOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_oneOp)
        try:
            self.state = 88
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.move()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.add()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 74
                self.sub()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 4)
                self.state = 75
                self.mul()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 5)
                self.state = 76
                self.div()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 6)
                self.state = 77
                self.cmp()
                pass
            elif token in [20, 21, 22, 23, 24, 25, 26]:
                self.enterOuterAlt(localctx, 7)
                self.state = 78
                self.jump()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 8)
                self.state = 79
                self.call()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 9)
                self.state = 80
                self.ret()
                pass
            elif token in [29, 30, 31]:
                self.enterOuterAlt(localctx, 10)
                self.state = 81
                self.push_op()
                pass
            elif token in [32, 33, 34]:
                self.enterOuterAlt(localctx, 11)
                self.state = 82
                self.pop_op()
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 12)
                self.state = 83
                self.input_()
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 13)
                self.state = 84
                self.print_()
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 14)
                self.state = 85
                self.rand()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 15)
                self.state = 86
                self.dump()
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 16)
                self.state = 87
                self.pause()
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


    class NumContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(toy_asmParser.INT, 0)

        def getRuleIndex(self):
            return toy_asmParser.RULE_num

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNum" ):
                listener.enterNum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNum" ):
                listener.exitNum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum" ):
                return visitor.visitNum(self)
            else:
                return visitor.visitChildren(self)




    def num(self):

        localctx = toy_asmParser.NumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_num)
        self._la = 0 # Token type
        try:
            self.state = 96
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==3:
                    self.state = 90
                    self.match(toy_asmParser.T__2)


                self.state = 93
                self.match(toy_asmParser.INT)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.match(toy_asmParser.T__3)
                self.state = 95
                self.match(toy_asmParser.INT)
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


    class RegContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return toy_asmParser.RULE_reg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReg" ):
                listener.enterReg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReg" ):
                listener.exitReg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReg" ):
                return visitor.visitReg(self)
            else:
                return visitor.visitChildren(self)




    def reg(self):

        localctx = toy_asmParser.RegContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_reg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2016) != 0)):
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


    class OffsetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(toy_asmParser.INT, 0)

        def getRuleIndex(self):
            return toy_asmParser.RULE_offset

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOffset" ):
                listener.enterOffset(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOffset" ):
                listener.exitOffset(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOffset" ):
                return visitor.visitOffset(self)
            else:
                return visitor.visitChildren(self)




    def offset(self):

        localctx = toy_asmParser.OffsetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_offset)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            _la = self._input.LA(1)
            if not(_la==3 or _la==4):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 101
            self.match(toy_asmParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def reg(self):
            return self.getTypedRuleContext(toy_asmParser.RegContext,0)


        def offset(self):
            return self.getTypedRuleContext(toy_asmParser.OffsetContext,0)


        def getRuleIndex(self):
            return toy_asmParser.RULE_mem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMem" ):
                listener.enterMem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMem" ):
                listener.exitMem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMem" ):
                return visitor.visitMem(self)
            else:
                return visitor.visitChildren(self)




    def mem(self):

        localctx = toy_asmParser.MemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_mem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(toy_asmParser.T__10)
            self.state = 104
            self.reg()
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3 or _la==4:
                self.state = 105
                self.offset()


            self.state = 108
            self.match(toy_asmParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MoveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def reg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(toy_asmParser.RegContext)
            else:
                return self.getTypedRuleContext(toy_asmParser.RegContext,i)


        def num(self):
            return self.getTypedRuleContext(toy_asmParser.NumContext,0)


        def mem(self):
            return self.getTypedRuleContext(toy_asmParser.MemContext,0)


        def getRuleIndex(self):
            return toy_asmParser.RULE_move

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMove" ):
                listener.enterMove(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMove" ):
                listener.exitMove(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMove" ):
                return visitor.visitMove(self)
            else:
                return visitor.visitChildren(self)




    def move(self):

        localctx = toy_asmParser.MoveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_move)
        try:
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.match(toy_asmParser.T__12)
                self.state = 111
                self.reg()
                self.state = 112
                self.match(toy_asmParser.T__13)
                self.state = 113
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 115
                self.match(toy_asmParser.T__12)
                self.state = 116
                self.reg()
                self.state = 117
                self.match(toy_asmParser.T__13)
                self.state = 118
                self.reg()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 120
                self.match(toy_asmParser.T__12)
                self.state = 121
                self.reg()
                self.state = 122
                self.match(toy_asmParser.T__13)
                self.state = 123
                self.mem()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 125
                self.match(toy_asmParser.T__12)
                self.state = 126
                self.mem()
                self.state = 127
                self.match(toy_asmParser.T__13)
                self.state = 128
                self.num()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 130
                self.match(toy_asmParser.T__12)
                self.state = 131
                self.mem()
                self.state = 132
                self.match(toy_asmParser.T__13)
                self.state = 133
                self.reg()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def reg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(toy_asmParser.RegContext)
            else:
                return self.getTypedRuleContext(toy_asmParser.RegContext,i)


        def num(self):
            return self.getTypedRuleContext(toy_asmParser.NumContext,0)


        def mem(self):
            return self.getTypedRuleContext(toy_asmParser.MemContext,0)


        def getRuleIndex(self):
            return toy_asmParser.RULE_add

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)




    def add(self):

        localctx = toy_asmParser.AddContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_add)
        try:
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.match(toy_asmParser.T__14)
                self.state = 138
                self.reg()
                self.state = 139
                self.match(toy_asmParser.T__13)
                self.state = 140
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.match(toy_asmParser.T__14)
                self.state = 143
                self.reg()
                self.state = 144
                self.match(toy_asmParser.T__13)
                self.state = 145
                self.reg()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 147
                self.match(toy_asmParser.T__14)
                self.state = 148
                self.reg()
                self.state = 149
                self.match(toy_asmParser.T__13)
                self.state = 150
                self.mem()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def reg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(toy_asmParser.RegContext)
            else:
                return self.getTypedRuleContext(toy_asmParser.RegContext,i)


        def num(self):
            return self.getTypedRuleContext(toy_asmParser.NumContext,0)


        def mem(self):
            return self.getTypedRuleContext(toy_asmParser.MemContext,0)


        def getRuleIndex(self):
            return toy_asmParser.RULE_sub

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSub" ):
                listener.enterSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSub" ):
                listener.exitSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSub" ):
                return visitor.visitSub(self)
            else:
                return visitor.visitChildren(self)




    def sub(self):

        localctx = toy_asmParser.SubContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_sub)
        try:
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.match(toy_asmParser.T__15)
                self.state = 155
                self.reg()
                self.state = 156
                self.match(toy_asmParser.T__13)
                self.state = 157
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.match(toy_asmParser.T__15)
                self.state = 160
                self.reg()
                self.state = 161
                self.match(toy_asmParser.T__13)
                self.state = 162
                self.reg()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 164
                self.match(toy_asmParser.T__15)
                self.state = 165
                self.reg()
                self.state = 166
                self.match(toy_asmParser.T__13)
                self.state = 167
                self.mem()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MulContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def num(self):
            return self.getTypedRuleContext(toy_asmParser.NumContext,0)


        def reg(self):
            return self.getTypedRuleContext(toy_asmParser.RegContext,0)


        def mem(self):
            return self.getTypedRuleContext(toy_asmParser.MemContext,0)


        def getRuleIndex(self):
            return toy_asmParser.RULE_mul

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMul" ):
                listener.enterMul(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMul" ):
                listener.exitMul(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul" ):
                return visitor.visitMul(self)
            else:
                return visitor.visitChildren(self)




    def mul(self):

        localctx = toy_asmParser.MulContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_mul)
        try:
            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.match(toy_asmParser.T__16)
                self.state = 172
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.match(toy_asmParser.T__16)
                self.state = 174
                self.reg()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 175
                self.match(toy_asmParser.T__16)
                self.state = 176
                self.mem()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DivContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def num(self):
            return self.getTypedRuleContext(toy_asmParser.NumContext,0)


        def reg(self):
            return self.getTypedRuleContext(toy_asmParser.RegContext,0)


        def mem(self):
            return self.getTypedRuleContext(toy_asmParser.MemContext,0)


        def getRuleIndex(self):
            return toy_asmParser.RULE_div

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiv" ):
                listener.enterDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiv" ):
                listener.exitDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDiv" ):
                return visitor.visitDiv(self)
            else:
                return visitor.visitChildren(self)




    def div(self):

        localctx = toy_asmParser.DivContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_div)
        try:
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.match(toy_asmParser.T__17)
                self.state = 180
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.match(toy_asmParser.T__17)
                self.state = 182
                self.reg()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 183
                self.match(toy_asmParser.T__17)
                self.state = 184
                self.mem()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def reg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(toy_asmParser.RegContext)
            else:
                return self.getTypedRuleContext(toy_asmParser.RegContext,i)


        def num(self):
            return self.getTypedRuleContext(toy_asmParser.NumContext,0)


        def mem(self):
            return self.getTypedRuleContext(toy_asmParser.MemContext,0)


        def getRuleIndex(self):
            return toy_asmParser.RULE_cmp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmp" ):
                listener.enterCmp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmp" ):
                listener.exitCmp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmp" ):
                return visitor.visitCmp(self)
            else:
                return visitor.visitChildren(self)




    def cmp(self):

        localctx = toy_asmParser.CmpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_cmp)
        try:
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.match(toy_asmParser.T__18)
                self.state = 188
                self.reg()
                self.state = 189
                self.match(toy_asmParser.T__13)
                self.state = 190
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.match(toy_asmParser.T__18)
                self.state = 193
                self.reg()
                self.state = 194
                self.match(toy_asmParser.T__13)
                self.state = 195
                self.reg()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 197
                self.match(toy_asmParser.T__18)
                self.state = 198
                self.reg()
                self.state = 199
                self.match(toy_asmParser.T__13)
                self.state = 200
                self.mem()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JumpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Label(self):
            return self.getToken(toy_asmParser.Label, 0)

        def getRuleIndex(self):
            return toy_asmParser.RULE_jump

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJump" ):
                listener.enterJump(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJump" ):
                listener.exitJump(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJump" ):
                return visitor.visitJump(self)
            else:
                return visitor.visitChildren(self)




    def jump(self):

        localctx = toy_asmParser.JumpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_jump)
        try:
            self.state = 218
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.match(toy_asmParser.T__19)
                self.state = 205
                self.match(toy_asmParser.Label)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                self.match(toy_asmParser.T__20)
                self.state = 207
                self.match(toy_asmParser.Label)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 208
                self.match(toy_asmParser.T__21)
                self.state = 209
                self.match(toy_asmParser.Label)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 4)
                self.state = 210
                self.match(toy_asmParser.T__22)
                self.state = 211
                self.match(toy_asmParser.Label)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 5)
                self.state = 212
                self.match(toy_asmParser.T__23)
                self.state = 213
                self.match(toy_asmParser.Label)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 6)
                self.state = 214
                self.match(toy_asmParser.T__24)
                self.state = 215
                self.match(toy_asmParser.Label)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 7)
                self.state = 216
                self.match(toy_asmParser.T__25)
                self.state = 217
                self.match(toy_asmParser.Label)
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


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Label(self):
            return self.getToken(toy_asmParser.Label, 0)

        def getRuleIndex(self):
            return toy_asmParser.RULE_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = toy_asmParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(toy_asmParser.T__26)
            self.state = 221
            self.match(toy_asmParser.Label)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return toy_asmParser.RULE_ret

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRet" ):
                listener.enterRet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRet" ):
                listener.exitRet(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRet" ):
                return visitor.visitRet(self)
            else:
                return visitor.visitChildren(self)




    def ret(self):

        localctx = toy_asmParser.RetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_ret)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(toy_asmParser.T__27)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Push_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def num(self):
            return self.getTypedRuleContext(toy_asmParser.NumContext,0)


        def reg(self):
            return self.getTypedRuleContext(toy_asmParser.RegContext,0)


        def getRuleIndex(self):
            return toy_asmParser.RULE_push_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPush_op" ):
                listener.enterPush_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPush_op" ):
                listener.exitPush_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPush_op" ):
                return visitor.visitPush_op(self)
            else:
                return visitor.visitChildren(self)




    def push_op(self):

        localctx = toy_asmParser.Push_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_push_op)
        try:
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.match(toy_asmParser.T__28)
                self.state = 226
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
                self.match(toy_asmParser.T__28)
                self.state = 228
                self.reg()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 229
                self.match(toy_asmParser.T__29)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 230
                self.match(toy_asmParser.T__30)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pop_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def reg(self):
            return self.getTypedRuleContext(toy_asmParser.RegContext,0)


        def getRuleIndex(self):
            return toy_asmParser.RULE_pop_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPop_op" ):
                listener.enterPop_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPop_op" ):
                listener.exitPop_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPop_op" ):
                return visitor.visitPop_op(self)
            else:
                return visitor.visitChildren(self)




    def pop_op(self):

        localctx = toy_asmParser.Pop_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_pop_op)
        try:
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.match(toy_asmParser.T__31)
                self.state = 234
                self.reg()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.match(toy_asmParser.T__32)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 3)
                self.state = 236
                self.match(toy_asmParser.T__33)
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


    class InputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def reg(self):
            return self.getTypedRuleContext(toy_asmParser.RegContext,0)


        def mem(self):
            return self.getTypedRuleContext(toy_asmParser.MemContext,0)


        def getRuleIndex(self):
            return toy_asmParser.RULE_input

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInput" ):
                listener.enterInput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInput" ):
                listener.exitInput(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInput" ):
                return visitor.visitInput(self)
            else:
                return visitor.visitChildren(self)




    def input_(self):

        localctx = toy_asmParser.InputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_input)
        try:
            self.state = 243
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.match(toy_asmParser.T__34)
                self.state = 240
                self.reg()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
                self.match(toy_asmParser.T__34)
                self.state = 242
                self.mem()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def num(self):
            return self.getTypedRuleContext(toy_asmParser.NumContext,0)


        def reg(self):
            return self.getTypedRuleContext(toy_asmParser.RegContext,0)


        def mem(self):
            return self.getTypedRuleContext(toy_asmParser.MemContext,0)


        def getRuleIndex(self):
            return toy_asmParser.RULE_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)




    def print_(self):

        localctx = toy_asmParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_print)
        try:
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.match(toy_asmParser.T__35)
                self.state = 246
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.match(toy_asmParser.T__35)
                self.state = 248
                self.reg()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 249
                self.match(toy_asmParser.T__35)
                self.state = 250
                self.mem()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def reg(self):
            return self.getTypedRuleContext(toy_asmParser.RegContext,0)


        def mem(self):
            return self.getTypedRuleContext(toy_asmParser.MemContext,0)


        def getRuleIndex(self):
            return toy_asmParser.RULE_rand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRand" ):
                listener.enterRand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRand" ):
                listener.exitRand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRand" ):
                return visitor.visitRand(self)
            else:
                return visitor.visitChildren(self)




    def rand(self):

        localctx = toy_asmParser.RandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_rand)
        try:
            self.state = 257
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.match(toy_asmParser.T__36)
                self.state = 254
                self.reg()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.match(toy_asmParser.T__36)
                self.state = 256
                self.mem()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DumpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def reg(self):
            return self.getTypedRuleContext(toy_asmParser.RegContext,0)


        def INT(self):
            return self.getToken(toy_asmParser.INT, 0)

        def getRuleIndex(self):
            return toy_asmParser.RULE_dump

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDump" ):
                listener.enterDump(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDump" ):
                listener.exitDump(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDump" ):
                return visitor.visitDump(self)
            else:
                return visitor.visitChildren(self)




    def dump(self):

        localctx = toy_asmParser.DumpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_dump)
        try:
            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 259
                self.match(toy_asmParser.T__37)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 260
                self.match(toy_asmParser.T__37)
                self.state = 261
                self.reg()
                self.state = 262
                self.match(toy_asmParser.T__13)
                self.state = 263
                self.match(toy_asmParser.INT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return toy_asmParser.RULE_pause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPause" ):
                listener.enterPause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPause" ):
                listener.exitPause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPause" ):
                return visitor.visitPause(self)
            else:
                return visitor.visitChildren(self)




    def pause(self):

        localctx = toy_asmParser.PauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_pause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(toy_asmParser.T__38)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





