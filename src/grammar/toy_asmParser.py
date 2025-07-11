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
        4,1,36,250,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,1,0,4,0,53,8,0,
        11,0,12,0,54,1,1,4,1,58,8,1,11,1,12,1,59,1,2,1,2,3,2,64,8,2,1,2,
        1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,3,3,87,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,97,
        8,4,1,5,1,5,1,5,1,6,3,6,103,8,6,1,6,1,6,1,6,3,6,108,8,6,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,3,7,132,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,3,8,146,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,3,9,160,8,9,1,10,1,10,1,10,1,10,1,10,1,10,3,10,168,8,10,
        1,11,1,11,1,11,1,11,1,11,1,11,3,11,176,8,11,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,190,8,12,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,
        206,8,13,1,14,1,14,1,14,1,15,1,15,1,16,1,16,1,16,1,16,3,16,217,8,
        16,1,17,1,17,1,17,1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,1,22,1,
        22,1,22,1,22,3,22,234,8,22,1,23,1,23,1,23,1,23,1,23,1,23,3,23,242,
        8,23,1,24,1,24,1,24,1,24,3,24,248,8,24,1,24,0,0,25,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,0,1,1,0,
        5,6,273,0,52,1,0,0,0,2,57,1,0,0,0,4,63,1,0,0,0,6,86,1,0,0,0,8,96,
        1,0,0,0,10,98,1,0,0,0,12,107,1,0,0,0,14,131,1,0,0,0,16,145,1,0,0,
        0,18,159,1,0,0,0,20,167,1,0,0,0,22,175,1,0,0,0,24,189,1,0,0,0,26,
        205,1,0,0,0,28,207,1,0,0,0,30,210,1,0,0,0,32,216,1,0,0,0,34,218,
        1,0,0,0,36,221,1,0,0,0,38,223,1,0,0,0,40,225,1,0,0,0,42,227,1,0,
        0,0,44,233,1,0,0,0,46,241,1,0,0,0,48,247,1,0,0,0,50,53,3,2,1,0,51,
        53,3,4,2,0,52,50,1,0,0,0,52,51,1,0,0,0,53,54,1,0,0,0,54,52,1,0,0,
        0,54,55,1,0,0,0,55,1,1,0,0,0,56,58,5,32,0,0,57,56,1,0,0,0,58,59,
        1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,3,1,0,0,0,61,62,5,35,0,0,
        62,64,5,1,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,65,1,0,0,0,65,66,3,
        6,3,0,66,67,5,2,0,0,67,5,1,0,0,0,68,87,3,14,7,0,69,87,3,16,8,0,70,
        87,3,18,9,0,71,87,3,20,10,0,72,87,3,22,11,0,73,87,3,24,12,0,74,87,
        3,26,13,0,75,87,3,28,14,0,76,87,3,30,15,0,77,87,3,32,16,0,78,87,
        3,34,17,0,79,87,3,36,18,0,80,87,3,38,19,0,81,87,3,40,20,0,82,87,
        3,42,21,0,83,87,3,44,22,0,84,87,3,46,23,0,85,87,3,48,24,0,86,68,
        1,0,0,0,86,69,1,0,0,0,86,70,1,0,0,0,86,71,1,0,0,0,86,72,1,0,0,0,
        86,73,1,0,0,0,86,74,1,0,0,0,86,75,1,0,0,0,86,76,1,0,0,0,86,77,1,
        0,0,0,86,78,1,0,0,0,86,79,1,0,0,0,86,80,1,0,0,0,86,81,1,0,0,0,86,
        82,1,0,0,0,86,83,1,0,0,0,86,84,1,0,0,0,86,85,1,0,0,0,87,7,1,0,0,
        0,88,89,5,3,0,0,89,90,5,33,0,0,90,97,5,4,0,0,91,92,5,3,0,0,92,93,
        5,33,0,0,93,94,3,10,5,0,94,95,5,4,0,0,95,97,1,0,0,0,96,88,1,0,0,
        0,96,91,1,0,0,0,97,9,1,0,0,0,98,99,7,0,0,0,99,100,5,34,0,0,100,11,
        1,0,0,0,101,103,5,5,0,0,102,101,1,0,0,0,102,103,1,0,0,0,103,104,
        1,0,0,0,104,108,5,34,0,0,105,106,5,6,0,0,106,108,5,34,0,0,107,102,
        1,0,0,0,107,105,1,0,0,0,108,13,1,0,0,0,109,110,5,7,0,0,110,111,5,
        33,0,0,111,112,5,8,0,0,112,132,3,12,6,0,113,114,5,7,0,0,114,115,
        5,33,0,0,115,116,5,8,0,0,116,132,5,33,0,0,117,118,5,7,0,0,118,119,
        5,33,0,0,119,120,5,8,0,0,120,132,3,8,4,0,121,122,5,7,0,0,122,123,
        3,8,4,0,123,124,5,8,0,0,124,125,3,12,6,0,125,132,1,0,0,0,126,127,
        5,7,0,0,127,128,3,8,4,0,128,129,5,8,0,0,129,130,5,33,0,0,130,132,
        1,0,0,0,131,109,1,0,0,0,131,113,1,0,0,0,131,117,1,0,0,0,131,121,
        1,0,0,0,131,126,1,0,0,0,132,15,1,0,0,0,133,134,5,9,0,0,134,135,5,
        33,0,0,135,136,5,8,0,0,136,146,3,12,6,0,137,138,5,9,0,0,138,139,
        5,33,0,0,139,140,5,8,0,0,140,146,5,33,0,0,141,142,5,9,0,0,142,143,
        5,33,0,0,143,144,5,8,0,0,144,146,3,8,4,0,145,133,1,0,0,0,145,137,
        1,0,0,0,145,141,1,0,0,0,146,17,1,0,0,0,147,148,5,10,0,0,148,149,
        5,33,0,0,149,150,5,8,0,0,150,160,3,12,6,0,151,152,5,10,0,0,152,153,
        5,33,0,0,153,154,5,8,0,0,154,160,5,33,0,0,155,156,5,10,0,0,156,157,
        5,33,0,0,157,158,5,8,0,0,158,160,3,8,4,0,159,147,1,0,0,0,159,151,
        1,0,0,0,159,155,1,0,0,0,160,19,1,0,0,0,161,162,5,11,0,0,162,168,
        3,12,6,0,163,164,5,11,0,0,164,168,5,33,0,0,165,166,5,11,0,0,166,
        168,3,8,4,0,167,161,1,0,0,0,167,163,1,0,0,0,167,165,1,0,0,0,168,
        21,1,0,0,0,169,170,5,12,0,0,170,176,3,12,6,0,171,172,5,12,0,0,172,
        176,5,33,0,0,173,174,5,12,0,0,174,176,3,8,4,0,175,169,1,0,0,0,175,
        171,1,0,0,0,175,173,1,0,0,0,176,23,1,0,0,0,177,178,5,13,0,0,178,
        179,5,33,0,0,179,180,5,8,0,0,180,190,3,12,6,0,181,182,5,13,0,0,182,
        183,5,33,0,0,183,184,5,8,0,0,184,190,5,33,0,0,185,186,5,13,0,0,186,
        187,5,33,0,0,187,188,5,8,0,0,188,190,3,8,4,0,189,177,1,0,0,0,189,
        181,1,0,0,0,189,185,1,0,0,0,190,25,1,0,0,0,191,192,5,14,0,0,192,
        206,5,35,0,0,193,194,5,15,0,0,194,206,5,35,0,0,195,196,5,16,0,0,
        196,206,5,35,0,0,197,198,5,17,0,0,198,206,5,35,0,0,199,200,5,18,
        0,0,200,206,5,35,0,0,201,202,5,19,0,0,202,206,5,35,0,0,203,204,5,
        20,0,0,204,206,5,35,0,0,205,191,1,0,0,0,205,193,1,0,0,0,205,195,
        1,0,0,0,205,197,1,0,0,0,205,199,1,0,0,0,205,201,1,0,0,0,205,203,
        1,0,0,0,206,27,1,0,0,0,207,208,5,21,0,0,208,209,5,35,0,0,209,29,
        1,0,0,0,210,211,5,22,0,0,211,31,1,0,0,0,212,213,5,23,0,0,213,217,
        3,12,6,0,214,215,5,23,0,0,215,217,5,33,0,0,216,212,1,0,0,0,216,214,
        1,0,0,0,217,33,1,0,0,0,218,219,5,24,0,0,219,220,5,33,0,0,220,35,
        1,0,0,0,221,222,5,25,0,0,222,37,1,0,0,0,223,224,5,26,0,0,224,39,
        1,0,0,0,225,226,5,27,0,0,226,41,1,0,0,0,227,228,5,28,0,0,228,43,
        1,0,0,0,229,230,5,29,0,0,230,234,5,33,0,0,231,232,5,29,0,0,232,234,
        3,8,4,0,233,229,1,0,0,0,233,231,1,0,0,0,234,45,1,0,0,0,235,236,5,
        30,0,0,236,242,3,12,6,0,237,238,5,30,0,0,238,242,5,33,0,0,239,240,
        5,30,0,0,240,242,3,8,4,0,241,235,1,0,0,0,241,237,1,0,0,0,241,239,
        1,0,0,0,242,47,1,0,0,0,243,244,5,31,0,0,244,248,5,33,0,0,245,246,
        5,31,0,0,246,248,3,8,4,0,247,243,1,0,0,0,247,245,1,0,0,0,248,49,
        1,0,0,0,19,52,54,59,63,86,96,102,107,131,145,159,167,175,189,205,
        216,233,241,247
    ]

