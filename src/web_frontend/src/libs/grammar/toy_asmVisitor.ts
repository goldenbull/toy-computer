// Generated from toy_asm.g4 by ANTLR 4.13.2

import {ParseTreeVisitor} from 'antlr4';


import { LineContext } from "./toy_asmParser.js";
import { LabelContext } from "./toy_asmParser.js";
import { CommentContext } from "./toy_asmParser.js";
import { OpContext } from "./toy_asmParser.js";
import { NumContext } from "./toy_asmParser.js";
import { RegContext } from "./toy_asmParser.js";
import { OffsetContext } from "./toy_asmParser.js";
import { MemContext } from "./toy_asmParser.js";
import { MovContext } from "./toy_asmParser.js";
import { AddContext } from "./toy_asmParser.js";
import { SubContext } from "./toy_asmParser.js";
import { MulContext } from "./toy_asmParser.js";
import { DivContext } from "./toy_asmParser.js";
import { CmpContext } from "./toy_asmParser.js";
import { JumpContext } from "./toy_asmParser.js";
import { CallContext } from "./toy_asmParser.js";
import { RetContext } from "./toy_asmParser.js";
import { PushContext } from "./toy_asmParser.js";
import { PopContext } from "./toy_asmParser.js";
import { InputContext } from "./toy_asmParser.js";
import { StrContext } from "./toy_asmParser.js";
import { PrintContext } from "./toy_asmParser.js";
import { RandContext } from "./toy_asmParser.js";
import { BreakContext } from "./toy_asmParser.js";
import { HaltContext } from "./toy_asmParser.js";


/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by `toy_asmParser`.
 *
 * @param <Result> The return type of the visit operation. Use `void` for
 * operations with no return type.
 */
export default class toy_asmVisitor<Result> extends ParseTreeVisitor<Result> {
	/**
	 * Visit a parse tree produced by `toy_asmParser.line`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitLine?: (ctx: LineContext) => Result;
	/**
	 * Visit a parse tree produced by `toy_asmParser.label`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitLabel?: (ctx: LabelContext) => Result;
	/**
	 * Visit a parse tree produced by `toy_asmParser.comment`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitComment?: (ctx: CommentContext) => Result;
	/**
	 * Visit a parse tree produced by `toy_asmParser.op`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitOp?: (ctx: OpContext) => Result;
	/**
	 * Visit a parse tree produced by `toy_asmParser.num`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitNum?: (ctx: NumContext) => Result;
	/**
	 * Visit a parse tree produced by `toy_asmParser.reg`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitReg?: (ctx: RegContext) => Result;
	/**
	 * Visit a parse tree produced by `toy_asmParser.offset`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitOffset?: (ctx: OffsetContext) => Result;
	/**
	 * Visit a parse tree produced by `toy_asmParser.mem`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitMem?: (ctx: MemContext) => Result;
	/**
	 * Visit a parse tree produced by `toy_asmParser.mov`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitMov?: (ctx: MovContext) => Result;
	/**
	 * Visit a parse tree produced by `toy_asmParser.add`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitAdd?: (ctx: AddContext) => Result;
	/**
	 * Visit a parse tree produced by `toy_asmParser.sub`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitSub?: (ctx: SubContext) => Result;
	/**
	 * Visit a parse tree produced by `toy_asmParser.mul`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitMul?: (ctx: MulContext) => Result;
	/**
	 * Visit a parse tree produced by `toy_asmParser.div`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitDiv?: (ctx: DivContext) => Result;
	/**
	 * Visit a parse tree produced by `toy_asmParser.cmp`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitCmp?: (ctx: CmpContext) => Result;
	/**
	 * Visit a parse tree produced by `toy_asmParser.jump`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitJump?: (ctx: JumpContext) => Result;
	/**
	 * Visit a parse tree produced by `toy_asmParser.call`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitCall?: (ctx: CallContext) => Result;
	/**
	 * Visit a parse tree produced by `toy_asmParser.ret`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitRet?: (ctx: RetContext) => Result;
	/**
	 * Visit a parse tree produced by `toy_asmParser.push`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitPush?: (ctx: PushContext) => Result;
	/**
	 * Visit a parse tree produced by `toy_asmParser.pop`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitPop?: (ctx: PopContext) => Result;
	/**
	 * Visit a parse tree produced by `toy_asmParser.input`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitInput?: (ctx: InputContext) => Result;
	/**
	 * Visit a parse tree produced by `toy_asmParser.str`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitStr?: (ctx: StrContext) => Result;
	/**
	 * Visit a parse tree produced by `toy_asmParser.print`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitPrint?: (ctx: PrintContext) => Result;
	/**
	 * Visit a parse tree produced by `toy_asmParser.rand`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitRand?: (ctx: RandContext) => Result;
	/**
	 * Visit a parse tree produced by `toy_asmParser.break`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitBreak?: (ctx: BreakContext) => Result;
	/**
	 * Visit a parse tree produced by `toy_asmParser.halt`.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	visitHalt?: (ctx: HaltContext) => Result;
}

