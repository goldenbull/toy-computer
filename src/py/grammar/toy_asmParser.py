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
        4,1,45,288,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,1,0,1,0,4,
        0,55,8,0,11,0,12,0,56,1,0,1,0,1,1,3,1,62,8,1,1,1,1,1,1,2,1,2,1,2,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,3,3,86,8,3,1,4,3,4,89,8,4,1,4,1,4,1,4,3,4,94,8,4,1,5,1,5,1,6,
        1,6,1,6,1,7,1,7,1,7,3,7,104,8,7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,3,9,135,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,152,8,10,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,3,11,169,8,11,1,12,1,12,1,12,1,12,1,12,1,12,3,12,177,8,12,1,13,
        1,13,1,13,1,13,1,13,1,13,3,13,185,8,13,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,202,8,14,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,3,15,218,8,15,1,16,1,16,1,16,1,17,1,17,1,18,1,18,1,18,1,18,
        1,18,1,18,3,18,231,8,18,1,19,1,19,1,19,1,19,1,19,3,19,238,8,19,1,
        20,1,20,1,20,1,20,3,20,244,8,20,1,21,1,21,1,21,1,21,1,21,1,21,1,
        21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,263,8,
        21,1,22,1,22,1,22,1,22,3,22,269,8,22,1,23,1,23,1,23,1,23,1,23,1,
        23,1,23,1,23,1,23,1,23,1,23,3,23,282,8,23,1,24,1,24,1,25,1,25,1,
        25,0,0,26,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,46,48,50,0,2,1,0,4,9,1,0,2,3,321,0,54,1,0,0,0,2,61,1,0,
        0,0,4,65,1,0,0,0,6,85,1,0,0,0,8,93,1,0,0,0,10,95,1,0,0,0,12,97,1,
        0,0,0,14,100,1,0,0,0,16,107,1,0,0,0,18,134,1,0,0,0,20,151,1,0,0,
        0,22,168,1,0,0,0,24,176,1,0,0,0,26,184,1,0,0,0,28,201,1,0,0,0,30,
        217,1,0,0,0,32,219,1,0,0,0,34,222,1,0,0,0,36,230,1,0,0,0,38,237,
        1,0,0,0,40,243,1,0,0,0,42,262,1,0,0,0,44,268,1,0,0,0,46,281,1,0,
        0,0,48,283,1,0,0,0,50,285,1,0,0,0,52,55,5,41,0,0,53,55,3,2,1,0,54,
        52,1,0,0,0,54,53,1,0,0,0,55,56,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,
        0,57,58,1,0,0,0,58,59,5,0,0,1,59,1,1,0,0,0,60,62,3,4,2,0,61,60,1,
        0,0,0,61,62,1,0,0,0,62,63,1,0,0,0,63,64,3,6,3,0,64,3,1,0,0,0,65,
        66,5,43,0,0,66,67,5,1,0,0,67,5,1,0,0,0,68,86,3,18,9,0,69,86,3,20,
        10,0,70,86,3,22,11,0,71,86,3,24,12,0,72,86,3,26,13,0,73,86,3,28,
        14,0,74,86,3,30,15,0,75,86,3,32,16,0,76,86,3,34,17,0,77,86,3,36,
        18,0,78,86,3,38,19,0,79,86,3,40,20,0,80,86,3,42,21,0,81,86,3,44,
        22,0,82,86,3,46,23,0,83,86,3,48,24,0,84,86,3,50,25,0,85,68,1,0,0,
        0,85,69,1,0,0,0,85,70,1,0,0,0,85,71,1,0,0,0,85,72,1,0,0,0,85,73,
        1,0,0,0,85,74,1,0,0,0,85,75,1,0,0,0,85,76,1,0,0,0,85,77,1,0,0,0,
        85,78,1,0,0,0,85,79,1,0,0,0,85,80,1,0,0,0,85,81,1,0,0,0,85,82,1,
        0,0,0,85,83,1,0,0,0,85,84,1,0,0,0,86,7,1,0,0,0,87,89,5,2,0,0,88,
        87,1,0,0,0,88,89,1,0,0,0,89,90,1,0,0,0,90,94,5,42,0,0,91,92,5,3,
        0,0,92,94,5,42,0,0,93,88,1,0,0,0,93,91,1,0,0,0,94,9,1,0,0,0,95,96,
        7,0,0,0,96,11,1,0,0,0,97,98,7,1,0,0,98,99,5,42,0,0,99,13,1,0,0,0,
        100,101,5,10,0,0,101,103,3,10,5,0,102,104,3,12,6,0,103,102,1,0,0,
        0,103,104,1,0,0,0,104,105,1,0,0,0,105,106,5,11,0,0,106,15,1,0,0,
        0,107,108,5,44,0,0,108,17,1,0,0,0,109,110,5,12,0,0,110,111,3,10,
        5,0,111,112,5,13,0,0,112,113,3,8,4,0,113,135,1,0,0,0,114,115,5,12,
        0,0,115,116,3,10,5,0,116,117,5,13,0,0,117,118,3,10,5,0,118,135,1,
        0,0,0,119,120,5,12,0,0,120,121,3,10,5,0,121,122,5,13,0,0,122,123,
        3,14,7,0,123,135,1,0,0,0,124,125,5,12,0,0,125,126,3,14,7,0,126,127,
        5,13,0,0,127,128,3,8,4,0,128,135,1,0,0,0,129,130,5,12,0,0,130,131,
        3,14,7,0,131,132,5,13,0,0,132,133,3,10,5,0,133,135,1,0,0,0,134,109,
        1,0,0,0,134,114,1,0,0,0,134,119,1,0,0,0,134,124,1,0,0,0,134,129,
        1,0,0,0,135,19,1,0,0,0,136,137,5,14,0,0,137,138,3,10,5,0,138,139,
        5,13,0,0,139,140,3,8,4,0,140,152,1,0,0,0,141,142,5,14,0,0,142,143,
        3,10,5,0,143,144,5,13,0,0,144,145,3,10,5,0,145,152,1,0,0,0,146,147,
        5,14,0,0,147,148,3,10,5,0,148,149,5,13,0,0,149,150,3,14,7,0,150,
        152,1,0,0,0,151,136,1,0,0,0,151,141,1,0,0,0,151,146,1,0,0,0,152,
        21,1,0,0,0,153,154,5,15,0,0,154,155,3,10,5,0,155,156,5,13,0,0,156,
        157,3,8,4,0,157,169,1,0,0,0,158,159,5,15,0,0,159,160,3,10,5,0,160,
        161,5,13,0,0,161,162,3,10,5,0,162,169,1,0,0,0,163,164,5,15,0,0,164,
        165,3,10,5,0,165,166,5,13,0,0,166,167,3,14,7,0,167,169,1,0,0,0,168,
        153,1,0,0,0,168,158,1,0,0,0,168,163,1,0,0,0,169,23,1,0,0,0,170,171,
        5,16,0,0,171,177,3,8,4,0,172,173,5,16,0,0,173,177,3,10,5,0,174,175,
        5,16,0,0,175,177,3,14,7,0,176,170,1,0,0,0,176,172,1,0,0,0,176,174,
        1,0,0,0,177,25,1,0,0,0,178,179,5,17,0,0,179,185,3,8,4,0,180,181,
        5,17,0,0,181,185,3,10,5,0,182,183,5,17,0,0,183,185,3,14,7,0,184,
        178,1,0,0,0,184,180,1,0,0,0,184,182,1,0,0,0,185,27,1,0,0,0,186,187,
        5,18,0,0,187,188,3,10,5,0,188,189,5,13,0,0,189,190,3,8,4,0,190,202,
        1,0,0,0,191,192,5,18,0,0,192,193,3,10,5,0,193,194,5,13,0,0,194,195,
        3,10,5,0,195,202,1,0,0,0,196,197,5,18,0,0,197,198,3,10,5,0,198,199,
        5,13,0,0,199,200,3,14,7,0,200,202,1,0,0,0,201,186,1,0,0,0,201,191,
        1,0,0,0,201,196,1,0,0,0,202,29,1,0,0,0,203,204,5,19,0,0,204,218,
        5,43,0,0,205,206,5,20,0,0,206,218,5,43,0,0,207,208,5,21,0,0,208,
        218,5,43,0,0,209,210,5,22,0,0,210,218,5,43,0,0,211,212,5,23,0,0,
        212,218,5,43,0,0,213,214,5,24,0,0,214,218,5,43,0,0,215,216,5,25,
        0,0,216,218,5,43,0,0,217,203,1,0,0,0,217,205,1,0,0,0,217,207,1,0,
        0,0,217,209,1,0,0,0,217,211,1,0,0,0,217,213,1,0,0,0,217,215,1,0,
        0,0,218,31,1,0,0,0,219,220,5,26,0,0,220,221,5,43,0,0,221,33,1,0,
        0,0,222,223,5,27,0,0,223,35,1,0,0,0,224,225,5,28,0,0,225,231,3,8,
        4,0,226,227,5,28,0,0,227,231,3,10,5,0,228,231,5,29,0,0,229,231,5,
        30,0,0,230,224,1,0,0,0,230,226,1,0,0,0,230,228,1,0,0,0,230,229,1,
        0,0,0,231,37,1,0,0,0,232,238,5,31,0,0,233,234,5,31,0,0,234,238,3,
        10,5,0,235,238,5,32,0,0,236,238,5,33,0,0,237,232,1,0,0,0,237,233,
        1,0,0,0,237,235,1,0,0,0,237,236,1,0,0,0,238,39,1,0,0,0,239,240,5,
        34,0,0,240,244,3,10,5,0,241,242,5,34,0,0,242,244,3,14,7,0,243,239,
        1,0,0,0,243,241,1,0,0,0,244,41,1,0,0,0,245,246,5,35,0,0,246,263,
        3,8,4,0,247,248,5,35,0,0,248,263,3,10,5,0,249,250,5,35,0,0,250,263,
        3,14,7,0,251,252,5,35,0,0,252,263,3,16,8,0,253,254,5,36,0,0,254,
        263,3,8,4,0,255,256,5,36,0,0,256,263,3,10,5,0,257,258,5,36,0,0,258,
        263,3,14,7,0,259,260,5,36,0,0,260,263,3,16,8,0,261,263,5,36,0,0,
        262,245,1,0,0,0,262,247,1,0,0,0,262,249,1,0,0,0,262,251,1,0,0,0,
        262,253,1,0,0,0,262,255,1,0,0,0,262,257,1,0,0,0,262,259,1,0,0,0,
        262,261,1,0,0,0,263,43,1,0,0,0,264,265,5,37,0,0,265,269,3,10,5,0,
        266,267,5,37,0,0,267,269,3,14,7,0,268,264,1,0,0,0,268,266,1,0,0,
        0,269,45,1,0,0,0,270,282,5,38,0,0,271,272,5,38,0,0,272,273,3,10,
        5,0,273,274,5,13,0,0,274,275,5,42,0,0,275,282,1,0,0,0,276,277,5,
        38,0,0,277,278,3,8,4,0,278,279,5,13,0,0,279,280,5,42,0,0,280,282,
        1,0,0,0,281,270,1,0,0,0,281,271,1,0,0,0,281,276,1,0,0,0,282,47,1,
        0,0,0,283,284,5,39,0,0,284,49,1,0,0,0,285,286,5,40,0,0,286,51,1,
        0,0,0,20,54,56,61,85,88,93,103,134,151,168,176,184,201,217,230,237,
        243,262,268,281
    ]

