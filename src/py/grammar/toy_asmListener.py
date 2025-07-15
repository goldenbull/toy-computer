# Generated from toy_asm.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .toy_asmParser import toy_asmParser
else:
    from toy_asmParser import toy_asmParser

# This class defines a complete listener for a parse tree produced by toy_asmParser.
class toy_asmListener(ParseTreeListener):

    # Enter a parse tree produced by toy_asmParser#program.
    def enterProgram(self, ctx:toy_asmParser.ProgramContext):
        pass

    # Exit a parse tree produced by toy_asmParser#program.
    def exitProgram(self, ctx:toy_asmParser.ProgramContext):
        pass


    # Enter a parse tree produced by toy_asmParser#opWithLabel.
    def enterOpWithLabel(self, ctx:toy_asmParser.OpWithLabelContext):
        pass

    # Exit a parse tree produced by toy_asmParser#opWithLabel.
    def exitOpWithLabel(self, ctx:toy_asmParser.OpWithLabelContext):
        pass


    # Enter a parse tree produced by toy_asmParser#opLabel.
    def enterOpLabel(self, ctx:toy_asmParser.OpLabelContext):
        pass

    # Exit a parse tree produced by toy_asmParser#opLabel.
    def exitOpLabel(self, ctx:toy_asmParser.OpLabelContext):
        pass


    # Enter a parse tree produced by toy_asmParser#op.
    def enterOp(self, ctx:toy_asmParser.OpContext):
        pass

    # Exit a parse tree produced by toy_asmParser#op.
    def exitOp(self, ctx:toy_asmParser.OpContext):
        pass


    # Enter a parse tree produced by toy_asmParser#num.
    def enterNum(self, ctx:toy_asmParser.NumContext):
        pass

    # Exit a parse tree produced by toy_asmParser#num.
    def exitNum(self, ctx:toy_asmParser.NumContext):
        pass


    # Enter a parse tree produced by toy_asmParser#reg.
    def enterReg(self, ctx:toy_asmParser.RegContext):
        pass

    # Exit a parse tree produced by toy_asmParser#reg.
    def exitReg(self, ctx:toy_asmParser.RegContext):
        pass


    # Enter a parse tree produced by toy_asmParser#offset.
    def enterOffset(self, ctx:toy_asmParser.OffsetContext):
        pass

    # Exit a parse tree produced by toy_asmParser#offset.
    def exitOffset(self, ctx:toy_asmParser.OffsetContext):
        pass


    # Enter a parse tree produced by toy_asmParser#mem.
    def enterMem(self, ctx:toy_asmParser.MemContext):
        pass

    # Exit a parse tree produced by toy_asmParser#mem.
    def exitMem(self, ctx:toy_asmParser.MemContext):
        pass


    # Enter a parse tree produced by toy_asmParser#str.
    def enterStr(self, ctx:toy_asmParser.StrContext):
        pass

    # Exit a parse tree produced by toy_asmParser#str.
    def exitStr(self, ctx:toy_asmParser.StrContext):
        pass


    # Enter a parse tree produced by toy_asmParser#move.
    def enterMove(self, ctx:toy_asmParser.MoveContext):
        pass

    # Exit a parse tree produced by toy_asmParser#move.
    def exitMove(self, ctx:toy_asmParser.MoveContext):
        pass


    # Enter a parse tree produced by toy_asmParser#add.
    def enterAdd(self, ctx:toy_asmParser.AddContext):
        pass

    # Exit a parse tree produced by toy_asmParser#add.
    def exitAdd(self, ctx:toy_asmParser.AddContext):
        pass


    # Enter a parse tree produced by toy_asmParser#sub.
    def enterSub(self, ctx:toy_asmParser.SubContext):
        pass

    # Exit a parse tree produced by toy_asmParser#sub.
    def exitSub(self, ctx:toy_asmParser.SubContext):
        pass


    # Enter a parse tree produced by toy_asmParser#mul.
    def enterMul(self, ctx:toy_asmParser.MulContext):
        pass

    # Exit a parse tree produced by toy_asmParser#mul.
    def exitMul(self, ctx:toy_asmParser.MulContext):
        pass


    # Enter a parse tree produced by toy_asmParser#div.
    def enterDiv(self, ctx:toy_asmParser.DivContext):
        pass

    # Exit a parse tree produced by toy_asmParser#div.
    def exitDiv(self, ctx:toy_asmParser.DivContext):
        pass


    # Enter a parse tree produced by toy_asmParser#cmp.
    def enterCmp(self, ctx:toy_asmParser.CmpContext):
        pass

    # Exit a parse tree produced by toy_asmParser#cmp.
    def exitCmp(self, ctx:toy_asmParser.CmpContext):
        pass


    # Enter a parse tree produced by toy_asmParser#jump.
    def enterJump(self, ctx:toy_asmParser.JumpContext):
        pass

    # Exit a parse tree produced by toy_asmParser#jump.
    def exitJump(self, ctx:toy_asmParser.JumpContext):
        pass


    # Enter a parse tree produced by toy_asmParser#call.
    def enterCall(self, ctx:toy_asmParser.CallContext):
        pass

    # Exit a parse tree produced by toy_asmParser#call.
    def exitCall(self, ctx:toy_asmParser.CallContext):
        pass


    # Enter a parse tree produced by toy_asmParser#ret.
    def enterRet(self, ctx:toy_asmParser.RetContext):
        pass

    # Exit a parse tree produced by toy_asmParser#ret.
    def exitRet(self, ctx:toy_asmParser.RetContext):
        pass


    # Enter a parse tree produced by toy_asmParser#push_op.
    def enterPush_op(self, ctx:toy_asmParser.Push_opContext):
        pass

    # Exit a parse tree produced by toy_asmParser#push_op.
    def exitPush_op(self, ctx:toy_asmParser.Push_opContext):
        pass


    # Enter a parse tree produced by toy_asmParser#pop_op.
    def enterPop_op(self, ctx:toy_asmParser.Pop_opContext):
        pass

    # Exit a parse tree produced by toy_asmParser#pop_op.
    def exitPop_op(self, ctx:toy_asmParser.Pop_opContext):
        pass


    # Enter a parse tree produced by toy_asmParser#input.
    def enterInput(self, ctx:toy_asmParser.InputContext):
        pass

    # Exit a parse tree produced by toy_asmParser#input.
    def exitInput(self, ctx:toy_asmParser.InputContext):
        pass


    # Enter a parse tree produced by toy_asmParser#print.
    def enterPrint(self, ctx:toy_asmParser.PrintContext):
        pass

    # Exit a parse tree produced by toy_asmParser#print.
    def exitPrint(self, ctx:toy_asmParser.PrintContext):
        pass


    # Enter a parse tree produced by toy_asmParser#rand.
    def enterRand(self, ctx:toy_asmParser.RandContext):
        pass

    # Exit a parse tree produced by toy_asmParser#rand.
    def exitRand(self, ctx:toy_asmParser.RandContext):
        pass


    # Enter a parse tree produced by toy_asmParser#dump.
    def enterDump(self, ctx:toy_asmParser.DumpContext):
        pass

    # Exit a parse tree produced by toy_asmParser#dump.
    def exitDump(self, ctx:toy_asmParser.DumpContext):
        pass


    # Enter a parse tree produced by toy_asmParser#pause.
    def enterPause(self, ctx:toy_asmParser.PauseContext):
        pass

    # Exit a parse tree produced by toy_asmParser#pause.
    def exitPause(self, ctx:toy_asmParser.PauseContext):
        pass


    # Enter a parse tree produced by toy_asmParser#halt.
    def enterHalt(self, ctx:toy_asmParser.HaltContext):
        pass

    # Exit a parse tree produced by toy_asmParser#halt.
    def exitHalt(self, ctx:toy_asmParser.HaltContext):
        pass


    # Enter a parse tree produced by toy_asmParser#nop.
    def enterNop(self, ctx:toy_asmParser.NopContext):
        pass

    # Exit a parse tree produced by toy_asmParser#nop.
    def exitNop(self, ctx:toy_asmParser.NopContext):
        pass



del toy_asmParser