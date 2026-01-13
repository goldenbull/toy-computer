# -*- coding: utf-8 -*-

import numpy.random as rnd
from . import ExecutionState, OpBase, DivZeroError, MemType
from .operand import OperandType, Operand


class Move(OpBase):
    def __init__(self, p1: Operand, p2: Operand):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return f"mov {self.p1}, {self.p2}"

    def execute(self):
        try:
            v = self.p2.value(self.computer_state)

            if self.p1.tp == OperandType.Reg:
                self.computer_state.set_reg_value(self.p1.reg, v)
            elif self.p1.tp == OperandType.Mem:
                addr = self.p1.mem_addr(self.computer_state)
                self.computer_state.set_mem_value(addr, v)
            else:
                raise TypeError("unexpected error")

            self.computer_state.ip += 1
        except IndexError as e:
            self.computer_state.execution_state = ExecutionState.Error
            self.computer_state.errmsg = f"{self} | {e}"


class Add(OpBase):
    def __init__(self, p1: Operand, p2: Operand):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return f"add {self.p1}, {self.p2}"

    def execute(self):
        try:
            v1 = self.computer_state.get_reg_value(self.p1.reg)
            v2 = self.p2.value(self.computer_state)
            self.computer_state.set_reg_value(self.p1.reg, v1 + v2)

            self.computer_state.ip += 1
        except IndexError as e:
            self.computer_state.execution_state = ExecutionState.Error
            self.computer_state.errmsg = f"{self} | {e}"


class Sub(OpBase):
    def __init__(self, p1: Operand, p2: Operand):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return f"sub {self.p1}, {self.p2}"

    def execute(self):
        try:
            v1 = self.computer_state.get_reg_value(self.p1.reg)
            v2 = self.p2.value(self.computer_state)
            self.computer_state.set_reg_value(self.p1.reg, v1 - v2)

            self.computer_state.ip += 1
        except IndexError as e:
            self.computer_state.execution_state = ExecutionState.Error
            self.computer_state.errmsg = f"{self} | {e}"


class Mul(OpBase):
    def __init__(self, p1: Operand):
        self.p1 = p1

    def __repr__(self):
        return f"mul {self.p1}"

    def execute(self):
        try:
            v1 = self.computer_state.get_reg_value("ax")
            v2 = self.p1.value(self.computer_state)
            self.computer_state.set_reg_value("ax", v1 * v2)

            self.computer_state.ip += 1
        except IndexError as e:
            self.computer_state.execution_state = ExecutionState.Error
            self.computer_state.errmsg = f"{self} | {e}"


class Div(OpBase):
    def __init__(self, p1: Operand):
        self.p1 = p1

    def __repr__(self):
        return f"div {self.p1}"

    def execute(self):
        try:
            # 需要处理除0的情况
            v1 = self.computer_state.get_reg_value("ax")
            v2 = self.p1.value(self.computer_state)
            if v2 == 0:
                raise DivZeroError()
            # 特殊处理向零取整，和C一致
            r1 = int(v1 / v2)
            r2 = v1 - v2 * r1
            self.computer_state.set_reg_value("ax", r1)
            self.computer_state.set_reg_value("dx", r2)

            self.computer_state.ip += 1
        except IndexError as e:
            self.computer_state.execution_state = ExecutionState.Error
            self.computer_state.errmsg = f"{self} | {e}"
        except DivZeroError:
            self.computer_state.execution_state = ExecutionState.Error
            self.computer_state.errmsg = f"{self} | div0"


class Cmp(OpBase):
    def __init__(self, p1: Operand, p2: Operand):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return f"cmp {self.p1}, {self.p2}"

    def execute(self):
        try:
            v1 = self.computer_state.get_reg_value(self.p1.reg)
            v2 = self.p2.value(self.computer_state)
            if v1 > v2:
                self.computer_state.set_reg_value("flg", 1)
            elif v1 == v2:
                self.computer_state.set_reg_value("flg", 0)
            else:
                self.computer_state.set_reg_value("flg", -1)
            self.computer_state.ip += 1
        except IndexError as e:
            self.computer_state.execution_state = ExecutionState.Error
            self.computer_state.errmsg = f"{self} | {e}"


class Jump(OpBase):
    def __init__(self, action: str, target: str, src_line: int):
        self.action = action
        self.target = target
        self.src_line = src_line  # line no. of this op in source code, for compile error report

    def __repr__(self):
        try:
            target_addr = self.computer_state.labels_tbl[self.target]
            return f"{self.action} {self.target} ({target_addr - self.addr:+d})"
        except (KeyError, AttributeError):
            return f"{self.action} {self.target}"

    def execute(self):
        try:
            target_addr = self.computer_state.labels_tbl[self.target]
            flg = self.computer_state.get_reg_value("flg")
            if (self.action == "jmp"
                    or (self.action == "je" and flg == 0)
                    or (self.action == "jne" and flg != 0)
                    or (self.action == "jg" and flg > 0)
                    or (self.action == "jge" and flg >= 0)
                    or (self.action == "jl" and flg < 0)
                    or (self.action == "jle" and flg <= 0)
            ):
                self.computer_state.ip = target_addr
            else:
                self.computer_state.ip += 1
        except KeyError as e:
            self.computer_state.execution_state = ExecutionState.Error
            self.computer_state.errmsg = f"{self} | invalid label {e}"


class Call(OpBase):
    def __init__(self, target: str, src_line: int):
        self.target = target
        self.src_line = src_line  # line no. of this op in source code, for compile error report

    def __repr__(self):
        try:
            target_addr = self.computer_state.labels_tbl[self.target]
            return f"call {self.target} <{target_addr}>"
        except (KeyError, AttributeError):
            return f"call {self.target}"

    def execute(self):
        try:
            # ip入栈，jmp到函数入口
            target_addr = self.computer_state.labels_tbl[self.target]
            self.computer_state.push_stack(self.computer_state.ip + 1, MemType.IP)  # 返回的位置应该是下一条指令
            self.computer_state.ip = target_addr
        except KeyError as e:
            self.computer_state.execution_state = ExecutionState.Error
            self.computer_state.errmsg = f"{self} | invalid label {e}"