class toy_asmParser ( Parser ):

    grammarFileName = "toy_asm.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'\\n'", "'['", "']'", "'+'", "'-'", 
                     "'mov'", "','", "'add'", "'sub'", "'mul'", "'div'", 
                     "'cmp'", "'jmp'", "'je'", "'jne'", "'jg'", "'jge'", 
                     "'jl'", "'jle'", "'call'", "'ret'", "'push'", "'pop'", 
                     "'pushf'", "'popf'", "'pusha'", "'popa'", "'input'", 
                     "'print'", "'rand'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "Comment", "Reg", "INT", "Addr", "WS" ]

    RULE_program = 0
    RULE_comment = 1
    RULE_oneLineCode = 2
    RULE_oneOp = 3
    RULE_mem = 4
    RULE_offset = 5
    RULE_num = 6
    RULE_move = 7
    RULE_add = 8
    RULE_sub = 9
    RULE_mul = 10
    RULE_div = 11
    RULE_cmp = 12
    RULE_jump = 13
    RULE_call = 14
    RULE_ret = 15
    RULE_push = 16
    RULE_pop = 17
    RULE_pushf = 18
    RULE_popf = 19
    RULE_pusha = 20
    RULE_popa = 21
    RULE_input = 22
    RULE_print = 23
    RULE_rand = 24

    ruleNames =  [ "program", "comment", "oneLineCode", "oneOp", "mem", 
                   "offset", "num", "move", "add", "sub", "mul", "div", 
                   "cmp", "jump", "call", "ret", "push", "pop", "pushf", 
                   "popf", "pusha", "popa", "input", "print", "rand" ]

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
    Comment=32
    Reg=33
    INT=34
    Addr=35
    WS=36

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
                if token in [32]:
                    self.state = 50
                    self.comment()
                    pass
                elif token in [7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 35]:
                    self.state = 51
                    self.oneLineCode()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 54 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 42949672576) != 0)):
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


        def Addr(self):
            return self.getToken(toy_asmParser.Addr, 0)

        def getRuleIndex(self):
            return toy_asmParser.RULE_oneLineCode

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOneLineCode" ):
                listener.enterOneLineCode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOneLineCode" ):
                listener.exitOneLineCode(self)




    def oneLineCode(self):

        localctx = toy_asmParser.OneLineCodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_oneLineCode)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 61
                self.match(toy_asmParser.Addr)
                self.state = 62
                self.match(toy_asmParser.T__0)


            self.state = 65
            self.oneOp()
            self.state = 66
            self.match(toy_asmParser.T__1)
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


        def push(self):
            return self.getTypedRuleContext(toy_asmParser.PushContext,0)


        def pop(self):
            return self.getTypedRuleContext(toy_asmParser.PopContext,0)


        def pushf(self):
            return self.getTypedRuleContext(toy_asmParser.PushfContext,0)


        def popf(self):
            return self.getTypedRuleContext(toy_asmParser.PopfContext,0)


        def pusha(self):
            return self.getTypedRuleContext(toy_asmParser.PushaContext,0)


        def popa(self):
            return self.getTypedRuleContext(toy_asmParser.PopaContext,0)


        def input_(self):
            return self.getTypedRuleContext(toy_asmParser.InputContext,0)


        def print_(self):
            return self.getTypedRuleContext(toy_asmParser.PrintContext,0)


        def rand(self):
            return self.getTypedRuleContext(toy_asmParser.RandContext,0)


        def getRuleIndex(self):
            return toy_asmParser.RULE_oneOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOneOp" ):
                listener.enterOneOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOneOp" ):
                listener.exitOneOp(self)




    def oneOp(self):

        localctx = toy_asmParser.OneOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_oneOp)
        try:
            self.state = 86
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.move()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.add()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 70
                self.sub()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 71
                self.mul()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 5)
                self.state = 72
                self.div()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 6)
                self.state = 73
                self.cmp()
                pass
            elif token in [14, 15, 16, 17, 18, 19, 20]:
                self.enterOuterAlt(localctx, 7)
                self.state = 74
                self.jump()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 8)
                self.state = 75
                self.call()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 9)
                self.state = 76
                self.ret()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 10)
                self.state = 77
                self.push()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 11)
                self.state = 78
                self.pop()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 12)
                self.state = 79
                self.pushf()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 13)
                self.state = 80
                self.popf()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 14)
                self.state = 81
                self.pusha()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 15)
                self.state = 82
                self.popa()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 16)
                self.state = 83
                self.input_()
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 17)
                self.state = 84
                self.print_()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 18)
                self.state = 85
                self.rand()
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


    class MemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Reg(self):
            return self.getToken(toy_asmParser.Reg, 0)

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




    def mem(self):

        localctx = toy_asmParser.MemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_mem)
        try:
            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.match(toy_asmParser.T__2)
                self.state = 89
                self.match(toy_asmParser.Reg)
                self.state = 90
                self.match(toy_asmParser.T__3)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.match(toy_asmParser.T__2)
                self.state = 92
                self.match(toy_asmParser.Reg)
                self.state = 93
                self.offset()
                self.state = 94
                self.match(toy_asmParser.T__3)
                pass


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




    def offset(self):

        localctx = toy_asmParser.OffsetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_offset)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            _la = self._input.LA(1)
            if not(_la==5 or _la==6):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 99
            self.match(toy_asmParser.INT)
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




    def num(self):

        localctx = toy_asmParser.NumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_num)
        self._la = 0 # Token type
        try:
            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 101
                    self.match(toy_asmParser.T__4)


                self.state = 104
                self.match(toy_asmParser.INT)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.match(toy_asmParser.T__5)
                self.state = 106
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


    class MoveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Reg(self, i:int=None):
            if i is None:
                return self.getTokens(toy_asmParser.Reg)
            else:
                return self.getToken(toy_asmParser.Reg, i)

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




    def move(self):

        localctx = toy_asmParser.MoveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_move)
        try:
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.match(toy_asmParser.T__6)
                self.state = 110
                self.match(toy_asmParser.Reg)
                self.state = 111
                self.match(toy_asmParser.T__7)
                self.state = 112
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.match(toy_asmParser.T__6)
                self.state = 114
                self.match(toy_asmParser.Reg)
                self.state = 115
                self.match(toy_asmParser.T__7)
                self.state = 116
                self.match(toy_asmParser.Reg)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 117
                self.match(toy_asmParser.T__6)
                self.state = 118
                self.match(toy_asmParser.Reg)
                self.state = 119
                self.match(toy_asmParser.T__7)
                self.state = 120
                self.mem()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 121
                self.match(toy_asmParser.T__6)
                self.state = 122
                self.mem()
                self.state = 123
                self.match(toy_asmParser.T__7)
                self.state = 124
                self.num()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 126
                self.match(toy_asmParser.T__6)
                self.state = 127
                self.mem()
                self.state = 128
                self.match(toy_asmParser.T__7)
                self.state = 129
                self.match(toy_asmParser.Reg)
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

        def Reg(self, i:int=None):
            if i is None:
                return self.getTokens(toy_asmParser.Reg)
            else:
                return self.getToken(toy_asmParser.Reg, i)

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




    def add(self):

        localctx = toy_asmParser.AddContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_add)
        try:
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.match(toy_asmParser.T__8)
                self.state = 134
                self.match(toy_asmParser.Reg)
                self.state = 135
                self.match(toy_asmParser.T__7)
                self.state = 136
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.match(toy_asmParser.T__8)
                self.state = 138
                self.match(toy_asmParser.Reg)
                self.state = 139
                self.match(toy_asmParser.T__7)
                self.state = 140
                self.match(toy_asmParser.Reg)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 141
                self.match(toy_asmParser.T__8)
                self.state = 142
                self.match(toy_asmParser.Reg)
                self.state = 143
                self.match(toy_asmParser.T__7)
                self.state = 144
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

        def Reg(self, i:int=None):
            if i is None:
                return self.getTokens(toy_asmParser.Reg)
            else:
                return self.getToken(toy_asmParser.Reg, i)

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




    def sub(self):

        localctx = toy_asmParser.SubContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_sub)
        try:
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.match(toy_asmParser.T__9)
                self.state = 148
                self.match(toy_asmParser.Reg)
                self.state = 149
                self.match(toy_asmParser.T__7)
                self.state = 150
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.match(toy_asmParser.T__9)
                self.state = 152
                self.match(toy_asmParser.Reg)
                self.state = 153
                self.match(toy_asmParser.T__7)
                self.state = 154
                self.match(toy_asmParser.Reg)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 155
                self.match(toy_asmParser.T__9)
                self.state = 156
                self.match(toy_asmParser.Reg)
                self.state = 157
                self.match(toy_asmParser.T__7)
                self.state = 158
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


        def Reg(self):
            return self.getToken(toy_asmParser.Reg, 0)

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




    def mul(self):

        localctx = toy_asmParser.MulContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_mul)
        try:
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.match(toy_asmParser.T__10)
                self.state = 162
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.match(toy_asmParser.T__10)
                self.state = 164
                self.match(toy_asmParser.Reg)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 165
                self.match(toy_asmParser.T__10)
                self.state = 166
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


        def Reg(self):
            return self.getToken(toy_asmParser.Reg, 0)

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




    def div(self):

        localctx = toy_asmParser.DivContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_div)
        try:
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.match(toy_asmParser.T__11)
                self.state = 170
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
                self.match(toy_asmParser.T__11)
                self.state = 172
                self.match(toy_asmParser.Reg)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 173
                self.match(toy_asmParser.T__11)
                self.state = 174
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

        def Reg(self, i:int=None):
            if i is None:
                return self.getTokens(toy_asmParser.Reg)
            else:
                return self.getToken(toy_asmParser.Reg, i)

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




    def cmp(self):

        localctx = toy_asmParser.CmpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_cmp)
        try:
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.match(toy_asmParser.T__12)
                self.state = 178
                self.match(toy_asmParser.Reg)
                self.state = 179
                self.match(toy_asmParser.T__7)
                self.state = 180
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.match(toy_asmParser.T__12)
                self.state = 182
                self.match(toy_asmParser.Reg)
                self.state = 183
                self.match(toy_asmParser.T__7)
                self.state = 184
                self.match(toy_asmParser.Reg)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 185
                self.match(toy_asmParser.T__12)
                self.state = 186
                self.match(toy_asmParser.Reg)
                self.state = 187
                self.match(toy_asmParser.T__7)
                self.state = 188
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

        def Addr(self):
            return self.getToken(toy_asmParser.Addr, 0)

        def getRuleIndex(self):
            return toy_asmParser.RULE_jump

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJump" ):
                listener.enterJump(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJump" ):
                listener.exitJump(self)




    def jump(self):

        localctx = toy_asmParser.JumpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_jump)
        try:
            self.state = 205
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.match(toy_asmParser.T__13)
                self.state = 192
                self.match(toy_asmParser.Addr)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.match(toy_asmParser.T__14)
                self.state = 194
                self.match(toy_asmParser.Addr)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 195
                self.match(toy_asmParser.T__15)
                self.state = 196
                self.match(toy_asmParser.Addr)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 4)
                self.state = 197
                self.match(toy_asmParser.T__16)
                self.state = 198
                self.match(toy_asmParser.Addr)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 5)
                self.state = 199
                self.match(toy_asmParser.T__17)
                self.state = 200
                self.match(toy_asmParser.Addr)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 6)
                self.state = 201
                self.match(toy_asmParser.T__18)
                self.state = 202
                self.match(toy_asmParser.Addr)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 7)
                self.state = 203
                self.match(toy_asmParser.T__19)
                self.state = 204
                self.match(toy_asmParser.Addr)
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

        def Addr(self):
            return self.getToken(toy_asmParser.Addr, 0)

        def getRuleIndex(self):
            return toy_asmParser.RULE_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)




    def call(self):

        localctx = toy_asmParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(toy_asmParser.T__20)
            self.state = 208
            self.match(toy_asmParser.Addr)
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




    def ret(self):

        localctx = toy_asmParser.RetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_ret)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(toy_asmParser.T__21)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PushContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def num(self):
            return self.getTypedRuleContext(toy_asmParser.NumContext,0)


        def Reg(self):
            return self.getToken(toy_asmParser.Reg, 0)

        def getRuleIndex(self):
            return toy_asmParser.RULE_push

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPush" ):
                listener.enterPush(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPush" ):
                listener.exitPush(self)




    def push(self):

        localctx = toy_asmParser.PushContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_push)
        try:
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.match(toy_asmParser.T__22)
                self.state = 213
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
                self.match(toy_asmParser.T__22)
                self.state = 215
                self.match(toy_asmParser.Reg)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Reg(self):
            return self.getToken(toy_asmParser.Reg, 0)

        def getRuleIndex(self):
            return toy_asmParser.RULE_pop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPop" ):
                listener.enterPop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPop" ):
                listener.exitPop(self)




    def pop(self):

        localctx = toy_asmParser.PopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_pop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(toy_asmParser.T__23)
            self.state = 219
            self.match(toy_asmParser.Reg)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PushfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return toy_asmParser.RULE_pushf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPushf" ):
                listener.enterPushf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPushf" ):
                listener.exitPushf(self)




    def pushf(self):

        localctx = toy_asmParser.PushfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_pushf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(toy_asmParser.T__24)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PopfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return toy_asmParser.RULE_popf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPopf" ):
                listener.enterPopf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPopf" ):
                listener.exitPopf(self)




    def popf(self):

        localctx = toy_asmParser.PopfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_popf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(toy_asmParser.T__25)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PushaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return toy_asmParser.RULE_pusha

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPusha" ):
                listener.enterPusha(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPusha" ):
                listener.exitPusha(self)




    def pusha(self):

        localctx = toy_asmParser.PushaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_pusha)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(toy_asmParser.T__26)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PopaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return toy_asmParser.RULE_popa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPopa" ):
                listener.enterPopa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPopa" ):
                listener.exitPopa(self)




    def popa(self):

        localctx = toy_asmParser.PopaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_popa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(toy_asmParser.T__27)
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

        def Reg(self):
            return self.getToken(toy_asmParser.Reg, 0)

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




    def input_(self):

        localctx = toy_asmParser.InputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_input)
        try:
            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.match(toy_asmParser.T__28)
                self.state = 230
                self.match(toy_asmParser.Reg)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 231
                self.match(toy_asmParser.T__28)
                self.state = 232
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


        def Reg(self):
            return self.getToken(toy_asmParser.Reg, 0)

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




    def print_(self):

        localctx = toy_asmParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_print)
        try:
            self.state = 241
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.match(toy_asmParser.T__29)
                self.state = 236
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.match(toy_asmParser.T__29)
                self.state = 238
                self.match(toy_asmParser.Reg)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 239
                self.match(toy_asmParser.T__29)
                self.state = 240
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

        def Reg(self):
            return self.getToken(toy_asmParser.Reg, 0)

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




    def rand(self):

        localctx = toy_asmParser.RandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_rand)
        try:
            self.state = 247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.match(toy_asmParser.T__30)
                self.state = 244
                self.match(toy_asmParser.Reg)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
                self.match(toy_asmParser.T__30)
                self.state = 246
                self.mem()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





