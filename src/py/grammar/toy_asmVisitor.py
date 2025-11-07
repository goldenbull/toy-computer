# Generated from toy_asm.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .toy_asmParser import toy_asmParser
else:
    from toy_asmParser import toy_asmParser

# This class defines a complete generic visitor for a parse tree produced by toy_asmParser.

class toy_asmVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by toy_asmParser#program.
    def visitProgram(self, ctx:toy_asmParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by toy_asmParser#opLabel.
    def visitOpLabel(self, ctx:toy_asmParser.OpLabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by toy_asmParser#op.
    def visitOp(self, ctx:toy_asmParser.OpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by toy_asmParser#num.
    def visitNum(self, ctx:toy_asmParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by toy_asmParser#reg.
    def visitReg(self, ctx:toy_asmParser.RegContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by toy_asmParser#offset.
    def visitOffset(self, ctx:toy_asmParser.OffsetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by toy_asmParser#mem.
    def visitMem(self, ctx:toy_asmParser.MemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by toy_asmParser#move.
    def visitMove(self, ctx:toy_asmParser.MoveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by toy_asmParser#add.
    def visitAdd(self, ctx:toy_asmParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by toy_asmParser#sub.
    def visitSub(self, ctx:toy_asmParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by toy_asmParser#mul.
    def visitMul(self, ctx:toy_asmParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by toy_asmParser#div.
    def visitDiv(self, ctx:toy_asmParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by toy_asmParser#cmp.
    def visitCmp(self, ctx:toy_asmParser.CmpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by toy_asmParser#jump.
    def visitJump(self, ctx:toy_asmParser.JumpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by toy_asmParser#call.
    def visitCall(self, ctx:toy_asmParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by toy_asmParser#ret.
    def visitRet(self, ctx:toy_asmParser.RetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by toy_asmParser#push.
    def visitPush(self, ctx:toy_asmParser.PushContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by toy_asmParser#pop.
    def visitPop(self, ctx:toy_asmParser.PopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by toy_asmParser#input.
    def visitInput(self, ctx:toy_asmParser.InputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by toy_asmParser#str.
    def visitStr(self, ctx:toy_asmParser.StrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by toy_asmParser#print.
    def visitPrint(self, ctx:toy_asmParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by toy_asmParser#rand.
    def visitRand(self, ctx:toy_asmParser.RandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by toy_asmParser#dump.
    def visitDump(self, ctx:toy_asmParser.DumpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by toy_asmParser#pause.
    def visitPause(self, ctx:toy_asmParser.PauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by toy_asmParser#halt.
    def visitHalt(self, ctx:toy_asmParser.HaltContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by toy_asmParser#nop.
    def visitNop(self, ctx:toy_asmParser.NopContext):
        return self.visitChildren(ctx)



del toy_asmParser