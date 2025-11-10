# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from . import ComputerState, ExecutionState


class ExecutorBase(ABC):
    """
    Computer executor that manages the execution of assembly programs.
    Separated from ComputerState to decouple execution logic from state management.
    """

    def __init__(self, content: str, step_mode: bool):
        # Compile the source code
        from ..grammar.compiler import Compiler
        compiled = Compiler.compile(content)

        # Create the computer state
        self.state = ComputerState(compiled.ops)
        self.state.labels_tbl = compiled.labels_tbl

        # Set up state reference and executor reference for each operation
        for op in self.state.ops:
            op.computer_state = self.state
            op.executor = self

        # 逐步执行模式
        self.step_mode = step_mode

    def run(self):
        """
        Execute the program. Base implementation without I/O.
        Subclasses should override this to add I/O and debugging features.
        """
        while True:
            next_ip = self.state.ip
            if next_ip < 0:
                self.state.execution_state = ExecutionState.Error
                self.state.errmsg = f"next ip={next_ip} 异常终止"
                break
            if next_ip >= len(self.state.ops) or self.state.execution_state == ExecutionState.Finished:
                self.state.execution_state = ExecutionState.Finished
                break

            op = self.state.ops[next_ip]
            op.execute()

            if self.state.execution_state == ExecutionState.Error:
                break

    # Abstract methods for I/O operations that subclasses must implement
    @abstractmethod
    def handle_input(self, target_operand):
        """
        Handle input operation.

        Args:
            target_operand: The operand (Reg or Mem) to store the input value
        """
        pass

    @abstractmethod
    def handle_print(self, value: str, newline: bool):
        """
        Handle print operation.

        Args:
            value: The value to print (already converted to string)
            newline: Whether to print a newline after the value
        """
        pass

    @abstractmethod
    def handle_dump(self, mem_start_idx, mem_count: int):
        """
        Handle dump operation (display registers and memory).

        Args:
            mem_start_idx: Starting memory address to display (None to skip memory)
            mem_count: Number of memory cells to display
        """
        pass

    @abstractmethod
    def handle_pause(self):
        """Handle pause operation (wait for user input to continue)."""
        pass
