# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from . import ComputerState, ExecutionState, OpBase


class ExecutorBase(ABC):
    """
    Computer executor that manages the execution of assembly programs.
    Separated from ComputerState to decouple execution logic from state management.
    """

    def __init__(self, ops_and_labels: list, step_mode: bool):
        # 为加载的指令生成序号
        ops = [x for x in ops_and_labels if isinstance(x, OpBase)]

        # Create the computer state
        self.state = ComputerState(ops)

        # Set up instruction addresses, state reference, and executor reference
        for i, op in enumerate(self.state.ops):
            op.addr = i
            op.computer_state = self.state
            op.executor = self

        # 所有label归属到下一条op
        cur_labels = []
        for x in ops_and_labels:
            if isinstance(x, str):
                cur_labels.append(x)
            elif isinstance(x, OpBase):
                # assign all above labels to this op
                x.labels = cur_labels
                cur_labels = []
            else:
                raise ValueError("impossible")
        if len(cur_labels) > 0:
            raise SyntaxError("最后的label没有对应指令")

        # 建立Label和addr的映射表
        for op in self.state.ops:
            for label in op.labels:
                self.state.labels_tbl[label] = op.addr

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
