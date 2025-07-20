# -*- coding: utf-8 -*-

import numpy.random as rnd
from . import ComputerState, Op, DivZeroError
from .computer import Computer


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
        return f"mov {self.p1}, {self.p2}"

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
        return f"add {self.p1}, {self.p2}"

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
        return f"sub {self.p1}, {self.p2}"

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
        return f"mul {self.p1}"

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
        return f"div {self.p1}"

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
        return f"cmp {self.p1}, {self.p2}"

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
            return f"{self.action} {self.target} ({target_addr - self.addr:+d})"
        except KeyError as e:
            return f"{self.action} {self.target} <ERROR>"

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
            return f"call {self.target} <{target_addr}>"
        except KeyError as e:
            return f"call {self.target} <ERROR>"

    def execute(self):
        try:
            # ip入栈，sp+1，jmp到函数入口
            target_addr = self.c.labels_tbl[self.target]
            self.push_stack(self.c.ip + 1)  # 返回的位置应该是下一条指令
            self.c.ip = target_addr
        except KeyError as e:
            self.c.state = ComputerState.Error
            self.c.errmsg = f"{self} | invalid label {e}"


class Ret(Op):
    def __repr__(self):
        return f"ret"  # TODO 如何显示来时的地址？执行前后sp会变化

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
            return f"{self.action}"
        else:
            return f"{self.action} {self.p1}"

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
            return f"{self.action}"
        else:
            return f"{self.action} {self.p1}"

    def execute(self):
        # 分情况处理
        try:
            if self.action == "pop":
                v = self.pop_stack()
                if self.p1 is not None:
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
        return f"input {self.p1}"

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
    def __init__(self, act, p1):
        self.act = act
        self.p1 = p1

    def __repr__(self):
        return f"{self.act} {self.p1}"

    def execute(self):
        try:
            v = self.get_value(self.p1)
            print(v, end="" if self.act == "print" else "\n")
            self.c.ip += 1
        except IndexError as e:
            self.c.state = ComputerState.Error
            self.c.errmsg = f"{self} | {e}"


class Rand(Op):
    def __init__(self, p1):
        self.p1 = p1

    def __repr__(self):
        return f"rand {self.p1}"

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
    def __init__(self, p1=None, n: int = None):
        self.p1 = p1
        self.n = n

    def __repr__(self):
        if self.p1 is None:
            return f"dump"
        else:
            return f"dump {self.p1}, {self.n}"

    def execute(self):
        # 检查参数合法性
        if self.p1 is not None:
            if self.n < 0:
                self.c.state = ComputerState.Error
                self.c.errmsg = f"{self} <== dump的参数不能小于0"
                return

            idx0 = self.get_value(self.p1)
            if idx0 < 0 or idx0 >= self.c.MEM_SIZE:
                self.c.state = ComputerState.Error
                self.c.errmsg = f"{self.p1}={idx0} 超出内存范围"
                return
        else:
            idx0 = None

        self.c.ip += 1
        self.c.dump(idx0, self.n)
        # 避免两次回车
        if not self.c.step_mode:
            input("按回车继续执行后续指令")


class Halt(Op):
    def __repr__(self):
        return f"halt"

    def execute(self):
        self.c.state = ComputerState.Finished


class Nop(Op):
    def __repr__(self):
        return f"nop"

    def execute(self):
        self.c.ip += 1
