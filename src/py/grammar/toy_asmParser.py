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
        4,1,45,287,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,1,0,1,0,5,0,54,
        8,0,10,0,12,0,57,9,0,1,0,1,0,3,0,61,8,0,1,0,1,0,1,1,1,1,1,1,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        3,2,85,8,2,1,3,3,3,88,8,3,1,3,1,3,1,3,3,3,93,8,3,1,4,1,4,1,5,1,5,
        1,5,1,6,1,6,1,6,3,6,103,8,6,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,3,8,134,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,3,9,151,8,9,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,168,8,10,1,11,
        1,11,1,11,1,11,1,11,1,11,3,11,176,8,11,1,12,1,12,1,12,1,12,1,12,
        1,12,3,12,184,8,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,3,13,201,8,13,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,217,8,14,
        1,15,1,15,1,15,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,3,17,230,
        8,17,1,18,1,18,1,18,1,18,1,18,3,18,237,8,18,1,19,1,19,1,19,1,19,
        3,19,243,8,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,262,8,20,1,21,1,21,1,21,
        1,21,3,21,268,8,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,
        1,22,1,22,3,22,281,8,22,1,23,1,23,1,24,1,24,1,24,0,0,25,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,0,
        2,1,0,4,9,1,0,2,3,322,0,55,1,0,0,0,2,64,1,0,0,0,4,84,1,0,0,0,6,92,
        1,0,0,0,8,94,1,0,0,0,10,96,1,0,0,0,12,99,1,0,0,0,14,106,1,0,0,0,
        16,133,1,0,0,0,18,150,1,0,0,0,20,167,1,0,0,0,22,175,1,0,0,0,24,183,
        1,0,0,0,26,200,1,0,0,0,28,216,1,0,0,0,30,218,1,0,0,0,32,221,1,0,
        0,0,34,229,1,0,0,0,36,236,1,0,0,0,38,242,1,0,0,0,40,261,1,0,0,0,
        42,267,1,0,0,0,44,280,1,0,0,0,46,282,1,0,0,0,48,284,1,0,0,0,50,54,
        5,41,0,0,51,54,3,2,1,0,52,54,3,4,2,0,53,50,1,0,0,0,53,51,1,0,0,0,
        53,52,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,60,1,
        0,0,0,57,55,1,0,0,0,58,61,5,41,0,0,59,61,3,4,2,0,60,58,1,0,0,0,60,
        59,1,0,0,0,61,62,1,0,0,0,62,63,5,0,0,1,63,1,1,0,0,0,64,65,5,43,0,
        0,65,66,5,1,0,0,66,3,1,0,0,0,67,85,3,16,8,0,68,85,3,18,9,0,69,85,
        3,20,10,0,70,85,3,22,11,0,71,85,3,24,12,0,72,85,3,26,13,0,73,85,
        3,28,14,0,74,85,3,30,15,0,75,85,3,32,16,0,76,85,3,34,17,0,77,85,
        3,36,18,0,78,85,3,38,19,0,79,85,3,40,20,0,80,85,3,42,21,0,81,85,
        3,44,22,0,82,85,3,46,23,0,83,85,3,48,24,0,84,67,1,0,0,0,84,68,1,
        0,0,0,84,69,1,0,0,0,84,70,1,0,0,0,84,71,1,0,0,0,84,72,1,0,0,0,84,
        73,1,0,0,0,84,74,1,0,0,0,84,75,1,0,0,0,84,76,1,0,0,0,84,77,1,0,0,
        0,84,78,1,0,0,0,84,79,1,0,0,0,84,80,1,0,0,0,84,81,1,0,0,0,84,82,
        1,0,0,0,84,83,1,0,0,0,85,5,1,0,0,0,86,88,5,2,0,0,87,86,1,0,0,0,87,
        88,1,0,0,0,88,89,1,0,0,0,89,93,5,42,0,0,90,91,5,3,0,0,91,93,5,42,
        0,0,92,87,1,0,0,0,92,90,1,0,0,0,93,7,1,0,0,0,94,95,7,0,0,0,95,9,
        1,0,0,0,96,97,7,1,0,0,97,98,5,42,0,0,98,11,1,0,0,0,99,100,5,10,0,
        0,100,102,3,8,4,0,101,103,3,10,5,0,102,101,1,0,0,0,102,103,1,0,0,
        0,103,104,1,0,0,0,104,105,5,11,0,0,105,13,1,0,0,0,106,107,5,44,0,
        0,107,15,1,0,0,0,108,109,5,12,0,0,109,110,3,8,4,0,110,111,5,13,0,
        0,111,112,3,6,3,0,112,134,1,0,0,0,113,114,5,12,0,0,114,115,3,8,4,
        0,115,116,5,13,0,0,116,117,3,8,4,0,117,134,1,0,0,0,118,119,5,12,
        0,0,119,120,3,8,4,0,120,121,5,13,0,0,121,122,3,12,6,0,122,134,1,
        0,0,0,123,124,5,12,0,0,124,125,3,12,6,0,125,126,5,13,0,0,126,127,
        3,6,3,0,127,134,1,0,0,0,128,129,5,12,0,0,129,130,3,12,6,0,130,131,
        5,13,0,0,131,132,3,8,4,0,132,134,1,0,0,0,133,108,1,0,0,0,133,113,
        1,0,0,0,133,118,1,0,0,0,133,123,1,0,0,0,133,128,1,0,0,0,134,17,1,
        0,0,0,135,136,5,14,0,0,136,137,3,8,4,0,137,138,5,13,0,0,138,139,
        3,6,3,0,139,151,1,0,0,0,140,141,5,14,0,0,141,142,3,8,4,0,142,143,
        5,13,0,0,143,144,3,8,4,0,144,151,1,0,0,0,145,146,5,14,0,0,146,147,
        3,8,4,0,147,148,5,13,0,0,148,149,3,12,6,0,149,151,1,0,0,0,150,135,
        1,0,0,0,150,140,1,0,0,0,150,145,1,0,0,0,151,19,1,0,0,0,152,153,5,
        15,0,0,153,154,3,8,4,0,154,155,5,13,0,0,155,156,3,6,3,0,156,168,
        1,0,0,0,157,158,5,15,0,0,158,159,3,8,4,0,159,160,5,13,0,0,160,161,
        3,8,4,0,161,168,1,0,0,0,162,163,5,15,0,0,163,164,3,8,4,0,164,165,
        5,13,0,0,165,166,3,12,6,0,166,168,1,0,0,0,167,152,1,0,0,0,167,157,
        1,0,0,0,167,162,1,0,0,0,168,21,1,0,0,0,169,170,5,16,0,0,170,176,
        3,6,3,0,171,172,5,16,0,0,172,176,3,8,4,0,173,174,5,16,0,0,174,176,
        3,12,6,0,175,169,1,0,0,0,175,171,1,0,0,0,175,173,1,0,0,0,176,23,
        1,0,0,0,177,178,5,17,0,0,178,184,3,6,3,0,179,180,5,17,0,0,180,184,
        3,8,4,0,181,182,5,17,0,0,182,184,3,12,6,0,183,177,1,0,0,0,183,179,
        1,0,0,0,183,181,1,0,0,0,184,25,1,0,0,0,185,186,5,18,0,0,186,187,
        3,8,4,0,187,188,5,13,0,0,188,189,3,6,3,0,189,201,1,0,0,0,190,191,
        5,18,0,0,191,192,3,8,4,0,192,193,5,13,0,0,193,194,3,8,4,0,194,201,
        1,0,0,0,195,196,5,18,0,0,196,197,3,8,4,0,197,198,5,13,0,0,198,199,
        3,12,6,0,199,201,1,0,0,0,200,185,1,0,0,0,200,190,1,0,0,0,200,195,
        1,0,0,0,201,27,1,0,0,0,202,203,5,19,0,0,203,217,5,43,0,0,204,205,
        5,20,0,0,205,217,5,43,0,0,206,207,5,21,0,0,207,217,5,43,0,0,208,
        209,5,22,0,0,209,217,5,43,0,0,210,211,5,23,0,0,211,217,5,43,0,0,
        212,213,5,24,0,0,213,217,5,43,0,0,214,215,5,25,0,0,215,217,5,43,
        0,0,216,202,1,0,0,0,216,204,1,0,0,0,216,206,1,0,0,0,216,208,1,0,
        0,0,216,210,1,0,0,0,216,212,1,0,0,0,216,214,1,0,0,0,217,29,1,0,0,
        0,218,219,5,26,0,0,219,220,5,43,0,0,220,31,1,0,0,0,221,222,5,27,
        0,0,222,33,1,0,0,0,223,224,5,28,0,0,224,230,3,6,3,0,225,226,5,28,
        0,0,226,230,3,8,4,0,227,230,5,29,0,0,228,230,5,30,0,0,229,223,1,
        0,0,0,229,225,1,0,0,0,229,227,1,0,0,0,229,228,1,0,0,0,230,35,1,0,
        0,0,231,237,5,31,0,0,232,233,5,31,0,0,233,237,3,8,4,0,234,237,5,
        32,0,0,235,237,5,33,0,0,236,231,1,0,0,0,236,232,1,0,0,0,236,234,
        1,0,0,0,236,235,1,0,0,0,237,37,1,0,0,0,238,239,5,34,0,0,239,243,
        3,8,4,0,240,241,5,34,0,0,241,243,3,12,6,0,242,238,1,0,0,0,242,240,
        1,0,0,0,243,39,1,0,0,0,244,245,5,35,0,0,245,262,3,6,3,0,246,247,
        5,35,0,0,247,262,3,8,4,0,248,249,5,35,0,0,249,262,3,12,6,0,250,251,
        5,35,0,0,251,262,3,14,7,0,252,253,5,36,0,0,253,262,3,6,3,0,254,255,
        5,36,0,0,255,262,3,8,4,0,256,257,5,36,0,0,257,262,3,12,6,0,258,259,
        5,36,0,0,259,262,3,14,7,0,260,262,5,36,0,0,261,244,1,0,0,0,261,246,
        1,0,0,0,261,248,1,0,0,0,261,250,1,0,0,0,261,252,1,0,0,0,261,254,
        1,0,0,0,261,256,1,0,0,0,261,258,1,0,0,0,261,260,1,0,0,0,262,41,1,
        0,0,0,263,264,5,37,0,0,264,268,3,8,4,0,265,266,5,37,0,0,266,268,
        3,12,6,0,267,263,1,0,0,0,267,265,1,0,0,0,268,43,1,0,0,0,269,281,
        5,38,0,0,270,271,5,38,0,0,271,272,3,8,4,0,272,273,5,13,0,0,273,274,
        5,42,0,0,274,281,1,0,0,0,275,276,5,38,0,0,276,277,3,6,3,0,277,278,
        5,13,0,0,278,279,5,42,0,0,279,281,1,0,0,0,280,269,1,0,0,0,280,270,
        1,0,0,0,280,275,1,0,0,0,281,45,1,0,0,0,282,283,5,39,0,0,283,47,1,
        0,0,0,284,285,5,40,0,0,285,49,1,0,0,0,20,53,55,60,84,87,92,102,133,
        150,167,175,183,200,216,229,236,242,261,267,280
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
    RULE_opLabel = 1
    RULE_op = 2
    RULE_num = 3
    RULE_reg = 4
    RULE_offset = 5
    RULE_mem = 6
    RULE_str = 7
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
    RULE_halt = 23
    RULE_nop = 24

    ruleNames =  [ "program", "opLabel", "op", "num", "reg", "offset", "mem", 
                   "str", "move", "add", "sub", "mul", "div", "cmp", "jump", 
                   "call", "ret", "push_op", "pop_op", "input", "print", 
                   "rand", "dump", "halt", "nop" ]

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

        def op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(toy_asmParser.OpContext)
            else:
                return self.getTypedRuleContext(toy_asmParser.OpContext,i)


        def opLabel(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(toy_asmParser.OpLabelContext)
            else:
                return self.getTypedRuleContext(toy_asmParser.OpLabelContext,i)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 53
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [41]:
                        self.state = 50
                        self.match(toy_asmParser.Comment)
                        pass
                    elif token in [43]:
                        self.state = 51
                        self.opLabel()
                        pass
                    elif token in [12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]:
                        self.state = 52
                        self.op()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 57
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [41]:
                self.state = 58
                self.match(toy_asmParser.Comment)
                pass
            elif token in [12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]:
                self.state = 59
                self.op()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 62
            self.match(toy_asmParser.EOF)
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
        self.enterRule(localctx, 2, self.RULE_opLabel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(toy_asmParser.Label)
            self.state = 65
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
        self.enterRule(localctx, 4, self.RULE_op)
        try:
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.move()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.add()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 69
                self.sub()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 4)
                self.state = 70
                self.mul()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 5)
                self.state = 71
                self.div()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 6)
                self.state = 72
                self.cmp()
                pass
            elif token in [19, 20, 21, 22, 23, 24, 25]:
                self.enterOuterAlt(localctx, 7)
                self.state = 73
                self.jump()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 8)
                self.state = 74
                self.call()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 9)
                self.state = 75
                self.ret()
                pass
            elif token in [28, 29, 30]:
                self.enterOuterAlt(localctx, 10)
                self.state = 76
                self.push_op()
                pass
            elif token in [31, 32, 33]:
                self.enterOuterAlt(localctx, 11)
                self.state = 77
                self.pop_op()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 12)
                self.state = 78
                self.input_()
                pass
            elif token in [35, 36]:
                self.enterOuterAlt(localctx, 13)
                self.state = 79
                self.print_()
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 14)
                self.state = 80
                self.rand()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 15)
                self.state = 81
                self.dump()
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 16)
                self.state = 82
                self.halt()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 17)
                self.state = 83
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
        self.enterRule(localctx, 6, self.RULE_num)
        self._la = 0 # Token type
        try:
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2:
                    self.state = 86
                    self.match(toy_asmParser.T__1)


                self.state = 89
                self.match(toy_asmParser.INT)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.match(toy_asmParser.T__2)
                self.state = 91
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
        self.enterRule(localctx, 8, self.RULE_reg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
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
        self.enterRule(localctx, 10, self.RULE_offset)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            _la = self._input.LA(1)
            if not(_la==2 or _la==3):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 97
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
        self.enterRule(localctx, 12, self.RULE_mem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(toy_asmParser.T__9)
            self.state = 100
            self.reg()
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2 or _la==3:
                self.state = 101
                self.offset()


            self.state = 104
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
        self.enterRule(localctx, 14, self.RULE_str)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
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
        self.enterRule(localctx, 16, self.RULE_move)
        try:
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.match(toy_asmParser.T__11)
                self.state = 109
                self.reg()
                self.state = 110
                self.match(toy_asmParser.T__12)
                self.state = 111
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.match(toy_asmParser.T__11)
                self.state = 114
                self.reg()
                self.state = 115
                self.match(toy_asmParser.T__12)
                self.state = 116
                self.reg()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 118
                self.match(toy_asmParser.T__11)
                self.state = 119
                self.reg()
                self.state = 120
                self.match(toy_asmParser.T__12)
                self.state = 121
                self.mem()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 123
                self.match(toy_asmParser.T__11)
                self.state = 124
                self.mem()
                self.state = 125
                self.match(toy_asmParser.T__12)
                self.state = 126
                self.num()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 128
                self.match(toy_asmParser.T__11)
                self.state = 129
                self.mem()
                self.state = 130
                self.match(toy_asmParser.T__12)
                self.state = 131
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
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.match(toy_asmParser.T__13)
                self.state = 136
                self.reg()
                self.state = 137
                self.match(toy_asmParser.T__12)
                self.state = 138
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.match(toy_asmParser.T__13)
                self.state = 141
                self.reg()
                self.state = 142
                self.match(toy_asmParser.T__12)
                self.state = 143
                self.reg()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 145
                self.match(toy_asmParser.T__13)
                self.state = 146
                self.reg()
                self.state = 147
                self.match(toy_asmParser.T__12)
                self.state = 148
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
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.match(toy_asmParser.T__14)
                self.state = 153
                self.reg()
                self.state = 154
                self.match(toy_asmParser.T__12)
                self.state = 155
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.match(toy_asmParser.T__14)
                self.state = 158
                self.reg()
                self.state = 159
                self.match(toy_asmParser.T__12)
                self.state = 160
                self.reg()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 162
                self.match(toy_asmParser.T__14)
                self.state = 163
                self.reg()
                self.state = 164
                self.match(toy_asmParser.T__12)
                self.state = 165
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
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.match(toy_asmParser.T__15)
                self.state = 170
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
                self.match(toy_asmParser.T__15)
                self.state = 172
                self.reg()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 173
                self.match(toy_asmParser.T__15)
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
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.match(toy_asmParser.T__16)
                self.state = 178
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.match(toy_asmParser.T__16)
                self.state = 180
                self.reg()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 181
                self.match(toy_asmParser.T__16)
                self.state = 182
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
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.match(toy_asmParser.T__17)
                self.state = 186
                self.reg()
                self.state = 187
                self.match(toy_asmParser.T__12)
                self.state = 188
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self.match(toy_asmParser.T__17)
                self.state = 191
                self.reg()
                self.state = 192
                self.match(toy_asmParser.T__12)
                self.state = 193
                self.reg()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 195
                self.match(toy_asmParser.T__17)
                self.state = 196
                self.reg()
                self.state = 197
                self.match(toy_asmParser.T__12)
                self.state = 198
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
            self.state = 216
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.match(toy_asmParser.T__18)
                self.state = 203
                self.match(toy_asmParser.Label)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.match(toy_asmParser.T__19)
                self.state = 205
                self.match(toy_asmParser.Label)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 206
                self.match(toy_asmParser.T__20)
                self.state = 207
                self.match(toy_asmParser.Label)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 4)
                self.state = 208
                self.match(toy_asmParser.T__21)
                self.state = 209
                self.match(toy_asmParser.Label)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 5)
                self.state = 210
                self.match(toy_asmParser.T__22)
                self.state = 211
                self.match(toy_asmParser.Label)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 6)
                self.state = 212
                self.match(toy_asmParser.T__23)
                self.state = 213
                self.match(toy_asmParser.Label)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 7)
                self.state = 214
                self.match(toy_asmParser.T__24)
                self.state = 215
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
            self.state = 218
            self.match(toy_asmParser.T__25)
            self.state = 219
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
            self.state = 221
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
        self.enterRule(localctx, 34, self.RULE_push_op)
        try:
            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.match(toy_asmParser.T__27)
                self.state = 224
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 225
                self.match(toy_asmParser.T__27)
                self.state = 226
                self.reg()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 227
                self.match(toy_asmParser.T__28)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 228
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
        self.enterRule(localctx, 36, self.RULE_pop_op)
        try:
            self.state = 236
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.match(toy_asmParser.T__30)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
                self.match(toy_asmParser.T__30)
                self.state = 233
                self.reg()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 234
                self.match(toy_asmParser.T__31)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 235
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
        self.enterRule(localctx, 38, self.RULE_input)
        try:
            self.state = 242
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.match(toy_asmParser.T__33)
                self.state = 239
                self.reg()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
                self.match(toy_asmParser.T__33)
                self.state = 241
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
        self.enterRule(localctx, 40, self.RULE_print)
        try:
            self.state = 261
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                self.match(toy_asmParser.T__34)
                self.state = 245
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 246
                self.match(toy_asmParser.T__34)
                self.state = 247
                self.reg()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 248
                self.match(toy_asmParser.T__34)
                self.state = 249
                self.mem()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 250
                self.match(toy_asmParser.T__34)
                self.state = 251
                self.str_()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 252
                self.match(toy_asmParser.T__35)
                self.state = 253
                self.num()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 254
                self.match(toy_asmParser.T__35)
                self.state = 255
                self.reg()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 256
                self.match(toy_asmParser.T__35)
                self.state = 257
                self.mem()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 258
                self.match(toy_asmParser.T__35)
                self.state = 259
                self.str_()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 260
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
        self.enterRule(localctx, 42, self.RULE_rand)
        try:
            self.state = 267
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.match(toy_asmParser.T__36)
                self.state = 264
                self.reg()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 265
                self.match(toy_asmParser.T__36)
                self.state = 266
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
        self.enterRule(localctx, 44, self.RULE_dump)
        try:
            self.state = 280
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.match(toy_asmParser.T__37)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 270
                self.match(toy_asmParser.T__37)
                self.state = 271
                self.reg()
                self.state = 272
                self.match(toy_asmParser.T__12)
                self.state = 273
                self.match(toy_asmParser.INT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 275
                self.match(toy_asmParser.T__37)
                self.state = 276
                self.num()
                self.state = 277
                self.match(toy_asmParser.T__12)
                self.state = 278
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
        self.enterRule(localctx, 46, self.RULE_halt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
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
        self.enterRule(localctx, 48, self.RULE_nop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(toy_asmParser.T__39)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





