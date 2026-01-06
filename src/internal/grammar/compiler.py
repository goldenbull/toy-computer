# -*- coding: utf-8 -*-

from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from .toy_asmLexer import toy_asmLexer
from .toy_asmParser import toy_asmParser
from .visitor_impl import VisitorImpl
from ..computer import OpBase


class MyErrorListener(ErrorListener):
    """Custom error listener that raises exceptions on syntax errors."""

    def __init__(self, source_code: str):
        super().__init__()
        print(source_code)
        self.source_code_lines = source_code.split("\n")
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_message = f"第{line}行：\n"
        error_message += self.source_code_lines[line - 1] + "\n"
        error_message += " " * (column - 1) + "^ 语法错误，请检查"
        raise Exception(error_message)


class CompileResult:
    """Result of compiling assembly source code."""

    def __init__(self, ops: list[OpBase], labels_tbl: dict[str, int]):
        self.ops = ops
        self.labels_tbl = labels_tbl


class Compiler:
    """
    Compiler for toy assembly language.
    Parses source code into structured operations and label table.
    """

    @staticmethod
    def compile(source_code: str) -> CompileResult:
        """
        Compile assembly source code into operations and labels.

        Args:
            source_code: Assembly source code as string

        Returns:
            CompileResult containing operations and label table

        Raises:
            Exception: If there are syntax errors in the source code
        """
        # Parse ASM source code
        err_listener = MyErrorListener(source_code)
        stm = InputStream(source_code)
        lexer = toy_asmLexer(stm)
        lexer.addErrorListener(err_listener)
        stream = CommonTokenStream(lexer)
        parser = toy_asmParser(stream)
        parser.addErrorListener(err_listener)
        visitor = VisitorImpl()
        visitor.visit(parser.program())

        # Extract operations
        ops = [x for x in visitor.ops_and_labels if isinstance(x, OpBase)]

        # Assign addresses to operations
        for i, op in enumerate(ops):
            op.addr = i

        # Assign labels to operations
        cur_labels = []
        for x in visitor.ops_and_labels:
            if isinstance(x, str):
                if x in cur_labels:
                    raise SyntaxError(f"出现了重复的Label [{x}]")
                cur_labels.append(x)
            elif isinstance(x, OpBase):
                x.labels = cur_labels
                cur_labels = []

        if len(cur_labels) > 0:
            raise SyntaxError("Label at end of file has no corresponding instruction")

        # Build label table (mapping label names to instruction addresses)
        labels_tbl = {}
        for op in ops:
            for label in op.labels:
                if label in labels_tbl:
                    raise SyntaxError(f"出现了重复的Label [{label}]")
                labels_tbl[label] = op.addr

        # check all jmp and call labels
        for op in ops:
            from internal.computer.operations import Jump, Call
            if isinstance(op, (Jump, Call)):
                if op.target not in labels_tbl:
                    raise SyntaxError(f"{op.to_str()} [{op.target}]不存在")

        return CompileResult(ops, labels_tbl)
