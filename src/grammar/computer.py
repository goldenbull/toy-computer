# -*- coding: utf-8 -*-

import numpy.random as rnd
from grammar import ComputerState
from src.grammar.operations import *


class Computer:
    # 内存总的大小
    MEM_SIZE = 1024

    def __init__(self, ops: list["Op"]):
        # 通用寄存器
        self.ax = rnd.randint(-2 ** 30, 2 ** 30)
        self.bx = rnd.randint(-2 ** 30, 2 ** 30)
        self.cx = rnd.randint(-2 ** 30, 2 ** 30)
        self.dx = rnd.randint(-2 ** 30, 2 ** 30)
        self.flg = rnd.randint(-1, 1)

        # 指令寄存器和栈寄存器
        self.ip = 0
        self.bp = rnd.randint(-2 ** 30, 2 ** 30)
        self.sp = self.MEM_SIZE // 2  # 内存的后一半留给栈

        # 内存，填满随机值
        self.mem = rnd.randint(-2 ** 30, 2 ** 30, self.MEM_SIZE)

        # 为加载的指令生成序号
        self.ops = ops
        for i, op in enumerate(ops):
            op.addr = i

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
        for op in self.ops:
            op.execute(self)
            if self.state == ComputerState.Error:
                print(f"系统错误: {self.errmsg}")
                break
        if self.state == ComputerState.Running:
            self.state = ComputerState.Finished
            print("====== finished ======")
