# -*- coding: utf-8 -*-

from abc import ABC
from enum import Enum


class ComputerState(Enum):
    Running = 0
    Finished = 1
    Error = 2


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
    labels: list[str] = []
    c = None

    def execute(self):
        raise NotImplementedError("由子类实现")

    def to_str(self):
        ret = ""
        for l in self.labels:
            ret += f"{l}:\n"
        ret += f"<{self.addr}> {self.__repr__()}"
        return ret

    def get_value(self, p):
        if p is None:
            v = ""
        elif isinstance(p, int) or isinstance(p, str):
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
