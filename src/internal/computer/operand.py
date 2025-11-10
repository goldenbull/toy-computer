# -*- coding: utf-8 -*-

from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .state import ComputerState


class OperandType(Enum):
    Reg = 0
    Mem = 1
    Imm = 2
    Str = 3


class Operand:
    reg: str = ""
    offset: int = 0
    immVal: int = 0
    text: str = ""

    def __init__(self, tp: OperandType, reg: str = "", offset: int = 0, immVal: int = 0, text: str = ""):
        self.tp = tp
        self.reg = reg
        self.offset = offset
        self.immVal = immVal
        self.text = text

    def mem_addr(self, state: 'ComputerState'):
        if self.tp != OperandType.Mem:
            raise TypeError("Operand type must be Mem")
        v = state.get_reg_value(self.reg)
        return v + self.offset

    def value(self, state: 'ComputerState') -> int | str:
        if self.tp == OperandType.Reg:
            return state.get_reg_value(self.reg)
        elif self.tp == OperandType.Mem:
            return state.get_reg_mem_value(self.reg, self.offset)
        elif self.tp == OperandType.Imm:
            return self.immVal
        elif self.tp == OperandType.Str:
            return self.text
        else:
            raise TypeError(f"invalid Operand type:{self.tp}")

    def __repr__(self):
        if self.tp == OperandType.Reg:
            return self.reg
        elif self.tp == OperandType.Mem:
            if self.offset == 0:
                return f"[{self.reg}]"
            else:
                return f"[{self.reg}{self.offset:+d}]"
        elif self.tp == OperandType.Imm:
            return str(self.immVal)
        elif self.tp == OperandType.Str:
            return f'"{self.text}"'
        else:
            raise TypeError(f"invalid Operand type:{self.tp}")
