# -*- coding: utf-8 -*-

from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from .toy_asmLexer import toy_asmLexer
from .toy_asmParser import toy_asmParser
from .visitor_impl import VisitorImpl
from ..computer import OpBase
from ..computer.op_base import OpLabel


class MyErrorListener(ErrorListener):
    """Custom error listener that raises exceptions on syntax errors."""

    def __init__(self, source_code: str):
        super().__init__()
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
            CompileResult containing operations and label2addr table

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

        # Assign labels to operations, each op may have multiple labels
        cur_op_labels: list[OpLabel] = []
        for x in visitor.ops_and_labels:
            if isinstance(x, OpLabel):
                if x.label in [l.label for l in cur_op_labels]:
                    raise SyntaxError(f"第 {x.src_line} 行出现了重复的Label [{x.label}]")
                cur_op_labels.append(x)
            elif isinstance(x, OpBase):
                x.op_labels = cur_op_labels
                cur_op_labels = []

        if len(cur_op_labels) > 0:
            raise SyntaxError(f"第 {cur_op_labels[-1].src_line} 行的 Label [{cur_op_labels[-1].label}] 缺少指令")

        # Build op_label table (mapping op_label.label to instruction addresses)
        all_op_labels: list[OpLabel] = []
        label2addr: dict[str, int] = {}
        for op in ops:
            for op_label in op.op_labels:
                if op_label.label in label2addr:
                    prev_occurrance = [x for x in all_op_labels if x.label == op_label.label][0]
                    raise SyntaxError(f"第 {op_label.src_line} 行出现了重复的Label [{op_label.label}]，"
                                      f"已在第 {prev_occurrance.src_line} 行定义了同名Label")
                all_op_labels.append(op_label)
                label2addr[op_label.label] = op.addr

        # check all jmp and call labels
        for op in ops:
            from internal.computer.operations import Jump, Call
            if isinstance(op, (Jump, Call)):
                if op.target not in label2addr:
                    raise SyntaxError(f"第 {op.src_line} 行，{op.to_str()} [{op.target}]不存在")

        return CompileResult(ops, label2addr)
