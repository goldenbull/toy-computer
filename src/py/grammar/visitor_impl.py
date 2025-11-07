# -*- coding: utf-8 -*-

from .toy_asmParser import toy_asmParser
from .toy_asmVisitor import toy_asmVisitor
from computer.operations import *


class VisitorImpl(toy_asmVisitor):
    ops_and_labels: list[Op | str] = []

    def visitNum(self, ctx: toy_asmParser.NumContext):
        return int(ctx.getText())

    def visitReg(self, ctx: toy_asmParser.RegContext):
        return Reg(ctx.getText())

    def visitMem(self, ctx: toy_asmParser.MemContext):
        reg = ctx.children[1].getText()
        if len(ctx.children) == 3:
            offset = 0
        else:
            offset = int(ctx.children[2].getText())
        return Mem(reg, offset)

    def visitStr(self, ctx: toy_asmParser.StrContext):
        s = ctx.getText()
        return s.encode('utf-8').decode('unicode_escape')[1:-1]

    def visitMove(self, ctx: toy_asmParser.MoveContext):
        p1 = self.visit(ctx.children[1])
        p2 = self.visit(ctx.children[3])
        return Move(p1, p2)

    def visitAdd(self, ctx: toy_asmParser.AddContext):
        p1 = self.visit(ctx.children[1])
        p2 = self.visit(ctx.children[3])
        return Add(p1, p2)

    def visitSub(self, ctx: toy_asmParser.SubContext):
        p1 = self.visit(ctx.children[1])
        p2 = self.visit(ctx.children[3])
        return Sub(p1, p2)

    def visitMul(self, ctx: toy_asmParser.MulContext):
        p1 = self.visit(ctx.children[1])
        return Mul(p1)

    def visitDiv(self, ctx: toy_asmParser.DivContext):
        p1 = self.visit(ctx.children[1])
        return Div(p1)

    def visitCmp(self, ctx: toy_asmParser.CmpContext):
        p1 = self.visit(ctx.children[1])
        p2 = self.visit(ctx.children[3])
        return Cmp(p1, p2)

    def visitJump(self, ctx: toy_asmParser.JumpContext):
        act = ctx.children[0].getText()
        label = ctx.children[1].getText()
        return Jump(act, label)

    def visitCall(self, ctx: toy_asmParser.CallContext):
        label = ctx.children[1].getText()
        return Call(label)

    def visitRet(self, ctx: toy_asmParser.RetContext):
        return Ret()

    def visitPush(self, ctx: toy_asmParser.PushContext):
        act = ctx.children[0].getText()
        if len(ctx.children) == 2:
            p1 = self.visit(ctx.children[1])
        else:
            p1 = None
        return Push(act, p1)

    def visitPop(self, ctx: toy_asmParser.PopContext):
        act = ctx.children[0].getText()
        if len(ctx.children) == 2:
            p1 = self.visit(ctx.children[1])
        else:
            p1 = None
        return Pop(act, p1)

    def visitInput(self, ctx: toy_asmParser.InputContext):
        p1 = self.visit(ctx.children[1])
        return Input(p1)

    def visitPrint(self, ctx: toy_asmParser.PrintContext):
        act = ctx.children[0].getText()
        if len(ctx.children) == 2:
            p1 = self.visit(ctx.children[1])
        else:
            p1 = None
        return Print(act, p1)

    def visitDump(self, ctx: toy_asmParser.DumpContext):
        if len(ctx.children) > 1:
            p1 = self.visit(ctx.children[1])
            n = int(ctx.children[3].getText())
            return Dump(p1, n)
        else:
            return Dump()

    def visitPause(self, ctx: toy_asmParser.PauseContext):
        return Pause()

    def visitHalt(self, ctx: toy_asmParser.HaltContext):
        return Halt()

    def visitNop(self, ctx: toy_asmParser.NopContext):
        return Nop()

    def visitRand(self, ctx: toy_asmParser.RandContext):
        p1 = self.visit(ctx.children[1])
        return Rand(p1)

    def visitOpLabel(self, ctx: toy_asmParser.OpLabelContext):
        label = ctx.children[0].getText().strip()
        self.ops_and_labels.append(label)

    def visitOp(self, ctx: toy_asmParser.OpContext):
        op = self.visit(ctx.children[0])

        assert isinstance(op, Op)
        self.ops_and_labels.append(op)
