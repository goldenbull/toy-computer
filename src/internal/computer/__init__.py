# -*- coding: utf-8 -*-

from enum import Enum


# Global enums
class ExecutionState(Enum):
    """Enum representing the execution state of the computer."""
    Running = 0
    Finished = 1
    Error = 2


# Import core classes from their respective modules
from .state import MemType, ComputerState
from .op_base import OpBase
from .operand import OperandType, Operand


# Exception classes
class OpError(Exception):
    def __init__(self, op: OpBase, message: str):
        self.op = op
        self.message = message


class DivZeroError(Exception):
    pass


class MemError(Exception):
    def __init__(self, op: OpBase, addr: int):
        self.op = op
        self.addr = addr


from .executor_base import ExecutorBase

# Export all public classes
__all__ = [
    'ExecutionState',
    'MemType',
    'ComputerState',
    'OpBase',
    'OperandType',
    'Operand',
    'OpError',
    'DivZeroError',
    'MemError',
    'ExecutorBase',
]
