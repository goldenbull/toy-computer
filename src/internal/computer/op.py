# -*- coding: utf-8 -*-

from abc import ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .state import ComputerState
    from .operand import Operand


class Op(ABC):
    """
    Base class for all assembly operations.
    Each operation can execute itself and modify the computer state.
    """
    addr: int = 0  # Address (line number) of this operation
    labels: list[str] = []  # Labels pointing to this operation
    computer_state: 'ComputerState' = None  # Reference to state

    def execute(self):
        """
        Execute this operation using self.computer_state.
        Must be implemented by subclasses.
        """
        raise NotImplementedError("由子类实现")

    def to_str(self):
        """Convert operation to string with labels."""
        ret = ""
        for l in self.labels:
            ret += f"{l}:\n"
        ret += f"<{self.addr}> {self.__repr__()}"
        return ret
