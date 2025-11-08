# -*- coding: utf-8 -*-

import argparse
from console.console_executor import ConsoleExecutor

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("-s", "--step", help="step mode", default=False, action="store_true")
    args = parser.parse_args()
    step_mode = args.step
    fname = args.filename
    # fname = "../tests/2-syntax-error.asm"
    # step_mode = False

    try:
        txt = open(fname, "rt", encoding="utf-8").read()

        # 启动计算机，开始逐行执行
        executor = ConsoleExecutor(txt, step_mode)
        executor.run()
    except Exception as ex:
        print(ex)
        # 语法解析错误
        exit()
