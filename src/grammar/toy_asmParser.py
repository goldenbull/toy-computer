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
        4,1,43,263,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,1,0,4,0,51,8,0,11,0,12,0,
        52,1,1,3,1,56,8,1,1,1,1,1,1,1,1,2,1,2,1,2,3,2,64,8,2,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,82,8,3,1,
        4,3,4,85,8,4,1,4,1,4,1,4,3,4,90,8,4,1,5,1,5,1,6,1,6,1,6,1,7,1,7,
        1,7,3,7,100,8,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,
        129,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,3,9,146,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,3,10,163,8,10,1,11,1,11,1,11,1,11,1,11,
        1,11,3,11,171,8,11,1,12,1,12,1,12,1,12,1,12,1,12,3,12,179,8,12,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,3,13,196,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,3,14,212,8,14,1,15,1,15,1,15,1,16,1,
        16,1,17,1,17,1,17,1,17,1,17,1,17,3,17,225,8,17,1,18,1,18,1,18,1,
        18,3,18,231,8,18,1,19,1,19,1,19,1,19,3,19,237,8,19,1,20,1,20,1,20,
        1,20,1,20,1,20,3,20,245,8,20,1,21,1,21,1,21,1,21,3,21,251,8,21,1,
        22,1,22,1,22,1,22,1,22,1,22,3,22,259,8,22,1,23,1,23,1,23,0,0,24,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,
        46,0,2,1,0,5,10,1,0,3,4,290,0,50,1,0,0,0,2,55,1,0,0,0,4,60,1,0,0,
        0,6,81,1,0,0,0,8,89,1,0,0,0,10,91,1,0,0,0,12,93,1,0,0,0,14,96,1,
        0,0,0,16,128,1,0,0,0,18,145,1,0,0,0,20,162,1,0,0,0,22,170,1,0,0,
        0,24,178,1,0,0,0,26,195,1,0,0,0,28,211,1,0,0,0,30,213,1,0,0,0,32,
        216,1,0,0,0,34,224,1,0,0,0,36,230,1,0,0,0,38,236,1,0,0,0,40,244,
        1,0,0,0,42,250,1,0,0,0,44,258,1,0,0,0,46,260,1,0,0,0,48,51,5,40,
        0,0,49,51,3,2,1,0,50,48,1,0,0,0,50,49,1,0,0,0,51,52,1,0,0,0,52,50,
        1,0,0,0,52,53,1,0,0,0,53,1,1,0,0,0,54,56,3,4,2,0,55,54,1,0,0,0,55,
        56,1,0,0,0,56,57,1,0,0,0,57,58,3,6,3,0,58,59,5,1,0,0,59,3,1,0,0,
        0,60,61,5,42,0,0,61,63,5,2,0,0,62,64,5,1,0,0,63,62,1,0,0,0,63,64,
        1,0,0,0,64,5,1,0,0,0,65,82,3,16,8,0,66,82,3,18,9,0,67,82,3,20,10,
        0,68,82,3,22,11,0,69,82,3,24,12,0,70,82,3,26,13,0,71,82,3,28,14,
        0,72,82,3,30,15,0,73,82,3,32,16,0,74,82,3,34,17,0,75,82,3,36,18,
        0,76,82,3,38,19,0,77,82,3,40,20,0,78,82,3,42,21,0,79,82,3,44,22,
        0,80,82,3,46,23,0,81,65,1,0,0,0,81,66,1,0,0,0,81,67,1,0,0,0,81,68,
        1,0,0,0,81,69,1,0,0,0,81,70,1,0,0,0,81,71,1,0,0,0,81,72,1,0,0,0,
        81,73,1,0,0,0,81,74,1,0,0,0,81,75,1,0,0,0,81,76,1,0,0,0,81,77,1,
        0,0,0,81,78,1,0,0,0,81,79,1,0,0,0,81,80,1,0,0,0,82,7,1,0,0,0,83,
        85,5,3,0,0,84,83,1,0,0,0,84,85,1,0,0,0,85,86,1,0,0,0,86,90,5,41,
        0,0,87,88,5,4,0,0,88,90,5,41,0,0,89,84,1,0,0,0,89,87,1,0,0,0,90,
        9,1,0,0,0,91,92,7,0,0,0,92,11,1,0,0,0,93,94,7,1,0,0,94,95,5,41,0,
        0,95,13,1,0,0,0,96,97,5,11,0,0,97,99,3,10,5,0,98,100,3,12,6,0,99,
        98,1,0,0,0,99,100,1,0,0,0,100,101,1,0,0,0,101,102,5,12,0,0,102,15,
        1,0,0,0,103,104,5,13,0,0,104,105,3,10,5,0,105,106,5,14,0,0,106,107,
        3,8,4,0,107,129,1,0,0,0,108,109,5,13,0,0,109,110,3,10,5,0,110,111,
        5,14,0,0,111,112,3,10,5,0,112,129,1,0,0,0,113,114,5,13,0,0,114,115,
        3,10,5,0,115,116,5,14,0,0,116,117,3,14,7,0,117,129,1,0,0,0,118,119,
        5,13,0,0,119,120,3,14,7,0,120,121,5,14,0,0,121,122,3,8,4,0,122,129,
        1,0,0,0,123,124,5,13,0,0,124,125,3,14,7,0,125,126,5,14,0,0,126,127,
        3,10,5,0,127,129,1,0,0,0,128,103,1,0,0,0,128,108,1,0,0,0,128,113,
        1,0,0,0,128,118,1,0,0,0,128,123,1,0,0,0,129,17,1,0,0,0,130,131,5,
        15,0,0,131,132,3,10,5,0,132,133,5,14,0,0,133,134,3,8,4,0,134,146,
        1,0,0,0,135,136,5,15,0,0,136,137,3,10,5,0,137,138,5,14,0,0,138,139,
        3,10,5,0,139,146,1,0,0,0,140,141,5,15,0,0,141,142,3,10,5,0,142,143,
        5,14,0,0,143,144,3,14,7,0,144,146,1,0,0,0,145,130,1,0,0,0,145,135,
        1,0,0,0,145,140,1,0,0,0,146,19,1,0,0,0,147,148,5,16,0,0,148,149,
        3,10,5,0,149,150,5,14,0,0,150,151,3,8,4,0,151,163,1,0,0,0,152,153,
        5,16,0,0,153,154,3,10,5,0,154,155,5,14,0,0,155,156,3,10,5,0,156,
        163,1,0,0,0,157,158,5,16,0,0,158,159,3,10,5,0,159,160,5,14,0,0,160,
        161,3,14,7,0,161,163,1,0,0,0,162,147,1,0,0,0,162,152,1,0,0,0,162,
        157,1,0,0,0,163,21,1,0,0,0,164,165,5,17,0,0,165,171,3,8,4,0,166,
        167,5,17,0,0,167,171,3,10,5,0,168,169,5,17,0,0,169,171,3,14,7,0,
        170,164,1,0,0,0,170,166,1,0,0,0,170,168,1,0,0,0,171,23,1,0,0,0,172,
        173,5,18,0,0,173,179,3,8,4,0,174,175,5,18,0,0,175,179,3,10,5,0,176,
        177,5,18,0,0,177,179,3,14,7,0,178,172,1,0,0,0,178,174,1,0,0,0,178,
        176,1,0,0,0,179,25,1,0,0,0,180,181,5,19,0,0,181,182,3,10,5,0,182,
        183,5,14,0,0,183,184,3,8,4,0,184,196,1,0,0,0,185,186,5,19,0,0,186,
        187,3,10,5,0,187,188,5,14,0,0,188,189,3,10,5,0,189,196,1,0,0,0,190,
        191,5,19,0,0,191,192,3,10,5,0,192,193,5,14,0,0,193,194,3,14,7,0,
        194,196,1,0,0,0,195,180,1,0,0,0,195,185,1,0,0,0,195,190,1,0,0,0,
        196,27,1,0,0,0,197,198,5,20,0,0,198,212,5,42,0,0,199,200,5,21,0,
        0,200,212,5,42,0,0,201,202,5,22,0,0,202,212,5,42,0,0,203,204,5,23,
        0,0,204,212,5,42,0,0,205,206,5,24,0,0,206,212,5,42,0,0,207,208,5,
        25,0,0,208,212,5,42,0,0,209,210,5,26,0,0,210,212,5,42,0,0,211,197,
        1,0,0,0,211,199,1,0,0,0,211,201,1,0,0,0,211,203,1,0,0,0,211,205,
        1,0,0,0,211,207,1,0,0,0,211,209,1,0,0,0,212,29,1,0,0,0,213,214,5,
        27,0,0,214,215,5,42,0,0,215,31,1,0,0,0,216,217,5,28,0,0,217,33,1,
        0,0,0,218,219,5,29,0,0,219,225,3,8,4,0,220,221,5,29,0,0,221,225,
        3,10,5,0,222,225,5,30,0,0,223,225,5,31,0,0,224,218,1,0,0,0,224,220,
        1,0,0,0,224,222,1,0,0,0,224,223,1,0,0,0,225,35,1,0,0,0,226,227,5,
        32,0,0,227,231,3,10,5,0,228,231,5,33,0,0,229,231,5,34,0,0,230,226,
        1,0,0,0,230,228,1,0,0,0,230,229,1,0,0,0,231,37,1,0,0,0,232,233,5,
        35,0,0,233,237,3,10,5,0,234,235,5,35,0,0,235,237,3,14,7,0,236,232,
        1,0,0,0,236,234,1,0,0,0,237,39,1,0,0,0,238,239,5,36,0,0,239,245,
        3,8,4,0,240,241,5,36,0,0,241,245,3,10,5,0,242,243,5,36,0,0,243,245,
        3,14,7,0,244,238,1,0,0,0,244,240,1,0,0,0,244,242,1,0,0,0,245,41,
        1,0,0,0,246,247,5,37,0,0,247,251,3,10,5,0,248,249,5,37,0,0,249,251,
        3,14,7,0,250,246,1,0,0,0,250,248,1,0,0,0,251,43,1,0,0,0,252,259,
        5,38,0,0,253,254,5,38,0,0,254,255,3,10,5,0,255,256,5,14,0,0,256,
        257,5,41,0,0,257,259,1,0,0,0,258,252,1,0,0,0,258,253,1,0,0,0,259,
        45,1,0,0,0,260,261,5,39,0,0,261,47,1,0,0,0,21,50,52,55,63,81,84,
        89,99,128,145,162,170,178,195,211,224,230,236,244,250,258
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
                      "Comment", "INT", "Label", "WS_SKIP" ]

    RULE_program = 0
    RULE_oneLineCode = 1
    RULE_opLabel = 2
    RULE_oneOp = 3
    RULE_num = 4
    RULE_reg = 5
    RULE_offset = 6
    RULE_mem = 7
    RULE_move = 8
    RULE_add = 9
    RULE_sub = 10
    RULE_mul = 11
    RULE_div = 12
    RULE_cmp = 13
    RULE_jump = 14
    RULE_call = 15
    RULE_ret = 16
    RULE_push_op = 17
    RULE_pop_op = 18
    RULE_input = 19
    RULE_print = 20
    RULE_rand = 21
    RULE_dump = 22
    RULE_pause = 23

    ruleNames =  [ "program", "oneLineCode", "opLabel", "oneOp", "num", 
                   "reg", "offset", "mem", "move", "add", "sub", "mul", 
                   "div", "cmp", "jump", "call", "ret", "push_op", "pop_op", 
                   "input", "print", "rand", "dump", "pause" ]

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
    WS_SKIP=43

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

        def Comment(self, i:int=None):
            if i is None:
                return self.getTokens(toy_asmParser.Comment)
            else:
                return self.getToken(toy_asmParser.Comment, i)

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
            self.state = 50 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 50
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [40]:
                    self.state = 48
                    self.match(toy_asmParser.Comment)
                    pass
                elif token in [13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 42]:
                    self.state = 49
                    self.oneLineCode()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 52 
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
        self.enterRule(localctx, 2, self.RULE_oneLineCode)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 54
                self.opLabel()


            self.state = 57
            self.oneOp()
            self.state = 58
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
        self.enterRule(localctx, 4, self.RULE_opLabel)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(toy_asmParser.Label)
            self.state = 61
            self.match(toy_asmParser.T__1)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 62
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
        self.enterRule(localctx, 6, self.RULE_oneOp)
        try:
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self.move()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.add()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 67
                self.sub()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 4)
                self.state = 68
                self.mul()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 5)
                self.state = 69
                self.div()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 6)
                self.state = 70
                self.cmp()
                pass
            elif token in [20, 21, 22, 23, 24, 25, 26]:
                self.enterOuterAlt(localctx, 7)
                self.state = 71
                self.jump()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 8)
                self.state = 72
                self.call()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 9)
                self.state = 73
                self.ret()
                pass
            elif token in [29, 30, 31]:
                self.enterOuterAlt(localctx, 10)
                self.state = 74
                self.push_op()
                pass
            elif token in [32, 33, 34]:
                self.enterOuterAlt(localctx, 11)
                self.state = 75
                self.pop_op()
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 12)
                self.state = 76
                self.input_()
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 13)
                self.state = 77
                self.print_()
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 14)
                self.state = 78
                self.rand()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 15)
                self.state = 79
                self.dump()
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 16)
                self.state = 80
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
        self.enterRule(localctx, 8, self.RULE_num)
        self._la = 0 # Token type
        try:
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==3:
                    self.state = 83
                    self.match(toy_asmParser.T__2)


                self.state = 86
                self.match(toy_asmParser.INT)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.match(toy_asmParser.T__3)
                self.state = 88
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
        self.enterRule(localctx, 10, self.RULE_reg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
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
        self.enterRule(localctx, 12, self.RULE_offset)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            _la = self._input.LA(1)
            if not(_la==3 or _la==4):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 94
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
        self.enterRule(localctx, 14, self.RULE_mem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(toy_asmParser.T__10)
            self.state = 97
            self.reg()
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3 or _la==4:
                self.state = 98
                self.offset()


            self.state = 101
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
        self.enterRule(localctx, 16, self.RULE_move)
        try:
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.match(toy_asmParser.T__12)
                self.state = 104
                self.reg()
                self.state = 105
                self.match(toy_asmParser.T__13)
                self.state = 106
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.match(toy_asmParser.T__12)
                self.state = 109
                self.reg()
                self.state = 110
                self.match(toy_asmParser.T__13)
                self.state = 111
                self.reg()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 113
                self.match(toy_asmParser.T__12)
                self.state = 114
                self.reg()
                self.state = 115
                self.match(toy_asmParser.T__13)
                self.state = 116
                self.mem()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 118
                self.match(toy_asmParser.T__12)
                self.state = 119
                self.mem()
                self.state = 120
                self.match(toy_asmParser.T__13)
                self.state = 121
                self.num()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 123
                self.match(toy_asmParser.T__12)
                self.state = 124
                self.mem()
                self.state = 125
                self.match(toy_asmParser.T__13)
                self.state = 126
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
        self.enterRule(localctx, 18, self.RULE_add)
        try:
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.match(toy_asmParser.T__14)
                self.state = 131
                self.reg()
                self.state = 132
                self.match(toy_asmParser.T__13)
                self.state = 133
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.match(toy_asmParser.T__14)
                self.state = 136
                self.reg()
                self.state = 137
                self.match(toy_asmParser.T__13)
                self.state = 138
                self.reg()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 140
                self.match(toy_asmParser.T__14)
                self.state = 141
                self.reg()
                self.state = 142
                self.match(toy_asmParser.T__13)
                self.state = 143
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
        self.enterRule(localctx, 20, self.RULE_sub)
        try:
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.match(toy_asmParser.T__15)
                self.state = 148
                self.reg()
                self.state = 149
                self.match(toy_asmParser.T__13)
                self.state = 150
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.match(toy_asmParser.T__15)
                self.state = 153
                self.reg()
                self.state = 154
                self.match(toy_asmParser.T__13)
                self.state = 155
                self.reg()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 157
                self.match(toy_asmParser.T__15)
                self.state = 158
                self.reg()
                self.state = 159
                self.match(toy_asmParser.T__13)
                self.state = 160
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
        self.enterRule(localctx, 22, self.RULE_mul)
        try:
            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.match(toy_asmParser.T__16)
                self.state = 165
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.match(toy_asmParser.T__16)
                self.state = 167
                self.reg()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 168
                self.match(toy_asmParser.T__16)
                self.state = 169
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
        self.enterRule(localctx, 24, self.RULE_div)
        try:
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.match(toy_asmParser.T__17)
                self.state = 173
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.match(toy_asmParser.T__17)
                self.state = 175
                self.reg()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 176
                self.match(toy_asmParser.T__17)
                self.state = 177
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
        self.enterRule(localctx, 26, self.RULE_cmp)
        try:
            self.state = 195
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.match(toy_asmParser.T__18)
                self.state = 181
                self.reg()
                self.state = 182
                self.match(toy_asmParser.T__13)
                self.state = 183
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.match(toy_asmParser.T__18)
                self.state = 186
                self.reg()
                self.state = 187
                self.match(toy_asmParser.T__13)
                self.state = 188
                self.reg()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 190
                self.match(toy_asmParser.T__18)
                self.state = 191
                self.reg()
                self.state = 192
                self.match(toy_asmParser.T__13)
                self.state = 193
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
        self.enterRule(localctx, 28, self.RULE_jump)
        try:
            self.state = 211
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.match(toy_asmParser.T__19)
                self.state = 198
                self.match(toy_asmParser.Label)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self.match(toy_asmParser.T__20)
                self.state = 200
                self.match(toy_asmParser.Label)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 201
                self.match(toy_asmParser.T__21)
                self.state = 202
                self.match(toy_asmParser.Label)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 4)
                self.state = 203
                self.match(toy_asmParser.T__22)
                self.state = 204
                self.match(toy_asmParser.Label)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 5)
                self.state = 205
                self.match(toy_asmParser.T__23)
                self.state = 206
                self.match(toy_asmParser.Label)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 6)
                self.state = 207
                self.match(toy_asmParser.T__24)
                self.state = 208
                self.match(toy_asmParser.Label)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 7)
                self.state = 209
                self.match(toy_asmParser.T__25)
                self.state = 210
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
        self.enterRule(localctx, 30, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(toy_asmParser.T__26)
            self.state = 214
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
        self.enterRule(localctx, 32, self.RULE_ret)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
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
        self.enterRule(localctx, 34, self.RULE_push_op)
        try:
            self.state = 224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.match(toy_asmParser.T__28)
                self.state = 219
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.match(toy_asmParser.T__28)
                self.state = 221
                self.reg()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 222
                self.match(toy_asmParser.T__29)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 223
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
        self.enterRule(localctx, 36, self.RULE_pop_op)
        try:
            self.state = 230
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.match(toy_asmParser.T__31)
                self.state = 227
                self.reg()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 228
                self.match(toy_asmParser.T__32)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 3)
                self.state = 229
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
        self.enterRule(localctx, 38, self.RULE_input)
        try:
            self.state = 236
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.match(toy_asmParser.T__34)
                self.state = 233
                self.reg()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
                self.match(toy_asmParser.T__34)
                self.state = 235
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
        self.enterRule(localctx, 40, self.RULE_print)
        try:
            self.state = 244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.match(toy_asmParser.T__35)
                self.state = 239
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
                self.match(toy_asmParser.T__35)
                self.state = 241
                self.reg()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 242
                self.match(toy_asmParser.T__35)
                self.state = 243
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
        self.enterRule(localctx, 42, self.RULE_rand)
        try:
            self.state = 250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.match(toy_asmParser.T__36)
                self.state = 247
                self.reg()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                self.match(toy_asmParser.T__36)
                self.state = 249
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
        self.enterRule(localctx, 44, self.RULE_dump)
        try:
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.match(toy_asmParser.T__37)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
                self.match(toy_asmParser.T__37)
                self.state = 254
                self.reg()
                self.state = 255
                self.match(toy_asmParser.T__13)
                self.state = 256
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
        self.enterRule(localctx, 46, self.RULE_pause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(toy_asmParser.T__38)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





