# -*- coding: utf-8 -*-

from antlr4 import *
from grammar.toy_asmLexer import toy_asmLexer
from grammar.toy_asmParser import toy_asmParser
from src.grammar.visitor_impl import VisitorImpl

if __name__ == '__main__':
    fname = "tests/1.asm"
    txt = open(fname, "rt", encoding="utf-8").read() + '\n'  # 确保最后一行有回车
    stm = InputStream(txt)
    lexer = toy_asmLexer(stm)
    stream = CommonTokenStream(lexer)
    parser = toy_asmParser(stream)
    visitor = VisitorImpl()

    # 得到所有指令
    visitor.visit(parser.program())

    # 为指令生成序号
    for i, op in enumerate(visitor.ops):
        op.addr = i
        print(op)
