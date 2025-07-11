# -*- coding: utf-8 -*-
from enum import Enum

import numpy.random as rnd


class State(Enum):
    Running = 0
    Finished = 1
    Error = 2


class Computer:
    # 内存总的大小
    MEM_SIZE = 1024

    def __init__(self):
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

        # 当前状态
        self.state = State.Running
        self.errmsg = ""
