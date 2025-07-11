# -*- coding: utf-8 -*-

import numpy.random as rnd
from abc import ABC
from .computer import Computer, ComputerState


class OpError(Exception):
    def __init__(self, op, message):
        self.op = op
        self.message = message


class DivZeroError(Exception):
    pass


class MemError(Exception):
    def __init__(self, op, addr: int):
        self.op = op
        self.addr = addr


class Op(ABC):
    addr: int = 0
    label: str = ""

    def execute(self, c: Computer):
        raise NotImplementedError("由子类实现")

    def header(self):
        if self.label:
            return f"{self.label}:\n<{self.addr}>"
        else:
            return f"<{self.addr}>"

    @staticmethod
    def get_value(p, c):
        if isinstance(p, int):
            v = p
        else:
            v = p.value(c)
        return v


class Reg:
    def __init__(self, reg: str):
        self.reg = reg

    def __repr__(self):
        return self.reg

    def value(self, c: Computer):
        return c.get_reg_value(self.reg)


class Mem:
    def __init__(self, reg: str, offset: int):
        self.reg = reg
        self.offset = offset

    def __repr__(self):
        return f"[{self.reg}{self.offset:+}]"

    def addr(self, c: Computer):
        v = c.get_reg_value(self.reg)
        return v + self.offset

    def value(self, c: Computer):
        return c.get_reg_mem_value(self.reg, self.offset)


class Move(Op):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return f"{self.header()} mov {self.p1}, {self.p2}"

    def execute(self, c: Computer):
        try:
            v = self.get_value(self.p2, c)

            if isinstance(self.p1, Reg):
                c.set_reg_value(self.p1.reg, v)
            else:
                c.set_mem_value(self.p1.addr(c), v)

            c.ip += 1
        except IndexError as e:
            c.state = ComputerState.Error
            c.errmsg = f"{self} | {e}"


