# -*- coding: utf-8 -*-
from enum import Enum

class ComputerState(Enum):
    Running = 0
    Finished = 1
    Error = 2

class Computer:
    # 内存总的大小
    MEM_SIZE = 1024

    def __init__(self, ops: list):
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
        self.ops = ops
        for i, op in enumerate(ops):
            op.addr = i
            op.c = self

        # 建立Label和addr的映射表
        self.labels_tbl = {op.label: op.addr for op in ops if len(op.label) > 0}

        # 当前状态
        self.state = ComputerState.Running
        self.errmsg = ""

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
            if self.state == ComputerState.Error:
                print(f"系统错误: {self.errmsg}")
                break

        if self.state == ComputerState.Finished:
            print("====== finished ======")
        else:
            print(self.errmsg)
        # TODO: 耗时统计
