// Generated from toy_asm.g4 by ANTLR 4.13.2

import {ParseTreeListener} from "antlr4";


import { ProgramContext } from "./toy_asmParser.js";
import { OpLabelContext } from "./toy_asmParser.js";
import { OpContext } from "./toy_asmParser.js";
import { NumContext } from "./toy_asmParser.js";
import { RegContext } from "./toy_asmParser.js";
import { OffsetContext } from "./toy_asmParser.js";
import { MemContext } from "./toy_asmParser.js";
import { MoveContext } from "./toy_asmParser.js";
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
import { PauseContext } from "./toy_asmParser.js";
import { HaltContext } from "./toy_asmParser.js";
import { NopContext } from "./toy_asmParser.js";


/**
 * This interface defines a complete listener for a parse tree produced by
 * `toy_asmParser`.
 */
export default class toy_asmListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by `toy_asmParser.program`.
	 * @param ctx the parse tree
	 */
	enterProgram?: (ctx: ProgramContext) => void;
	/**
	 * Exit a parse tree produced by `toy_asmParser.program`.
	 * @param ctx the parse tree
	 */
	exitProgram?: (ctx: ProgramContext) => void;
	/**
	 * Enter a parse tree produced by `toy_asmParser.opLabel`.
	 * @param ctx the parse tree
	 */
	enterOpLabel?: (ctx: OpLabelContext) => void;
	/**
	 * Exit a parse tree produced by `toy_asmParser.opLabel`.
	 * @param ctx the parse tree
	 */
	exitOpLabel?: (ctx: OpLabelContext) => void;
	/**
	 * Enter a parse tree produced by `toy_asmParser.op`.
	 * @param ctx the parse tree
	 */
	enterOp?: (ctx: OpContext) => void;
	/**
	 * Exit a parse tree produced by `toy_asmParser.op`.
	 * @param ctx the parse tree
	 */
	exitOp?: (ctx: OpContext) => void;
	/**
	 * Enter a parse tree produced by `toy_asmParser.num`.
	 * @param ctx the parse tree
	 */
	enterNum?: (ctx: NumContext) => void;
	/**
	 * Exit a parse tree produced by `toy_asmParser.num`.
	 * @param ctx the parse tree
	 */
	exitNum?: (ctx: NumContext) => void;
	/**
	 * Enter a parse tree produced by `toy_asmParser.reg`.
	 * @param ctx the parse tree
	 */
	enterReg?: (ctx: RegContext) => void;
	/**
	 * Exit a parse tree produced by `toy_asmParser.reg`.
	 * @param ctx the parse tree
	 */
	exitReg?: (ctx: RegContext) => void;
	/**
	 * Enter a parse tree produced by `toy_asmParser.offset`.
	 * @param ctx the parse tree
	 */
	enterOffset?: (ctx: OffsetContext) => void;
	/**
	 * Exit a parse tree produced by `toy_asmParser.offset`.
	 * @param ctx the parse tree
	 */
	exitOffset?: (ctx: OffsetContext) => void;
	/**
	 * Enter a parse tree produced by `toy_asmParser.mem`.
	 * @param ctx the parse tree
	 */
	enterMem?: (ctx: MemContext) => void;
	/**
	 * Exit a parse tree produced by `toy_asmParser.mem`.
	 * @param ctx the parse tree
	 */
	exitMem?: (ctx: MemContext) => void;
	/**
	 * Enter a parse tree produced by `toy_asmParser.move`.
	 * @param ctx the parse tree
	 */
	enterMove?: (ctx: MoveContext) => void;
	/**
	 * Exit a parse tree produced by `toy_asmParser.move`.
	 * @param ctx the parse tree
	 */
	exitMove?: (ctx: MoveContext) => void;
	/**
	 * Enter a parse tree produced by `toy_asmParser.add`.
	 * @param ctx the parse tree
	 */
	enterAdd?: (ctx: AddContext) => void;
	/**
	 * Exit a parse tree produced by `toy_asmParser.add`.
	 * @param ctx the parse tree
	 */
	exitAdd?: (ctx: AddContext) => void;
	/**
	 * Enter a parse tree produced by `toy_asmParser.sub`.
	 * @param ctx the parse tree
	 */
	enterSub?: (ctx: SubContext) => void;
	/**
	 * Exit a parse tree produced by `toy_asmParser.sub`.
	 * @param ctx the parse tree
	 */
	exitSub?: (ctx: SubContext) => void;
	/**
	 * Enter a parse tree produced by `toy_asmParser.mul`.
	 * @param ctx the parse tree
	 */
	enterMul?: (ctx: MulContext) => void;
	/**
	 * Exit a parse tree produced by `toy_asmParser.mul`.
	 * @param ctx the parse tree
	 */
	exitMul?: (ctx: MulContext) => void;
	/**
	 * Enter a parse tree produced by `toy_asmParser.div`.
	 * @param ctx the parse tree
	 */
	enterDiv?: (ctx: DivContext) => void;
	/**
	 * Exit a parse tree produced by `toy_asmParser.div`.
	 * @param ctx the parse tree
	 */
	exitDiv?: (ctx: DivContext) => void;
	/**
	 * Enter a parse tree produced by `toy_asmParser.cmp`.
	 * @param ctx the parse tree
	 */
	enterCmp?: (ctx: CmpContext) => void;
	/**
	 * Exit a parse tree produced by `toy_asmParser.cmp`.
	 * @param ctx the parse tree
	 */
	exitCmp?: (ctx: CmpContext) => void;
	/**
	 * Enter a parse tree produced by `toy_asmParser.jump`.
	 * @param ctx the parse tree
	 */
	enterJump?: (ctx: JumpContext) => void;
	/**
	 * Exit a parse tree produced by `toy_asmParser.jump`.
	 * @param ctx the parse tree
	 */
	exitJump?: (ctx: JumpContext) => void;
	/**
	 * Enter a parse tree produced by `toy_asmParser.call`.
	 * @param ctx the parse tree
	 */
	enterCall?: (ctx: CallContext) => void;
	/**
	 * Exit a parse tree produced by `toy_asmParser.call`.
	 * @param ctx the parse tree
	 */
	exitCall?: (ctx: CallContext) => void;
	/**
	 * Enter a parse tree produced by `toy_asmParser.ret`.
	 * @param ctx the parse tree
	 */
	enterRet?: (ctx: RetContext) => void;
	/**
	 * Exit a parse tree produced by `toy_asmParser.ret`.
	 * @param ctx the parse tree
	 */
	exitRet?: (ctx: RetContext) => void;
	/**
	 * Enter a parse tree produced by `toy_asmParser.push`.
	 * @param ctx the parse tree
	 */
	enterPush?: (ctx: PushContext) => void;
	/**
	 * Exit a parse tree produced by `toy_asmParser.push`.
	 * @param ctx the parse tree
	 */
	exitPush?: (ctx: PushContext) => void;
	/**
	 * Enter a parse tree produced by `toy_asmParser.pop`.
	 * @param ctx the parse tree
	 */
	enterPop?: (ctx: PopContext) => void;
	/**
	 * Exit a parse tree produced by `toy_asmParser.pop`.
	 * @param ctx the parse tree
	 */
	exitPop?: (ctx: PopContext) => void;
	/**
	 * Enter a parse tree produced by `toy_asmParser.input`.
	 * @param ctx the parse tree
	 */
	enterInput?: (ctx: InputContext) => void;
	/**
	 * Exit a parse tree produced by `toy_asmParser.input`.
	 * @param ctx the parse tree
	 */
	exitInput?: (ctx: InputContext) => void;
	/**
	 * Enter a parse tree produced by `toy_asmParser.str`.
	 * @param ctx the parse tree
	 */
	enterStr?: (ctx: StrContext) => void;
	/**
	 * Exit a parse tree produced by `toy_asmParser.str`.
	 * @param ctx the parse tree
	 */
	exitStr?: (ctx: StrContext) => void;
	/**
	 * Enter a parse tree produced by `toy_asmParser.print`.
	 * @param ctx the parse tree
	 */
	enterPrint?: (ctx: PrintContext) => void;
	/**
	 * Exit a parse tree produced by `toy_asmParser.print`.
	 * @param ctx the parse tree
	 */
	exitPrint?: (ctx: PrintContext) => void;
	/**
	 * Enter a parse tree produced by `toy_asmParser.rand`.
	 * @param ctx the parse tree
	 */
	enterRand?: (ctx: RandContext) => void;
	/**
	 * Exit a parse tree produced by `toy_asmParser.rand`.
	 * @param ctx the parse tree
	 */
	exitRand?: (ctx: RandContext) => void;
	/**
	 * Enter a parse tree produced by `toy_asmParser.pause`.
	 * @param ctx the parse tree
	 */
	enterPause?: (ctx: PauseContext) => void;
	/**
	 * Exit a parse tree produced by `toy_asmParser.pause`.
	 * @param ctx the parse tree
	 */
	exitPause?: (ctx: PauseContext) => void;
	/**
	 * Enter a parse tree produced by `toy_asmParser.halt`.
	 * @param ctx the parse tree
	 */
	enterHalt?: (ctx: HaltContext) => void;
	/**
	 * Exit a parse tree produced by `toy_asmParser.halt`.
	 * @param ctx the parse tree
	 */
	exitHalt?: (ctx: HaltContext) => void;
	/**
	 * Enter a parse tree produced by `toy_asmParser.nop`.
	 * @param ctx the parse tree
	 */
	enterNop?: (ctx: NopContext) => void;
	/**
	 * Exit a parse tree produced by `toy_asmParser.nop`.
	 * @param ctx the parse tree
	 */
	exitNop?: (ctx: NopContext) => void;
}