class toy_asmParser ( Parser ):

    grammarFileName = "toy_asm.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'+'", "'-'", "'ax'", "'bx'", "'cx'", 
                     "'dx'", "'bp'", "'sp'", "'['", "']'", "'mov'", "','", 
                     "'add'", "'sub'", "'mul'", "'div'", "'cmp'", "'jmp'", 
                     "'je'", "'jne'", "'jg'", "'jge'", "'jl'", "'jle'", 
                     "'call'", "'ret'", "'push'", "'pushf'", "'pusha'", 
                     "'pop'", "'popf'", "'popa'", "'input'", "'print'", 
                     "'println'", "'rand'", "'dump'", "'halt'", "'nop'" ]

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
                      "<INVALID>", "Comment", "INT", "Label", "STR", "WS" ]

    RULE_program = 0
    RULE_opWithLabel = 1
    RULE_opLabel = 2
    RULE_op = 3
    RULE_num = 4
    RULE_reg = 5
    RULE_offset = 6
    RULE_mem = 7
    RULE_str = 8
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
    RULE_halt = 24
    RULE_nop = 25

    ruleNames =  [ "program", "opWithLabel", "opLabel", "op", "num", "reg", 
                   "offset", "mem", "str", "move", "add", "sub", "mul", 
                   "div", "cmp", "jump", "call", "ret", "push_op", "pop_op", 
                   "input", "print", "rand", "dump", "halt", "nop" ]

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
    T__39=40
    Comment=41
    INT=42
    Label=43
    STR=44
    WS=45

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

        def EOF(self):
            return self.getToken(toy_asmParser.EOF, 0)

        def Comment(self, i:int=None):
            if i is None:
                return self.getTokens(toy_asmParser.Comment)
            else:
                return self.getToken(toy_asmParser.Comment, i)

        def opWithLabel(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(toy_asmParser.OpWithLabelContext)
            else:
                return self.getTypedRuleContext(toy_asmParser.OpWithLabelContext,i)


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
            self.state = 54 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 54
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [41]:
                    self.state = 52
                    self.match(toy_asmParser.Comment)
                    pass
                elif token in [12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 43]:
                    self.state = 53
                    self.opWithLabel()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 56 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 13194139521024) != 0)):
                    break

            self.state = 58
            self.match(toy_asmParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpWithLabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op(self):
            return self.getTypedRuleContext(toy_asmParser.OpContext,0)


        def opLabel(self):
            return self.getTypedRuleContext(toy_asmParser.OpLabelContext,0)


        def getRuleIndex(self):
            return toy_asmParser.RULE_opWithLabel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpWithLabel" ):
                listener.enterOpWithLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpWithLabel" ):
                listener.exitOpWithLabel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpWithLabel" ):
                return visitor.visitOpWithLabel(self)
            else:
                return visitor.visitChildren(self)




    def opWithLabel(self):

        localctx = toy_asmParser.OpWithLabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_opWithLabel)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==43:
                self.state = 60
                self.opLabel()


            self.state = 63
            self.op()
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(toy_asmParser.Label)
            self.state = 66
            self.match(toy_asmParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpContext(ParserRuleContext):
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


        def halt(self):
            return self.getTypedRuleContext(toy_asmParser.HaltContext,0)


        def nop(self):
            return self.getTypedRuleContext(toy_asmParser.NopContext,0)


        def getRuleIndex(self):
            return toy_asmParser.RULE_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp" ):
                listener.enterOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp" ):
                listener.exitOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp" ):
                return visitor.visitOp(self)
            else:
                return visitor.visitChildren(self)




    def op(self):

        localctx = toy_asmParser.OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_op)
        try:
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.move()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.add()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 70
                self.sub()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 4)
                self.state = 71
                self.mul()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 5)
                self.state = 72
                self.div()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 6)
                self.state = 73
                self.cmp()
                pass
            elif token in [19, 20, 21, 22, 23, 24, 25]:
                self.enterOuterAlt(localctx, 7)
                self.state = 74
                self.jump()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 8)
                self.state = 75
                self.call()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 9)
                self.state = 76
                self.ret()
                pass
            elif token in [28, 29, 30]:
                self.enterOuterAlt(localctx, 10)
                self.state = 77
                self.push_op()
                pass
            elif token in [31, 32, 33]:
                self.enterOuterAlt(localctx, 11)
                self.state = 78
                self.pop_op()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 12)
                self.state = 79
                self.input_()
                pass
            elif token in [35, 36]:
                self.enterOuterAlt(localctx, 13)
                self.state = 80
                self.print_()
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 14)
                self.state = 81
                self.rand()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 15)
                self.state = 82
                self.dump()
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 16)
                self.state = 83
                self.halt()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 17)
                self.state = 84
                self.nop()
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
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2:
                    self.state = 87
                    self.match(toy_asmParser.T__1)


                self.state = 90
                self.match(toy_asmParser.INT)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.match(toy_asmParser.T__2)
                self.state = 92
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
            self.state = 95
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1008) != 0)):
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
            self.state = 97
            _la = self._input.LA(1)
            if not(_la==2 or _la==3):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 98
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
            self.state = 100
            self.match(toy_asmParser.T__9)
            self.state = 101
            self.reg()
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2 or _la==3:
                self.state = 102
                self.offset()


            self.state = 105
            self.match(toy_asmParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STR(self):
            return self.getToken(toy_asmParser.STR, 0)

        def getRuleIndex(self):
            return toy_asmParser.RULE_str

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStr" ):
                listener.enterStr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStr" ):
                listener.exitStr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStr" ):
                return visitor.visitStr(self)
            else:
                return visitor.visitChildren(self)




    def str_(self):

        localctx = toy_asmParser.StrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_str)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(toy_asmParser.STR)
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
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.match(toy_asmParser.T__11)
                self.state = 110
                self.reg()
                self.state = 111
                self.match(toy_asmParser.T__12)
                self.state = 112
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.match(toy_asmParser.T__11)
                self.state = 115
                self.reg()
                self.state = 116
                self.match(toy_asmParser.T__12)
                self.state = 117
                self.reg()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 119
                self.match(toy_asmParser.T__11)
                self.state = 120
                self.reg()
                self.state = 121
                self.match(toy_asmParser.T__12)
                self.state = 122
                self.mem()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 124
                self.match(toy_asmParser.T__11)
                self.state = 125
                self.mem()
                self.state = 126
                self.match(toy_asmParser.T__12)
                self.state = 127
                self.num()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 129
                self.match(toy_asmParser.T__11)
                self.state = 130
                self.mem()
                self.state = 131
                self.match(toy_asmParser.T__12)
                self.state = 132
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
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.match(toy_asmParser.T__13)
                self.state = 137
                self.reg()
                self.state = 138
                self.match(toy_asmParser.T__12)
                self.state = 139
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.match(toy_asmParser.T__13)
                self.state = 142
                self.reg()
                self.state = 143
                self.match(toy_asmParser.T__12)
                self.state = 144
                self.reg()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 146
                self.match(toy_asmParser.T__13)
                self.state = 147
                self.reg()
                self.state = 148
                self.match(toy_asmParser.T__12)
                self.state = 149
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
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.match(toy_asmParser.T__14)
                self.state = 154
                self.reg()
                self.state = 155
                self.match(toy_asmParser.T__12)
                self.state = 156
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.match(toy_asmParser.T__14)
                self.state = 159
                self.reg()
                self.state = 160
                self.match(toy_asmParser.T__12)
                self.state = 161
                self.reg()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 163
                self.match(toy_asmParser.T__14)
                self.state = 164
                self.reg()
                self.state = 165
                self.match(toy_asmParser.T__12)
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
            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.match(toy_asmParser.T__15)
                self.state = 171
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.match(toy_asmParser.T__15)
                self.state = 173
                self.reg()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 174
                self.match(toy_asmParser.T__15)
                self.state = 175
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
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.match(toy_asmParser.T__16)
                self.state = 179
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.match(toy_asmParser.T__16)
                self.state = 181
                self.reg()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 182
                self.match(toy_asmParser.T__16)
                self.state = 183
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
            self.state = 201
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.match(toy_asmParser.T__17)
                self.state = 187
                self.reg()
                self.state = 188
                self.match(toy_asmParser.T__12)
                self.state = 189
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.match(toy_asmParser.T__17)
                self.state = 192
                self.reg()
                self.state = 193
                self.match(toy_asmParser.T__12)
                self.state = 194
                self.reg()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 196
                self.match(toy_asmParser.T__17)
                self.state = 197
                self.reg()
                self.state = 198
                self.match(toy_asmParser.T__12)
                self.state = 199
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
            self.state = 217
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.match(toy_asmParser.T__18)
                self.state = 204
                self.match(toy_asmParser.Label)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 205
                self.match(toy_asmParser.T__19)
                self.state = 206
                self.match(toy_asmParser.Label)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 207
                self.match(toy_asmParser.T__20)
                self.state = 208
                self.match(toy_asmParser.Label)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 4)
                self.state = 209
                self.match(toy_asmParser.T__21)
                self.state = 210
                self.match(toy_asmParser.Label)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 5)
                self.state = 211
                self.match(toy_asmParser.T__22)
                self.state = 212
                self.match(toy_asmParser.Label)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 6)
                self.state = 213
                self.match(toy_asmParser.T__23)
                self.state = 214
                self.match(toy_asmParser.Label)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 7)
                self.state = 215
                self.match(toy_asmParser.T__24)
                self.state = 216
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
            self.state = 219
            self.match(toy_asmParser.T__25)
            self.state = 220
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
            self.state = 222
            self.match(toy_asmParser.T__26)
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
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.match(toy_asmParser.T__27)
                self.state = 225
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.match(toy_asmParser.T__27)
                self.state = 227
                self.reg()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 228
                self.match(toy_asmParser.T__28)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 229
                self.match(toy_asmParser.T__29)
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
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.match(toy_asmParser.T__30)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.match(toy_asmParser.T__30)
                self.state = 234
                self.reg()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 235
                self.match(toy_asmParser.T__31)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 236
                self.match(toy_asmParser.T__32)
                pass


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
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.match(toy_asmParser.T__33)
                self.state = 240
                self.reg()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
                self.match(toy_asmParser.T__33)
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


        def str_(self):
            return self.getTypedRuleContext(toy_asmParser.StrContext,0)


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
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.match(toy_asmParser.T__34)
                self.state = 246
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.match(toy_asmParser.T__34)
                self.state = 248
                self.reg()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 249
                self.match(toy_asmParser.T__34)
                self.state = 250
                self.mem()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 251
                self.match(toy_asmParser.T__34)
                self.state = 252
                self.str_()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 253
                self.match(toy_asmParser.T__35)
                self.state = 254
                self.num()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 255
                self.match(toy_asmParser.T__35)
                self.state = 256
                self.reg()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 257
                self.match(toy_asmParser.T__35)
                self.state = 258
                self.mem()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 259
                self.match(toy_asmParser.T__35)
                self.state = 260
                self.str_()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 261
                self.match(toy_asmParser.T__35)
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
            self.state = 268
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.match(toy_asmParser.T__36)
                self.state = 265
                self.reg()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 266
                self.match(toy_asmParser.T__36)
                self.state = 267
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

        def num(self):
            return self.getTypedRuleContext(toy_asmParser.NumContext,0)


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
            self.state = 281
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 270
                self.match(toy_asmParser.T__37)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 271
                self.match(toy_asmParser.T__37)
                self.state = 272
                self.reg()
                self.state = 273
                self.match(toy_asmParser.T__12)
                self.state = 274
                self.match(toy_asmParser.INT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 276
                self.match(toy_asmParser.T__37)
                self.state = 277
                self.num()
                self.state = 278
                self.match(toy_asmParser.T__12)
                self.state = 279
                self.match(toy_asmParser.INT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HaltContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return toy_asmParser.RULE_halt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHalt" ):
                listener.enterHalt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHalt" ):
                listener.exitHalt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHalt" ):
                return visitor.visitHalt(self)
            else:
                return visitor.visitChildren(self)




    def halt(self):

        localctx = toy_asmParser.HaltContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_halt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(toy_asmParser.T__38)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return toy_asmParser.RULE_nop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNop" ):
                listener.enterNop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNop" ):
                listener.exitNop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNop" ):
                return visitor.visitNop(self)
            else:
                return visitor.visitChildren(self)




    def nop(self):

        localctx = toy_asmParser.NopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_nop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(toy_asmParser.T__39)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





