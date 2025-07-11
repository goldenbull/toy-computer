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
    c: Computer = None

    def execute(self):
        raise NotImplementedError("由子类实现")

    def header(self):
        if self.label:
            return f"{self.label}:\n<{self.addr}>"
        else:
            return f"<{self.addr}>"

    def get_value(self, p):
        if isinstance(p, int):
            v = p
        else:
            v = p.value(self.c)
        return v

    def push_stack(self, v):
        sp = self.c.get_reg_value("sp")
        self.c.set_mem_value(sp, v)
        self.c.set_reg_value("sp", sp + 1)

    def pop_stack(self):
        sp = self.c.get_reg_value("sp")
        self.c.set_reg_value("sp", sp - 1)
        return self.c.get_mem_value(sp - 1)


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

    def execute(self):
        try:
            v = self.get_value(self.p2)

            if isinstance(self.p1, Reg):
                self.c.set_reg_value(self.p1.reg, v)
            else:
                self.c.set_mem_value(self.p1.addr(self.c), v)

            self.c.ip += 1
        except IndexError as e:
            self.c.state = ComputerState.Error
            self.c.errmsg = f"{self} | {e}"


class Add(Op):
    def __init__(self, p1: Reg, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return f"{self.header()} add {self.p1}, {self.p2}"

    def execute(self):
        try:
            v1 = self.c.get_reg_value(self.p1.reg)
            v2 = self.get_value(self.p2)
            self.c.set_reg_value(self.p1.reg, v1 + v2)
            self.c.ip += 1
        except IndexError as e:
            self.c.state = ComputerState.Error
            self.c.errmsg = f"{self} | {e}"


class Sub(Op):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return f"{self.header()} sub {self.p1}, {self.p2}"

    def execute(self):
        try:
            v1 = self.c.get_reg_value(self.p1.reg)
            v2 = self.get_value(self.p2)
            self.c.set_reg_value(self.p1.reg, v1 - v2)
            self.c.ip += 1
        except IndexError as e:
            self.c.state = ComputerState.Error
            self.c.errmsg = f"{self} | {e}"


class Mul(Op):
    def __init__(self, p1):
        self.p1 = p1

    def __repr__(self):
        return f"{self.header()} mul {self.p1}"

    def execute(self):
        try:
            v1 = self.c.get_reg_value("ax")
            v2 = self.get_value(self.p1)
            self.c.set_reg_value("ax", v1 * v2)
            self.c.ip += 1
        except IndexError as e:
            self.c.state = ComputerState.Error
            self.c.errmsg = f"{self} | {e}"


class Div(Op):
    def __init__(self, p1):
        self.p1 = p1

    def __repr__(self):
        return f"{self.header()} div {self.p1}"

    def execute(self):
        try:
            # 需要处理除0的情况
            v1 = self.c.get_reg_value("ax")
            v2 = self.get_value(self.p1)
            if v2 == 0:
                raise DivZeroError()
            # 特殊处理向零取整，和C一致
            r1 = int(v1 / v2)
            r2 = v1 - v2 * r1
            self.c.set_reg_value("ax", r1)
            self.c.set_reg_value("dx", r2)
            self.c.ip += 1
        except IndexError as e:
            self.c.state = ComputerState.Error
            self.c.errmsg = f"{self} | {e}"
        except DivZeroError:
            self.c.state = ComputerState.Error
            self.c.errmsg = f"{self} | div0"


class Cmp(Op):
    def __init__(self, p1: Reg, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return f"{self.header()} cmp {self.p1}, {self.p2}"

    def execute(self):
        try:
            v1 = self.c.get_reg_value(self.p1.reg)
            v2 = self.get_value(self.p2)
            if v1 > v2:
                self.c.set_reg_value("flg", 1)
            elif v1 == v2:
                self.c.set_reg_value("flg", 0)
            else:
                self.c.set_reg_value("flg", -1)
            self.c.ip += 1
        except IndexError as e:
            self.c.state = ComputerState.Error
            self.c.errmsg = f"{self} | {e}"


class Jump(Op):
    def __init__(self, action: str, target: str):
        self.action = action
        self.target = target

    def __repr__(self):
        try:
            target_addr = self.c.labels_tbl[self.target]
            return f"{self.header()} {self.action} {self.target} <{target_addr}>"
        except KeyError as e:
            return f"{self.header()} {self.action} {self.target} <ERROR>"

    def execute(self):
        try:
            target_addr = self.c.labels_tbl[self.target]
            flg = self.c.get_reg_value("flg")
            if (self.action == "jmp"
                    or (self.action == "je" and flg == 0)
                    or (self.action == "jne" and flg != 0)
                    or (self.action == "jg" and flg > 0)
                    or (self.action == "jge" and flg >= 0)
                    or (self.action == "jl" and flg < 0)
                    or (self.action == "jle" and flg <= 0)
            ):
                self.c.ip = target_addr
            else:
                self.c.ip += 1
        except KeyError as e:
            self.c.state = ComputerState.Error
            self.c.errmsg = f"{self} | invalid label {e}"


class Call(Op):
    def __init__(self, target: str):
        self.target = target

    def __repr__(self):
        try:
            target_addr = self.c.labels_tbl[self.target]
            return f"{self.header()} call {self.target} <{target_addr}>"
        except KeyError as e:
            return f"{self.header()} call {self.target} <ERROR>"

    def execute(self):
        try:
            # ip入栈，sp+1，jmp到函数入口
            target_addr = self.c.labels_tbl[self.target]
            self.push_stack(self.c.get_reg_value("ip"))
            self.c.ip = target_addr
        except KeyError as e:
            self.c.state = ComputerState.Error
            self.c.errmsg = f"{self} | invalid label {e}"


class Ret(Op):
    def __repr__(self):
        return f"{self.header()} ret"  # TODO 如何显示来时的地址？执行前后sp会变化

    def execute(self):
        try:
            origin_addr = self.pop_stack()
            self.c.ip = origin_addr
        except IndexError as e:
            self.c.state = ComputerState.Error
            self.c.errmsg = f"{self} | {e}"


class Push(Op):
    def __init__(self, action: str, p1=None):
        self.action = action
        self.p1 = p1

    def __repr__(self):
        if self.p1 is None:
            return f"{self.header()} {self.action}"
        else:
            return f"{self.header()} {self.action} {self.p1}"

    def execute(self):
        # 分情况处理
        try:
            if self.action == "push":
                v = self.get_value(self.p1)
                self.push_stack(v)
            elif self.action == "pushf":
                v = self.c.get_reg_value("flg")
                self.push_stack(v)
            elif self.action == "pusha":
                for r in ["ax", "bx", "cx", "dx", "flg", "bp"]:
                    v = self.c.get_reg_value(r)
                    self.push_stack(v)
            else:
                raise ValueError()
            self.c.ip += 1
        except IndexError as e:
            self.c.state = ComputerState.Error
            self.c.errmsg = f"{self} | {e}"


class Pop(Op):
    def __init__(self, action: str, p1: Reg = None):
        self.action = action
        self.p1 = p1

    def __repr__(self):
        if self.p1 is None:
            return f"{self.header()} {self.action}"
        else:
            return f"{self.header()} {self.action} {self.p1}"

    def execute(self):
        # 分情况处理
        try:
            if self.action == "pop":
                v = self.pop_stack()
                self.c.set_reg_value(self.p1.reg, v)
            elif self.action == "popf":
                v = self.pop_stack()
                self.c.set_reg_value("flg", v)
            elif self.action == "popa":
                for r in ["ax", "bx", "cx", "dx", "flg", "bp"]:
                    v = self.pop_stack()
                    self.c.set_reg_value(r, v)
            else:
                raise ValueError()
            self.c.ip += 1
        except IndexError as e:
            self.c.state = ComputerState.Error
            self.c.errmsg = f"{self} | {e}"


class Input(Op):
    def __init__(self, p1):
        self.p1 = p1

    def __repr__(self):
        return f"{self.header()} input {self.p1}"

    def execute(self):
        try:
            s = input(f"Input a number into {self.p1}:")
            v = int(s)
            if isinstance(self.p1, Mem):
                self.c.set_mem_value(self.p1.addr(self.c), v)
            elif isinstance(self.p1, Reg):
                self.c.set_reg_value(self.p1.reg, v)
            else:
                raise ValueError()
            self.c.ip += 1
        except IndexError as e:
            self.c.state = ComputerState.Error
            self.c.errmsg = f"{self} | {e}"
        except ValueError as e:
            self.c.state = ComputerState.Error
            self.c.errmsg = f"{self} | {e}"


class Print(Op):
    def __init__(self, p1):
        self.p1 = p1

    def __repr__(self):
        return f"{self.header()} print {self.p1}"

    def execute(self):
        try:
            v = self.get_value(self.p1)
            print(v)
            self.c.ip += 1
        except IndexError as e:
            self.c.state = ComputerState.Error
            self.c.errmsg = f"{self} | {e}"


class Rand(Op):
    def __init__(self, p1):
        self.p1 = p1

    def __repr__(self):
        return f"{self.header()} rand {self.p1}"

    def execute(self):
        try:
            v = rnd.randint(0, 1000)
            if isinstance(self.p1, Mem):
                self.c.set_mem_value(self.p1.addr(self.c), v)
            elif isinstance(self.p1, Reg):
                self.c.set_reg_value(self.p1.reg, v)
            else:
                raise ValueError()
            self.c.ip += 1
        except IndexError as e:
            self.c.state = ComputerState.Error
            self.c.errmsg = f"{self} | {e}"


class Dump(Op):
    def __init__(self, reg: Reg = None, n: int = None):
        self.reg = reg
        self.n = n

    def __repr__(self):
        if self.reg is None:
            return f"{self.header()} dump"
        else:
            return f"{self.header()} dump {self.reg}, {self.n}"

    def execute(self):
        print(f"======== {self.c.state} ========")
        if self.c.state == ComputerState.Error:
            print(self.c.errmsg)

        # 通用寄存器
        print(f"ax={self.c.ax} bx={self.c.bx} cx={self.c.cx} dx={self.c.dx} flg={self.c.flg}")
        print(f"ip={self.c.ip} bp={self.c.bp} sp={self.c.sp}")

        # 当前指令上下文，各显示5条即可
        print("---- code context ----")
        for i in range(-5, 6):
            idx = self.c.ip + i
            if 0 <= idx < len(self.c.ops):
                print(self.c.ops[idx], end="")
                if i == 0:
                    print(" <===")
                else:
                    print()

        # 显示内存，每行显示16个数
        if self.reg is not None:
            print("---- memory ----")
            if self.n < 0:
                self.c.state = ComputerState.Error
                self.c.errmsg = f"{self} <== dump的参数不能小于0"
                return

            idx0 = self.c.get_reg_value(self.reg.reg)
            if idx0 < 0 or idx0 >= self.c.MEM_SIZE:
                self.c.state = ComputerState.Error
                self.c.errmsg = f"{self.reg}={idx0} 超出内存范围"
                return

            for i in range(0, self.n):
                idx = idx0 + i
                if i % 16 == 0:
                    print(f"{idx:4d}: ", end="")
                if idx < self.c.MEM_SIZE:
                    print(f"{self.c.mem[idx]:8d}", end="\n" if i % 16 == 15 else " ")
            print()

        self.c.ip += 1


class Pause(Op):
    def __repr__(self):
        return f"{self.header()} pause"

    def execute(self):
        input("press enter to continue...")
