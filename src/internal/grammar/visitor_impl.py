# -*- coding: utf-8 -*-

from .toy_asmParser import toy_asmParser
from .toy_asmVisitor import toy_asmVisitor
from ..computer.op_base import OpLabel
from ..computer.operations import *
from ..computer.operand import OperandType, Operand


class VisitorImpl(toy_asmVisitor):
    def __init__(self):
        self.ops_and_labels: list[OpBase | OpLabel] = []

    def visitNum(self, ctx: toy_asmParser.NumContext):
        """Visit a number and return an Imm operand."""
        return Operand(OperandType.Imm, immVal=int(ctx.getText()))

    def visitReg(self, ctx: toy_asmParser.RegContext):
        """Visit a register and return a Reg operand."""
        return Operand(OperandType.Reg, reg=ctx.getText())

    def visitMem(self, ctx: toy_asmParser.MemContext):
        """Visit a memory reference and return a Mem operand."""
        reg = ctx.children[1].getText()
        if len(ctx.children) == 3:
            offset = 0
        else:
            offset = int(ctx.children[2].getText())
        return Operand(OperandType.Mem, reg=reg, offset=offset)

    def visitStr(self, ctx: toy_asmParser.StrContext):
        """Visit a string literal and return a Str operand."""
        s = ctx.getText()
        # s is the repr form of the str shown in source code editor
        # we also need it's runtime form
        return Operand(OperandType.Str, text=[s, eval(s)])

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
        action = ctx.children[0].getText()
        label = ctx.children[1].getText()
        return Jump(action, label, ctx.stop.line)

    def visitCall(self, ctx: toy_asmParser.CallContext):
        label = ctx.children[1].getText()
        return Call(label, ctx.stop.line)

    def visitRet(self, ctx: toy_asmParser.RetContext):
        return Ret()

    def visitPush(self, ctx: toy_asmParser.PushContext):
        action = ctx.children[0].getText()
        if len(ctx.children) == 2:
            p1 = self.visit(ctx.children[1])
        else:
            p1 = None
        return Push(action, p1)

    def visitPop(self, ctx: toy_asmParser.PopContext):
        action = ctx.children[0].getText()
        if len(ctx.children) == 2:
            p1 = self.visit(ctx.children[1])
        else:
            p1 = None
        return Pop(action, p1)

    def visitInput(self, ctx: toy_asmParser.InputContext):
        p1 = self.visit(ctx.children[1])
        return Input(p1)

    def visitPrint(self, ctx: toy_asmParser.PrintContext):
        action = ctx.children[0].getText()
        if len(ctx.children) == 2:
            p1 = self.visit(ctx.children[1])
        else:
            p1 = None
        return Print(action, p1)

    # def visitDump(self, ctx: toy_asmParser.DumpContext):
    #     if len(ctx.children) > 1:
    #         p1 = self.visit(ctx.children[1])
    #         n = int(ctx.children[3].getText())
    #         return Dump(p1, n)
    #     else:
    #         return Dump()

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
        self.ops_and_labels.append(OpLabel(ctx.start.line, label))

    def visitOp(self, ctx: toy_asmParser.OpContext):
        op = self.visit(ctx.children[0])

        assert isinstance(op, OpBase)
        self.ops_and_labels.append(op)
