# -*- coding: utf-8 -*-

from abc import ABC
from .computer import Computer


class Op(ABC):
    addr: int = 0
    label: str = ""

    def execute(self, computer: Computer):
        raise NotImplementedError("由子类实现")

    def header(self):
        if self.label:
            return f"({self.label})<{self.addr}>"
        else:
            return f"<{self.addr}>"


class Reg:
    def __init__(self, reg: str):
        self.reg = reg

    def __repr__(self):
        return self.reg


class Mem:
    def __init__(self, reg: str, offset: int):
        self.reg = reg
        self.offset = offset

    def __repr__(self):
        return f"[{self.reg}{self.offset:+}]"


class Move(Op):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return f"{self.header()} mov {self.p1}, {self.p2}"

    def execute(self, computer: Computer):
        ...


class Add(Op):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return f"{self.header()} add {self.p1}, {self.p2}"

    def execute(self, computer: Computer):
        ...


class Sub(Op):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return f"{self.header()} sub {self.p1}, {self.p2}"

    def execute(self, computer: Computer):
        ...


class Mul(Op):
    def __init__(self, p1):
        self.p1 = p1

    def __repr__(self):
        return f"{self.header()} mul {self.p1}"

    def execute(self, computer: Computer):
        ...


class Div(Op):
    def __init__(self, p1):
        self.p1 = p1

    def __repr__(self):
        return f"{self.header()} div {self.p1}"

    def execute(self, computer: Computer):
        ...


class Cmp(Op):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return f"{self.header()} cmp {self.p1}, {self.p2}"

    def execute(self, computer: Computer):
        ...


class Jump(Op):
    def __init__(self, action: str, label: str):
        self.action = action
        self.label = label

    def __repr__(self):
        return f"{self.header()} {self.action} {self.label}"  # TODO: calc addr

    def execute(self, computer: Computer):
        ...


class Call(Op):
    def __init__(self, label: str):
        self.label = label

    def __repr__(self):
        return f"{self.header()} call {self.label}"  # TODO: calc addr

    def execute(self, computer: Computer):
        ...


class Ret(Op):
    def __repr__(self):
        return f"{self.header()} ret"  # TODO: calc addr

    def execute(self, computer: Computer):
        ...


class Push(Op):
    def __init__(self, action: str, p1=None):
        self.action = action
        self.p1 = p1

    def __repr__(self):
        if self.p1 is None:
            return f"{self.header()} {self.action}"
        else:
            return f"{self.header()} {self.action} {self.p1}"

    def execute(self, computer: Computer):
        ...


class Pop(Op):
    def __init__(self, action: str, p1=None):
        self.action = action
        self.p1 = p1

    def __repr__(self):
        if self.p1 is None:
            return f"{self.header()} {self.action}"
        else:
            return f"{self.header()} {self.action} {self.p1}"

    def execute(self, computer: Computer):
        ...


class Input(Op):
    def __init__(self, p1):
        self.p1 = p1

    def __repr__(self):
        return f"{self.header()} input {self.p1}"

    def execute(self, computer: Computer):
        ...


class Print(Op):
    def __init__(self, p1):
        self.p1 = p1

    def __repr__(self):
        return f"{self.header()} print {self.p1}"

    def execute(self, computer: Computer):
        ...


class Rand(Op):
    def __init__(self, p1):
        self.p1 = p1

    def __repr__(self):
        return f"{self.header()} rand {self.p1}"

    def execute(self, computer: Computer):
        ...


class Dump(Op):
    def __init__(self, p1, n: int):
        self.p1 = p1
        self.n = n

    def __repr__(self):
        return f"{self.header()} dump {self.p1}, {self.n}"

    def execute(self, computer: Computer):
        ...


class Pause(Op):
    def __repr__(self):
        return f"{self.header()} pause"

    def execute(self, computer: Computer):
        ...