class Ret(OpBase):
    def __repr__(self):
        return f"ret"  # TODO 如何显示来时的地址？执行前后sp会变化

    def execute(self):
        try:
            origin_addr = self.computer_state.pop_stack()
            self.computer_state.ip = origin_addr
        except IndexError as e:
            self.computer_state.execution_state = ExecutionState.Error
            self.computer_state.errmsg = f"{self} | {e}"


class Push(OpBase):
    def __init__(self, action: str, p1: Operand = None):
        self.action = action
        self.p1 = p1

    def __repr__(self):
        if self.p1 is None:
            return f"{self.action}"
        else:
            return f"{self.action} {self.p1}"

    def execute(self):
        # 分情况处理
        try:
            if self.action == "push":
                v = self.p1.value(self.computer_state)
                # special type for bp
                if self.p1.tp == OperandType.Reg and self.p1.reg == "bp":
                    tp = MemType.BP
                else:
                    tp = MemType.Data
                self.computer_state.push_stack(v, tp)
            elif self.action == "pushf":
                v = self.computer_state.get_reg_value("flg")
                self.computer_state.push_stack(v)
            else:
                raise ValueError()
            self.computer_state.ip += 1
        except IndexError as e:
            self.computer_state.execution_state = ExecutionState.Error
            self.computer_state.errmsg = f"{self} | {e}"


class Pop(OpBase):
    def __init__(self, action: str, p1: Operand = None):
        self.action = action
        self.p1 = p1

    def __repr__(self):
        if self.p1 is None:
            return f"{self.action}"
        else:
            return f"{self.action} {self.p1}"

    def execute(self):
        # 分情况处理
        try:
            if self.action == "pop":
                v = self.computer_state.pop_stack()
                if self.p1 is not None:
                    self.computer_state.set_reg_value(self.p1.reg, v)
            elif self.action == "popf":
                v = self.computer_state.pop_stack()
                self.computer_state.set_reg_value("flg", v)
            else:
                raise ValueError()
            self.computer_state.ip += 1
        except IndexError as e:
            self.computer_state.execution_state = ExecutionState.Error
            self.computer_state.errmsg = f"{self} | {e}"


class Input(OpBase):
    def __init__(self, p1):
        self.p1 = p1

    def __repr__(self):
        return f"input {self.p1}"

    def execute(self):
        """Input operation - delegates to executor."""
        try:
            self.executor.handle_input(self.p1)
            self.computer_state.ip += 1
        except (IndexError, ValueError) as e:
            self.computer_state.execution_state = ExecutionState.Error
            self.computer_state.errmsg = f"{self} | {e}"


class Print(OpBase):
    def __init__(self, action, p1):
        self.action = action
        self.p1 = p1

    def __repr__(self):
        return f"{self.action} {self.p1}"

    def execute(self):
        """Print operation - delegates to executor."""
        try:
            v = self.p1.value(self.computer_state) if self.p1 is not None else ""
            newline = (self.action == "println")
            self.executor.handle_print(str(v), newline)
            self.computer_state.ip += 1
        except IndexError as e:
            self.computer_state.execution_state = ExecutionState.Error
            self.computer_state.errmsg = f"{self} | {e}"


class Rand(OpBase):
    def __init__(self, p1):
        self.p1 = p1

    def __repr__(self):
        return f"rand {self.p1}"

    def execute(self):
        try:
            v = rnd.randint(0, 1000)
            if self.p1.tp == OperandType.Mem:
                self.computer_state.set_mem_value(self.p1.mem_addr(self.computer_state), v)
            elif self.p1.tp == OperandType.Reg:
                self.computer_state.set_reg_value(self.p1.reg, v)
            else:
                raise TypeError()
            self.computer_state.ip += 1
        except IndexError as e:
            self.computer_state.execution_state = ExecutionState.Error
            self.computer_state.errmsg = f"{self} | {e}"


class Dump(OpBase):
    def __init__(self, p1: Operand = None, cnt: int = None):
        self.p1 = p1
        self.cnt = cnt

    def __repr__(self):
        if self.p1 is None:
            return f"dump"
        else:
            return f"dump {self.p1}, {self.cnt}"

    def execute(self):
        """Dump operation - delegates to executor."""
        # 检查参数合法性
        if self.p1 is not None:
            if self.cnt < 0:
                self.computer_state.execution_state = ExecutionState.Error
                self.computer_state.errmsg = f"{self} <== dump的参数不能小于0"
                return

            idx0 = self.p1.value(self.computer_state)
            if idx0 < 0 or idx0 >= self.computer_state.MEM_SIZE:
                self.computer_state.execution_state = ExecutionState.Error
                self.computer_state.errmsg = f"{self.p1}={idx0} 超出内存范围"
                return
        else:
            idx0 = None

        self.executor.handle_dump(idx0, self.cnt if self.p1 is not None else 0)
        self.computer_state.ip += 1


class Pause(OpBase):
    def __repr__(self):
        return f"pause"

    def execute(self):
        """Pause operation - delegates to executor."""
        self.executor.handle_pause()
        self.computer_state.ip += 1


class Halt(OpBase):
    def __repr__(self):
        return f"halt"

    def execute(self):
        self.computer_state.execution_state = ExecutionState.Finished


class Nop(OpBase):
    def __repr__(self):
        return f"nop"

    def execute(self):
        self.computer_state.ip += 1
