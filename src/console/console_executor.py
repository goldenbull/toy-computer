# -*- coding: utf-8 -*-

from internal.computer.executor_base import ExecutorBase, ExecutionState
from internal.computer.operations import Dump, Pause, Input, Reg, Mem


class ConsoleExecutor(ExecutorBase):
    """
    Console-based executor with terminal I/O.
    Extends ExecutorBase to add console-specific functionality for debugging operations.
    """

    def run(self):
        """Execute the program with console I/O support."""
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

            # Handle console-specific operations before execution
            if isinstance(op, Dump):
                self._handle_dump(op)
            elif isinstance(op, Pause):
                self._handle_pause(op)
            elif isinstance(op, Input):
                self._handle_input(op)
            else:
                # Execute normal operation
                op.execute()

            # Step mode: dump after each instruction
            if self.step_mode:
                self.dump(self.state.sp // 64 * 64, 64)
                input("step模式，按回车继续执行下一条指令")

            if self.state.execution_state == ExecutionState.Error:
                print(f"系统错误: {self.state.errmsg}")
                break

        if self.state.execution_state == ExecutionState.Finished:
            print("====== finished ======")
        else:
            print(self.state.errmsg)

    def _handle_dump(self, op: Dump):
        """Handle dump operation with console output."""
        # Check parameters
        if op.p1 is not None:
            if op.n < 0:
                self.state.execution_state = ExecutionState.Error
                self.state.errmsg = f"{op} <== dump的参数不能小于0"
                return

            idx0 = op.p1.value(self.state)
            if idx0 < 0 or idx0 >= self.state.MEM_SIZE:
                self.state.execution_state = ExecutionState.Error
                self.state.errmsg = f"{op.p1}={idx0} 超出内存范围"
                return
        else:
            idx0 = None

        self.state.ip += 1
        self.dump(idx0, op.n)

        # Avoid double enter in step mode
        if not self.step_mode:
            input("按回车继续执行后续指令")

    def _handle_pause(self, op: Pause):
        """Handle pause operation with console input."""
        self.state.ip += 1
        input("...PAUSE...")

    def _handle_input(self, op: Input):
        """Handle input operation with console input."""
        try:
            s = input(f"Input a number into {op.p1}: ")
            v = int(s)
            if isinstance(op.p1, Mem):
                self.state.set_mem_value(op.p1.addr(self.state), v)
            elif isinstance(op.p1, Reg):
                self.state.set_reg_value(op.p1.reg, v)
            else:
                raise ValueError()
            self.state.ip += 1
        except IndexError as e:
            self.state.execution_state = ExecutionState.Error
            self.state.errmsg = f"{op} | {e}"
        except ValueError as e:
            self.state.execution_state = ExecutionState.Error
            self.state.errmsg = f"{op} | {e}"

    def dump(self, mem_idx0, mem_cnt):
        """
        Display registers and memory state to console.

        Args:
            mem_idx0: Starting memory address to display (None to skip memory dump)
            mem_cnt: Number of memory cells to display
        """
        print(f"\n=========== {self.state.execution_state} ============")
        if self.state.execution_state == ExecutionState.Error:
            print(self.state.errmsg)

        # Display general-purpose registers
        print(f"ax={self.state.ax:8d} bx={self.state.bx:8d} cx={self.state.cx:8d} dx={self.state.dx:8d} flg={self.state.flg:8d}")
        print(f"ip={self.state.ip:8d} bp={self.state.bp:8d} sp={self.state.sp:8d}")

        # Display instruction context (14 lines before and after current instruction)
        print("---- code context ----")
        for i in range(-14, 15):
            idx = self.state.ip + i
            if 0 <= idx < len(self.state.ops):
                _op = self.state.ops[idx]
                for label in _op.labels:
                    print(label + ":")
                print("==> " if i == 0 else "    ", end="")
                print(f"<{_op.addr}> {_op}")

        # Display memory in 16-column format
        if mem_idx0 is not None:
            print("---- memory ----")
            if mem_cnt < 0:
                self.state.execution_state = ExecutionState.Error
                self.state.errmsg = f"{self} <== dump的参数不能小于0"
                return

            if mem_idx0 < 0 or mem_idx0 >= self.state.MEM_SIZE:
                self.state.execution_state = ExecutionState.Error
                self.state.errmsg = f"内存起始地址{mem_idx0} 超出范围"
                return

            # Header row
            print("      ", end="")
            for i in range(16):
                print(f"{i:8d}", end=" ")
            print()

            # Memory rows
            for i in range(0, mem_cnt):
                idx = mem_idx0 + i
                if i % 16 == 0:
                    print(f"{idx:4d}: ", end="")
                if idx < self.state.MEM_SIZE:
                    print(f"{self.state.mem[idx][0]:8d}", end="\n" if i % 16 == 15 else " ")
            print()

        print(f"=========== dump finished ============")
