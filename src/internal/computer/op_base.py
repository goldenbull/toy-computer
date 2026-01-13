# -*- coding: utf-8 -*-

import dataclasses
from abc import ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .state import ComputerState
    from .operand import Operand
    from .executor_base import ExecutorBase


@dataclasses.dataclass
class OpLabel:
    src_line: int  # line no. in source code, to provide better compiler error message
    label: str


class OpBase(ABC):
    """
    Base class for all assembly operations.
    Each operation can execute itself and modify the computer state.
    """
    addr: int = 0  # Address (line number) of this operation
    op_labels: list[OpLabel] = []  # Labels pointing to this operation
    computer_state: 'ComputerState' = None  # Reference to state
    executor: 'ExecutorBase' = None  # Reference to executor for I/O operations

    p1: 'Operand' = None
    p2: 'Operand' = None

    action: str = None  # for jmp/jne/...  push/pushf print/println etc.
    target: str = None  # for jmp and call

    def execute(self):
        """
        Execute this operation using self.computer_state.
        Must be implemented by subclasses.
        """
        raise NotImplementedError("由子类实现")

    def to_str(self):
        """Convert operation to string with labels."""
        ret = ""
        for ol in self.op_labels:
            ret += f"{ol.label}:\n"
        ret += f"<{self.addr}> {self.__repr__()}"
        return ret
