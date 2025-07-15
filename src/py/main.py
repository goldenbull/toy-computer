# -*- coding: utf-8 -*-

from antlr4 import *

from grammar.computer import Computer
from grammar.toy_asmLexer import toy_asmLexer
from grammar.toy_asmParser import toy_asmParser
from src.grammar.visitor_impl import VisitorImpl

if __name__ == '__main__':
    try:
        fname = "tests/prime.asm"
        txt = open(fname, "rt", encoding="utf-8").read() + '\n'  # 确保最后一行有回车
        stm = InputStream(txt)
        lexer = toy_asmLexer(stm)
        stream = CommonTokenStream(lexer)
        parser = toy_asmParser(stream)
        visitor = VisitorImpl()

        # 得到所有指令
        visitor.visit(parser.program())
        # 启动计算机，开始逐行执行
        computer = Computer(visitor.ops)
        computer.run()
    except Exception as ex:
        print(ex)
        # 语法解析错误
        exit()
