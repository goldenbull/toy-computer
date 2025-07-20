# -*- coding: utf-8 -*-

import argparse
from antlr4 import *

from computer.computer import Computer
from grammar.toy_asmLexer import toy_asmLexer
from grammar.toy_asmParser import toy_asmParser
from grammar.visitor_impl import VisitorImpl

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("-s", "--step", help="step mode", default=False, action="store_true")
    args = parser.parse_args()
    fname = args.filename
    # fname = "src/tests/1-2.asm"

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
        computer = Computer(visitor.ops_and_labels, args.step)
        computer.run()
    except Exception as ex:
        print(ex)
        # 语法解析错误
        exit()
