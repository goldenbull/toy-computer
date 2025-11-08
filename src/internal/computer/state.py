# -*- coding: utf-8 -*-

from enum import Enum


class MemType(Enum):
    """Enum for memory cell type marking (for debugging purposes)."""
    Data = 0
    IP = 1  # Instruction pointer (return address)
    BP = 2  # Base pointer


class ComputerState:
    """
    Represents the complete state of the toy computer, decoupled from I/O.
    Contains all registers, memory, and instructions.
    """
    # Memory size constant
    MEM_SIZE = 1024

    def __init__(self, ops: list):
        """
        Initialize computer state with a list of operations.

        Args:
            ops: List of Op objects (instructions to execute)
        """
        # General-purpose registers
        self.ax = 11111111
        self.bx = 22222222
        self.cx = 33333333
        self.dx = 44444444
        self.flg = 0

        # Special registers
        self.ip = 0  # Instruction pointer
        self.sp = self.MEM_SIZE - 1  # Stack pointer (grows downward)
        self.bp = self.sp  # Base pointer

        # Memory: list of (value, MemType) tuples
        self.mem = [(-99, MemType.Data)] * self.MEM_SIZE

        # Instruction list
        self.ops = ops

        # Execution state (initialized by importing ExecutionState from parent module)
        from . import ExecutionState
        self.execution_state = ExecutionState.Running
        self.errmsg = ""

        # Label mapping (label_name -> instruction_address)
        self.labels_tbl = {}

    def get_reg_value(self, reg: str) -> int:
        """Get value of a register by name."""
        if reg == "ax":
            return self.ax
        elif reg == "bx":
            return self.bx
        elif reg == "cx":
            return self.cx
        elif reg == "dx":
            return self.dx
        elif reg == "flg":
            return self.flg
        elif reg == "ip":
            return self.ip
        elif reg == "bp":
            return self.bp
        elif reg == "sp":
            return self.sp
        else:
            raise ValueError(f"Unknown register: {reg}")

    def set_reg_value(self, reg: str, v: int):
        """Set value of a register by name."""
        if reg == "ax":
            self.ax = v
        elif reg == "bx":
            self.bx = v
        elif reg == "cx":
            self.cx = v
        elif reg == "dx":
            self.dx = v
        elif reg == "flg":
            self.flg = v
        elif reg == "ip":
            self.ip = v
        elif reg == "bp":
            self.bp = v
        elif reg == "sp":
            self.sp = v
        else:
            raise ValueError(f"Unknown register: {reg}")

    def get_mem_value(self, addr: int) -> int:
        """Get value from memory at given address."""
        if addr < 0 or addr >= self.MEM_SIZE:
            raise IndexError(f"addr={addr}, 内存越界")
        return self.mem[addr][0]

    def get_reg_mem_value(self, reg: str, offset: int) -> int:
        """Get value from memory at [reg+offset]."""
        v = self.get_reg_value(reg)
        addr = v + offset
        if addr < 0 or addr >= self.MEM_SIZE:
            raise IndexError(f"{reg}={v}, offset={offset}, addr={addr}, 内存越界")
        return self.mem[addr][0]

    def set_mem_value(self, addr: int, v: int, tp: MemType = MemType.Data):
        """Set value in memory at given address with optional type marker."""
        if addr < 0 or addr >= self.MEM_SIZE:
            raise IndexError(f"addr={addr}, 内存越界")
        self.mem[addr] = (v, tp)

    def push_stack(self, v: int, tp: MemType = MemType.Data):
        """
        Push a value onto the stack.
        Stack grows downward (sp decrements).

        Args:
            v: Value to push
            tp: Memory type marker
        """
        self.set_mem_value(self.sp, v, tp)
        self.sp -= 1

    def pop_stack(self) -> int:
        """
        Pop a value from the stack.
        Stack grows downward (sp increments on pop).

        Returns:
            Value popped from stack
        """
        self.sp += 1
        return self.get_mem_value(self.sp)

    def copy(self):
        """Create a deep copy of the current state for snapshotting."""
        import copy
        return copy.deepcopy(self)
