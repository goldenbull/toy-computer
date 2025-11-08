# -*- coding: utf-8 -*-

import argparse
from antlr4 import *

from console.console_executor import ConsoleExecutor
from internal.grammar.toy_asmLexer import toy_asmLexer
from internal.grammar.toy_asmParser import toy_asmParser
from internal.grammar.visitor_impl import VisitorImpl

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("-s", "--step", help="step mode", default=False, action="store_true")
    args = parser.parse_args()
    step_mode = args.step
    fname = args.filename
    # fname = "../tests/fib.asm"
    # step_mode = False

    try:
        txt = open(fname, "rt", encoding="utf-8").read()
        # txt = open(args.filename, "rt", encoding="utf-8").read()
        stm = InputStream(txt)
        lexer = toy_asmLexer(stm)
        stream = CommonTokenStream(lexer)
        parser = toy_asmParser(stream)
        visitor = VisitorImpl()

        # 得到所有指令
        visitor.visit(parser.program())

        # 启动计算机，开始逐行执行
        executor = ConsoleExecutor(visitor.ops_and_labels, step_mode)
        executor.run()
    except Exception as ex:
        print(ex)
        # 语法解析错误
        exit()
