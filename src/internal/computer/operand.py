# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .state import ComputerState


class Operand(ABC):
    """
    Base class for all operand types in assembly instructions.

    Operands can be:
    - Register (Reg): ax, bx, cx, dx, etc.
    - Memory reference (Mem): [reg+offset]
    - Immediate value (Imm): integer constant
    - String literal (Str): for print operations
    """

    @abstractmethod
    def value(self, state: 'ComputerState') -> int | str:
        """
        Get the value of this operand.

        Args:
            state: ComputerState to read from

        Returns:
            The value (int for most operands, str for string literals)
        """
        pass

    @abstractmethod
    def __repr__(self) -> str:
        """String representation of the operand."""
        pass


class Reg(Operand):
    """Register operand (e.g., ax, bx, cx, dx, sp, bp)."""

    def __init__(self, reg: str):
        self.reg = reg

    def __repr__(self):
        return self.reg

    def value(self, state: 'ComputerState') -> int:
        return state.get_reg_value(self.reg)


class Mem(Operand):
    """Memory operand with base register and offset (e.g., [ax+4], [bp-2])."""

    def __init__(self, reg: str, offset: int = 0):
        self.reg = reg
        self.offset = offset

    def __repr__(self):
        if self.offset == 0:
            return f"[{self.reg}]"
        else:
            return f"[{self.reg}{self.offset:+d}]"

    def addr(self, state: 'ComputerState') -> int:
        """Calculate the memory address."""
        v = state.get_reg_value(self.reg)
        return v + self.offset

    def value(self, state: 'ComputerState') -> int:
        return state.get_reg_mem_value(self.reg, self.offset)


class Imm(Operand):
    """Immediate value operand (integer constant)."""

    def __init__(self, val: int):
        self.val = val

    def __repr__(self):
        return str(self.val)

    def value(self, state: 'ComputerState') -> int:
        return self.val


class Str(Operand):
    """String literal operand (for print operations)."""

    def __init__(self, text: str):
        self.text = text

    def __repr__(self):
        return f'"{self.text}"'

    def value(self, state: 'ComputerState') -> str:
        return self.text


# Type alias for any operand type
OperandType = Reg | Mem | Imm | Str
