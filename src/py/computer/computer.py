# -*- coding: utf-8 -*-

from . import ComputerState, Op


class Computer:
    # 内存总的大小
    MEM_SIZE = 1024

    def __init__(self, ops_and_labels: list, step_mode: bool):
        # 通用寄存器
        self.ax = 11111111
        self.bx = 22222222
        self.cx = 33333333
        self.dx = 44444444
        self.flg = 0

        # 指令寄存器和栈寄存器
        self.ip = 0
        self.bp = 55555555
        self.sp = self.MEM_SIZE // 2  # 内存的后一半留给栈

        # 内存
        self.mem = [66666666] * (self.MEM_SIZE // 2) + [88888888] * (self.MEM_SIZE // 2)

        # 为加载的指令生成序号
        self.ops = [x for x in ops_and_labels if isinstance(x, Op)]
        for i, op in enumerate(self.ops):
            op.addr = i
            op.c = self

        # 所有label归属到下一条op
        cur_labels = []
        for x in ops_and_labels:
            if isinstance(x, str):
                cur_labels.append(x)
            elif isinstance(x, Op):
                # assign all above labels to this op
                x.labels = cur_labels
                cur_labels = []
            else:
                raise ValueError("impossible")
        if len(cur_labels) > 0:
            raise SyntaxError("最后的label没有对应指令")

        # 建立Label和addr的映射表
        self.labels_tbl = dict()
        for op in self.ops:
            for label in op.labels:
                self.labels_tbl[label] = op.addr

        # 当前状态
        self.state = ComputerState.Running
        self.errmsg = ""

        # 逐步执行模式
        self.step_mode = step_mode

    def get_reg_value(self, reg: str):
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
            raise ValueError()

    def set_reg_value(self, reg: str, v: int):
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
            raise ValueError()

    def get_mem_value(self, addr: int):
        if addr < 0 or addr >= self.MEM_SIZE:
            raise IndexError(f"addr={addr}, 内存越界")
        return self.mem[addr]

    def get_reg_mem_value(self, reg: str, offset: int):
        v = self.get_reg_value(reg)
        addr = v + offset
        if addr < 0 or addr >= self.MEM_SIZE:
            raise IndexError(f"{reg}={v}, offset={offset}, addr={addr}, 内存越界")
        return self.mem[addr]

    def set_mem_value(self, addr: int, v: int):
        if addr < 0 or addr >= self.MEM_SIZE:
            raise IndexError(f"addr={addr}, 内存越界")
        self.mem[addr] = v

    def run(self):
        while True:
            next_ip = self.ip
            if next_ip < 0:
                self.state = ComputerState.Error
                self.errmsg = f"next ip={next_ip} 异常终止"
                break
            if next_ip >= len(self.ops) or self.state == ComputerState.Finished:
                self.state = ComputerState.Finished
                break

            op = self.ops[next_ip]
            op.execute()
            if self.step_mode:
                self.dump(512, 64)  # 默认输出栈的前64个位置， TODO：动态改变
                input("step模式，按回车继续执行下一条指令")
            if self.state == ComputerState.Error:
                print(f"系统错误: {self.errmsg}")
                break

        if self.state == ComputerState.Finished:
            print("====== finished ======")
        else:
            print(self.errmsg)
        # TODO: 耗时统计

    def dump(self, mem_idx0, mem_cnt):
        """
        显示寄存器和内存的全部状态
        """
        print(f"\n=========== {self.state} ============")
        if self.state == ComputerState.Error:
            print(self.errmsg)

        # 通用寄存器
        print(f"ax={self.ax:8d} bx={self.bx:8d} cx={self.cx:8d} dx={self.dx:8d} flg={self.flg:8d}")
        print(f"ip={self.ip:8d} bp={self.bp:8d} sp={self.sp:8d}")

        # 当前指令上下文，各显示10条即可
        print("---- code context ----")
        for i in range(-10, 11):
            idx = self.ip + i
            if 0 <= idx < len(self.ops):
                _op = self.ops[idx]
                for label in _op.labels:
                    print(label + ":")
                print("==> " if i == 0 else "    ", end="")
                print(f"<{_op.addr}> {_op}")

        # 显示内存，每行显示16个数
        if mem_idx0 is not None:
            print("---- memory ----")
            if mem_cnt < 0:
                self.state = ComputerState.Error
                self.errmsg = f"{self} <== dump的参数不能小于0"
                return

            if mem_idx0 < 0 or mem_idx0 >= self.MEM_SIZE:
                self.state = ComputerState.Error
                self.errmsg = f"内存起始地址{mem_idx0} 超出范围"
                return

            for i in range(0, mem_cnt):
                idx = mem_idx0 + i
                if i % 16 == 0:
                    print(f"{idx:4d}: ", end="")
                if idx < self.MEM_SIZE:
                    print(f"{self.mem[idx]:8d}", end="\n" if i % 16 == 15 else " ")
            print(

            )
        print(f"=========== dump finished ============")