class Add(Op):
    def __init__(self, p1: Reg, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return f"{self.header()} add {self.p1}, {self.p2}"

    def execute(self, c: Computer):
        try:
            v1 = c.get_reg_value(self.p1.reg)
            v2 = self.get_value(self.p2, c)
            c.set_reg_value(self.p1.reg, v1 + v2)
            c.ip += 1
        except IndexError as e:
            c.state = ComputerState.Error
            c.errmsg = f"{self} | {e}"


class Sub(Op):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return f"{self.header()} sub {self.p1}, {self.p2}"

    def execute(self, c: Computer):
        try:
            v1 = c.get_reg_value(self.p1.reg)
            v2 = self.get_value(self.p2, c)
            c.set_reg_value(self.p1.reg, v1 - v2)
            c.ip += 1
        except IndexError as e:
            c.state = ComputerState.Error
            c.errmsg = f"{self} | {e}"


class Mul(Op):
    def __init__(self, p1):
        self.p1 = p1

    def __repr__(self):
        return f"{self.header()} mul {self.p1}"

    def execute(self, c: Computer):
        try:
            v1 = c.get_reg_value("ax")
            v2 = self.get_value(self.p1, c)
            c.set_reg_value("ax", v1 * v2)
            c.ip += 1
        except IndexError as e:
            c.state = ComputerState.Error
            c.errmsg = f"{self} | {e}"


class Div(Op):
    def __init__(self, p1):
        self.p1 = p1

    def __repr__(self):
        return f"{self.header()} div {self.p1}"

    def execute(self, c: Computer):
        try:
            # 需要处理除0的情况
            v1 = c.get_reg_value("ax")
            v2 = self.get_value(self.p1, c)
            if v2 == 0:
                raise DivZeroError()
            # 特殊处理向零取整，和C一致
            r1 = int(v1 / v2)
            r2 = v1 - v2 * r1
            c.set_reg_value("ax", r1)
            c.set_reg_value("dx", r2)
            c.ip += 1
        except IndexError as e:
            c.state = ComputerState.Error
            c.errmsg = f"{self} | {e}"
        except DivZeroError:
            c.state = ComputerState.Error
            c.errmsg = f"{self} | div0"


class Cmp(Op):
    def __init__(self, p1: Reg, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return f"{self.header()} cmp {self.p1}, {self.p2}"

    def execute(self, c: Computer):
        try:
            v1 = c.get_reg_value(self.p1.reg)
            v2 = self.get_value(self.p2, c)
            if v1 > v2:
                c.set_reg_value("flg", 1)
            elif v1 == v2:
                c.set_reg_value("flg", 0)
            else:
                c.set_reg_value("flg", -1)
            c.ip += 1
        except IndexError as e:
            c.state = ComputerState.Error
            c.errmsg = f"{self} | {e}"


class Jump(Op):
    def __init__(self, action: str, label: str):
        self.action = action
        self.label = label

    def __repr__(self):
        return f"{self.header()} {self.action} {self.label}"  # TODO: calc addr

    def execute(self, c: Computer):
        c.ip += 1


class Call(Op):
    def __init__(self, label: str):
        self.label = label

    def __repr__(self):
        return f"{self.header()} call {self.label}"  # TODO: calc addr

    def execute(self, c: Computer):
        c.ip += 1


class Ret(Op):
    def __repr__(self):
        return f"{self.header()} ret"  # TODO: calc addr

    def execute(self, c: Computer):
        c.ip += 1


class Push(Op):
    def __init__(self, action: str, p1=None):
        self.action = action
        self.p1 = p1

    def __repr__(self):
        if self.p1 is None:
            return f"{self.header()} {self.action}"
        else:
            return f"{self.header()} {self.action} {self.p1}"

    def execute(self, c: Computer):
        def _push(v):
            sp = c.get_reg_value("sp")
            c.set_mem_value(sp, v)
            c.set_reg_value("sp", sp + 1)

        # 分情况处理
        try:
            if self.action == "push":
                v = self.get_value(self.p1, c)
                _push(v)
            elif self.action == "pushf":
                v = c.get_reg_value("flg")
                _push(v)
            elif self.action == "pusha":
                for r in ["ax", "bx", "cx", "dx", "flg", "bp"]:
                    v = c.get_reg_value(r)
                    _push(v)
            else:
                raise ValueError()
            c.ip += 1
        except IndexError as e:
            c.state = ComputerState.Error
            c.errmsg = f"{self} | {e}"


class Pop(Op):
    def __init__(self, action: str, p1: Reg = None):
        self.action = action
        self.p1 = p1

    def __repr__(self):
        if self.p1 is None:
            return f"{self.header()} {self.action}"
        else:
            return f"{self.header()} {self.action} {self.p1}"

    def execute(self, c: Computer):
        def _pop():
            sp = c.get_reg_value("sp")
            c.set_reg_value("sp", sp - 1)
            return c.get_mem_value(sp - 1)

        # 分情况处理
        try:
            if self.action == "pop":
                v = _pop()
                c.set_reg_value(self.p1.reg, v)
            elif self.action == "popf":
                v = _pop()
                c.set_reg_value("flg", v)
            elif self.action == "popa":
                for r in ["ax", "bx", "cx", "dx", "flg", "bp"]:
                    v = _pop()
                    c.set_reg_value(r, v)
            else:
                raise ValueError()
            c.ip += 1
        except IndexError as e:
            c.state = ComputerState.Error
            c.errmsg = f"{self} | {e}"


class Input(Op):
    def __init__(self, p1):
        self.p1 = p1

    def __repr__(self):
        return f"{self.header()} input {self.p1}"

    def execute(self, c: Computer):
        try:
            s = input(f"Input a number into {self.p1}:")
            v = int(s)
            if isinstance(self.p1, Mem):
                c.set_mem_value(self.p1.addr(c), v)
            elif isinstance(self.p1, Reg):
                c.set_reg_value(self.p1.reg, v)
            else:
                raise ValueError()
            c.ip += 1
        except IndexError as e:
            c.state = ComputerState.Error
            c.errmsg = f"{self} | {e}"
        except ValueError as e:
            c.state = ComputerState.Error
            c.errmsg = f"{self} | {e}"


class Print(Op):
    def __init__(self, p1):
        self.p1 = p1

    def __repr__(self):
        return f"{self.header()} print {self.p1}"

    def execute(self, c: Computer):
        try:
            v = self.get_value(self.p1, c)
            print(v)
            c.ip += 1
        except IndexError as e:
            c.state = ComputerState.Error
            c.errmsg = f"{self} | {e}"


class Rand(Op):
    def __init__(self, p1):
        self.p1 = p1

    def __repr__(self):
        return f"{self.header()} rand {self.p1}"

    def execute(self, c: Computer):
        try:
            v = rnd.randint(0, 1000)
            if isinstance(self.p1, Mem):
                c.set_mem_value(self.p1.addr(c), v)
            elif isinstance(self.p1, Reg):
                c.set_reg_value(self.p1.reg, v)
            else:
                raise ValueError()
            c.ip += 1
        except IndexError as e:
            c.state = ComputerState.Error
            c.errmsg = f"{self} | {e}"


class Dump(Op):
    def __init__(self, reg: Reg = None, n: int = None):
        self.reg = reg
        self.n = n

    def __repr__(self):
        if self.reg is None:
            return f"{self.header()} dump"
        else:
            return f"{self.header()} dump {self.reg}, {self.n}"

    def execute(self, c: Computer):
        print(f"======== {c.state} ========")
        if c.state == ComputerState.Error:
            print(c.errmsg)

        # 通用寄存器
        print(f"ax={c.ax} bx={c.bx} cx={c.cx} dx={c.dx} flg={c.flg}")
        print(f"ip={c.ip} bp={c.bp} sp={c.sp}")

        # 当前指令上下文，各显示5条即可
        print("---- code context ----")
        for i in range(-5, 6):
            idx = c.ip + i
            if 0 <= idx < len(c.ops):
                print(c.ops[idx], end="")
                if i == 0:
                    print(" <===")
                else:
                    print()

        # 显示内存，每行显示16个数
        if self.reg is not None:
            print("---- memory ----")
            if self.n < 0:
                c.state = ComputerState.Error
                c.errmsg = f"{self} <== dump的参数不能小于0"
                return

            idx0 = c.get_reg_value(self.reg.reg)
            if idx0 < 0 or idx0 >= c.MEM_SIZE:
                c.state = ComputerState.Error
                c.errmsg = f"{self.reg}={idx0} 超出内存范围"
                return

            for i in range(0, self.n):
                idx = idx0 + i
                if i % 16 == 0:
                    print(f"{idx:4d}: ", end="")
                if idx < c.MEM_SIZE:
                    print(f"{c.mem[idx]:8d}", end="\n" if i % 16 == 15 else " ")
            print()

        c.ip += 1


class Pause(Op):
    def __repr__(self):
        return f"{self.header()} pause"

    def execute(self, c: Computer):
        input("press enter to continue...")
