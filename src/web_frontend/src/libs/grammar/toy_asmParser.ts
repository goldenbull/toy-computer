// Generated from toy_asm.g4 by ANTLR 4.13.2
// noinspection ES6UnusedImports,JSUnusedGlobalSymbols,JSUnusedLocalSymbols

import {
	ATN,
	ATNDeserializer, DecisionState, DFA, FailedPredicateException,
	RecognitionException, NoViableAltException, BailErrorStrategy,
	Parser, ParserATNSimulator,
	RuleContext, ParserRuleContext, PredictionMode, PredictionContextCache,
	TerminalNode, RuleNode,
	Token, TokenStream,
	Interval, IntervalSet
} from 'antlr4';
import toy_asmListener from "./toy_asmListener.js";
import toy_asmVisitor from "./toy_asmVisitor.js";

// for running tests with parameters, TODO: discuss strategy for typed parameters in CI
// eslint-disable-next-line no-unused-vars
type int = number;

export default class toy_asmParser extends Parser {
	public static readonly T__0 = 1;
	public static readonly T__1 = 2;
	public static readonly T__2 = 3;
	public static readonly T__3 = 4;
	public static readonly T__4 = 5;
	public static readonly T__5 = 6;
	public static readonly T__6 = 7;
	public static readonly T__7 = 8;
	public static readonly T__8 = 9;
	public static readonly T__9 = 10;
	public static readonly T__10 = 11;
	public static readonly T__11 = 12;
	public static readonly T__12 = 13;
	public static readonly T__13 = 14;
	public static readonly T__14 = 15;
	public static readonly T__15 = 16;
	public static readonly T__16 = 17;
	public static readonly T__17 = 18;
	public static readonly T__18 = 19;
	public static readonly T__19 = 20;
	public static readonly T__20 = 21;
	public static readonly T__21 = 22;
	public static readonly T__22 = 23;
	public static readonly T__23 = 24;
	public static readonly T__24 = 25;
	public static readonly T__25 = 26;
	public static readonly T__26 = 27;
	public static readonly T__27 = 28;
	public static readonly T__28 = 29;
	public static readonly T__29 = 30;
	public static readonly T__30 = 31;
	public static readonly T__31 = 32;
	public static readonly T__32 = 33;
	public static readonly T__33 = 34;
	public static readonly T__34 = 35;
	public static readonly T__35 = 36;
	public static readonly T__36 = 37;
	public static readonly T__37 = 38;
	public static readonly Comment = 39;
	public static readonly INT = 40;
	public static readonly Label = 41;
	public static readonly STR = 42;
	public static readonly WS = 43;
	public static override readonly EOF = Token.EOF;
	public static readonly RULE_program = 0;
	public static readonly RULE_opLabel = 1;
	public static readonly RULE_op = 2;
	public static readonly RULE_num = 3;
	public static readonly RULE_reg = 4;
	public static readonly RULE_offset = 5;
	public static readonly RULE_mem = 6;
	public static readonly RULE_move = 7;
	public static readonly RULE_add = 8;
	public static readonly RULE_sub = 9;
	public static readonly RULE_mul = 10;
	public static readonly RULE_div = 11;
	public static readonly RULE_cmp = 12;
	public static readonly RULE_jump = 13;
	public static readonly RULE_call = 14;
	public static readonly RULE_ret = 15;
	public static readonly RULE_push = 16;
	public static readonly RULE_pop = 17;
	public static readonly RULE_input = 18;
	public static readonly RULE_str = 19;
	public static readonly RULE_print = 20;
	public static readonly RULE_rand = 21;
	public static readonly RULE_pause = 22;
	public static readonly RULE_halt = 23;
	public static readonly RULE_nop = 24;
	public static readonly literalNames: (string | null)[] = [ null, "':'", 
                                                            "'+'", "'-'", 
                                                            "'ax'", "'bx'", 
                                                            "'cx'", "'dx'", 
                                                            "'bp'", "'sp'", 
                                                            "'['", "']'", 
                                                            "'mov'", "','", 
                                                            "'add'", "'sub'", 
                                                            "'mul'", "'div'", 
                                                            "'cmp'", "'jmp'", 
                                                            "'je'", "'jne'", 
                                                            "'jg'", "'jge'", 
                                                            "'jl'", "'jle'", 
                                                            "'call'", "'ret'", 
                                                            "'push'", "'pushf'", 
                                                            "'pop'", "'popf'", 
                                                            "'input'", "'print'", 
                                                            "'println'", 
                                                            "'rand'", "'pause'", 
                                                            "'halt'", "'nop'" ];
	public static readonly symbolicNames: (string | null)[] = [ null, null, 
                                                             null, null, 
                                                             null, null, 
                                                             null, null, 
                                                             null, null, 
                                                             null, null, 
                                                             null, null, 
                                                             null, null, 
                                                             null, null, 
                                                             null, null, 
                                                             null, null, 
                                                             null, null, 
                                                             null, null, 
                                                             null, null, 
                                                             null, null, 
                                                             null, null, 
                                                             null, null, 
                                                             null, null, 
                                                             null, null, 
                                                             null, "Comment", 
                                                             "INT", "Label", 
                                                             "STR", "WS" ];
	// tslint:disable:no-trailing-whitespace
	public static readonly ruleNames: string[] = [
		"program", "opLabel", "op", "num", "reg", "offset", "mem", "move", "add", 
		"sub", "mul", "div", "cmp", "jump", "call", "ret", "push", "pop", "input", 
		"str", "print", "rand", "pause", "halt", "nop",
	];
	public get grammarFileName(): string { return "toy_asm.g4"; }
	public get literalNames(): (string | null)[] { return toy_asmParser.literalNames; }
	public get symbolicNames(): (string | null)[] { return toy_asmParser.symbolicNames; }
	public get ruleNames(): string[] { return toy_asmParser.ruleNames; }
	public get serializedATN(): number[] { return toy_asmParser._serializedATN; }

	protected createFailedPredicateException(predicate?: string, message?: string): FailedPredicateException {
		return new FailedPredicateException(this, predicate, message);
	}

	constructor(input: TokenStream) {
		super(input);
		this._interp = new ParserATNSimulator(this, toy_asmParser._ATN, toy_asmParser.DecisionsToDFA, new PredictionContextCache());
	}
	// @RuleVersion(0)
	public program(): ProgramContext {
		let localctx: ProgramContext = new ProgramContext(this, this._ctx, this.state);
		this.enterRule(localctx, 0, toy_asmParser.RULE_program);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 55;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			while (((((_la - 12)) & ~0x1F) === 0 && ((1 << (_la - 12)) & 805306365) !== 0)) {
				{
				this.state = 53;
				this._errHandler.sync(this);
				switch (this._input.LA(1)) {
				case 39:
					{
					this.state = 50;
					this.match(toy_asmParser.Comment);
					}
					break;
				case 41:
					{
					this.state = 51;
					this.opLabel();
					}
					break;
				case 12:
				case 14:
				case 15:
				case 16:
				case 17:
				case 18:
				case 19:
				case 20:
				case 21:
				case 22:
				case 23:
				case 24:
				case 25:
				case 26:
				case 27:
				case 28:
				case 29:
				case 30:
				case 31:
				case 32:
				case 33:
				case 34:
				case 35:
				case 36:
				case 37:
				case 38:
					{
					this.state = 52;
					this.op();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				this.state = 57;
				this._errHandler.sync(this);
				_la = this._input.LA(1);
			}
			this.state = 58;
			this.match(toy_asmParser.EOF);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public opLabel(): OpLabelContext {
		let localctx: OpLabelContext = new OpLabelContext(this, this._ctx, this.state);
		this.enterRule(localctx, 2, toy_asmParser.RULE_opLabel);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 60;
			this.match(toy_asmParser.Label);
			this.state = 61;
			this.match(toy_asmParser.T__0);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public op(): OpContext {
		let localctx: OpContext = new OpContext(this, this._ctx, this.state);
		this.enterRule(localctx, 4, toy_asmParser.RULE_op);
		try {
			this.state = 80;
			this._errHandler.sync(this);
			switch (this._input.LA(1)) {
			case 12:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 63;
				this.move();
				}
				break;
			case 14:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 64;
				this.add();
				}
				break;
			case 15:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 65;
				this.sub();
				}
				break;
			case 16:
				this.enterOuterAlt(localctx, 4);
				{
				this.state = 66;
				this.mul();
				}
				break;
			case 17:
				this.enterOuterAlt(localctx, 5);
				{
				this.state = 67;
				this.div();
				}
				break;
			case 18:
				this.enterOuterAlt(localctx, 6);
				{
				this.state = 68;
				this.cmp();
				}
				break;
			case 19:
			case 20:
			case 21:
			case 22:
			case 23:
			case 24:
			case 25:
				this.enterOuterAlt(localctx, 7);
				{
				this.state = 69;
				this.jump();
				}
				break;
			case 26:
				this.enterOuterAlt(localctx, 8);
				{
				this.state = 70;
				this.call();
				}
				break;
			case 27:
				this.enterOuterAlt(localctx, 9);
				{
				this.state = 71;
				this.ret();
				}
				break;
			case 28:
			case 29:
				this.enterOuterAlt(localctx, 10);
				{
				this.state = 72;
				this.push();
				}
				break;
			case 30:
			case 31:
				this.enterOuterAlt(localctx, 11);
				{
				this.state = 73;
				this.pop();
				}
				break;
			case 32:
				this.enterOuterAlt(localctx, 12);
				{
				this.state = 74;
				this.input();
				}
				break;
			case 33:
			case 34:
				this.enterOuterAlt(localctx, 13);
				{
				this.state = 75;
				this.print();
				}
				break;
			case 35:
				this.enterOuterAlt(localctx, 14);
				{
				this.state = 76;
				this.rand();
				}
				break;
			case 36:
				this.enterOuterAlt(localctx, 15);
				{
				this.state = 77;
				this.pause();
				}
				break;
			case 37:
				this.enterOuterAlt(localctx, 16);
				{
				this.state = 78;
				this.halt();
				}
				break;
			case 38:
				this.enterOuterAlt(localctx, 17);
				{
				this.state = 79;
				this.nop();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public num(): NumContext {
		let localctx: NumContext = new NumContext(this, this._ctx, this.state);
		this.enterRule(localctx, 6, toy_asmParser.RULE_num);
		let _la: number;
		try {
			this.state = 88;
			this._errHandler.sync(this);
			switch (this._input.LA(1)) {
			case 2:
			case 40:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 83;
				this._errHandler.sync(this);
				_la = this._input.LA(1);
				if (_la===2) {
					{
					this.state = 82;
					this.match(toy_asmParser.T__1);
					}
				}

				this.state = 85;
				this.match(toy_asmParser.INT);
				}
				break;
			case 3:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 86;
				this.match(toy_asmParser.T__2);
				this.state = 87;
				this.match(toy_asmParser.INT);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public reg(): RegContext {
		let localctx: RegContext = new RegContext(this, this._ctx, this.state);
		this.enterRule(localctx, 8, toy_asmParser.RULE_reg);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 90;
			_la = this._input.LA(1);
			if(!((((_la) & ~0x1F) === 0 && ((1 << _la) & 1008) !== 0))) {
			this._errHandler.recoverInline(this);
			}
			else {
				this._errHandler.reportMatch(this);
			    this.consume();
			}
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public offset(): OffsetContext {
		let localctx: OffsetContext = new OffsetContext(this, this._ctx, this.state);
		this.enterRule(localctx, 10, toy_asmParser.RULE_offset);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 92;
			_la = this._input.LA(1);
			if(!(_la===2 || _la===3)) {
			this._errHandler.recoverInline(this);
			}
			else {
				this._errHandler.reportMatch(this);
			    this.consume();
			}
			this.state = 93;
			this.match(toy_asmParser.INT);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public mem(): MemContext {
		let localctx: MemContext = new MemContext(this, this._ctx, this.state);
		this.enterRule(localctx, 12, toy_asmParser.RULE_mem);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 95;
			this.match(toy_asmParser.T__9);
			this.state = 96;
			this.reg();
			this.state = 98;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===2 || _la===3) {
				{
				this.state = 97;
				this.offset();
				}
			}

			this.state = 100;
			this.match(toy_asmParser.T__10);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public move(): MoveContext {
		let localctx: MoveContext = new MoveContext(this, this._ctx, this.state);
		this.enterRule(localctx, 14, toy_asmParser.RULE_move);
		try {
			this.state = 127;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 6, this._ctx) ) {
			case 1:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 102;
				this.match(toy_asmParser.T__11);
				this.state = 103;
				this.reg();
				this.state = 104;
				this.match(toy_asmParser.T__12);
				this.state = 105;
				this.num();
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 107;
				this.match(toy_asmParser.T__11);
				this.state = 108;
				this.reg();
				this.state = 109;
				this.match(toy_asmParser.T__12);
				this.state = 110;
				this.reg();
				}
				break;
			case 3:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 112;
				this.match(toy_asmParser.T__11);
				this.state = 113;
				this.reg();
				this.state = 114;
				this.match(toy_asmParser.T__12);
				this.state = 115;
				this.mem();
				}
				break;
			case 4:
				this.enterOuterAlt(localctx, 4);
				{
				this.state = 117;
				this.match(toy_asmParser.T__11);
				this.state = 118;
				this.mem();
				this.state = 119;
				this.match(toy_asmParser.T__12);
				this.state = 120;
				this.num();
				}
				break;
			case 5:
				this.enterOuterAlt(localctx, 5);
				{
				this.state = 122;
				this.match(toy_asmParser.T__11);
				this.state = 123;
				this.mem();
				this.state = 124;
				this.match(toy_asmParser.T__12);
				this.state = 125;
				this.reg();
				}
				break;
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public add(): AddContext {
		let localctx: AddContext = new AddContext(this, this._ctx, this.state);
		this.enterRule(localctx, 16, toy_asmParser.RULE_add);
		try {
			this.state = 144;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 7, this._ctx) ) {
			case 1:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 129;
				this.match(toy_asmParser.T__13);
				this.state = 130;
				this.reg();
				this.state = 131;
				this.match(toy_asmParser.T__12);
				this.state = 132;
				this.num();
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 134;
				this.match(toy_asmParser.T__13);
				this.state = 135;
				this.reg();
				this.state = 136;
				this.match(toy_asmParser.T__12);
				this.state = 137;
				this.reg();
				}
				break;
			case 3:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 139;
				this.match(toy_asmParser.T__13);
				this.state = 140;
				this.reg();
				this.state = 141;
				this.match(toy_asmParser.T__12);
				this.state = 142;
				this.mem();
				}
				break;
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public sub(): SubContext {
		let localctx: SubContext = new SubContext(this, this._ctx, this.state);
		this.enterRule(localctx, 18, toy_asmParser.RULE_sub);
		try {
			this.state = 161;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 8, this._ctx) ) {
			case 1:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 146;
				this.match(toy_asmParser.T__14);
				this.state = 147;
				this.reg();
				this.state = 148;
				this.match(toy_asmParser.T__12);
				this.state = 149;
				this.num();
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 151;
				this.match(toy_asmParser.T__14);
				this.state = 152;
				this.reg();
				this.state = 153;
				this.match(toy_asmParser.T__12);
				this.state = 154;
				this.reg();
				}
				break;
			case 3:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 156;
				this.match(toy_asmParser.T__14);
				this.state = 157;
				this.reg();
				this.state = 158;
				this.match(toy_asmParser.T__12);
				this.state = 159;
				this.mem();
				}
				break;
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public mul(): MulContext {
		let localctx: MulContext = new MulContext(this, this._ctx, this.state);
		this.enterRule(localctx, 20, toy_asmParser.RULE_mul);
		try {
			this.state = 169;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 9, this._ctx) ) {
			case 1:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 163;
				this.match(toy_asmParser.T__15);
				this.state = 164;
				this.num();
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 165;
				this.match(toy_asmParser.T__15);
				this.state = 166;
				this.reg();
				}
				break;
			case 3:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 167;
				this.match(toy_asmParser.T__15);
				this.state = 168;
				this.mem();
				}
				break;
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public div(): DivContext {
		let localctx: DivContext = new DivContext(this, this._ctx, this.state);
		this.enterRule(localctx, 22, toy_asmParser.RULE_div);
		try {
			this.state = 177;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 10, this._ctx) ) {
			case 1:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 171;
				this.match(toy_asmParser.T__16);
				this.state = 172;
				this.num();
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 173;
				this.match(toy_asmParser.T__16);
				this.state = 174;
				this.reg();
				}
				break;
			case 3:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 175;
				this.match(toy_asmParser.T__16);
				this.state = 176;
				this.mem();
				}
				break;
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public cmp(): CmpContext {
		let localctx: CmpContext = new CmpContext(this, this._ctx, this.state);
		this.enterRule(localctx, 24, toy_asmParser.RULE_cmp);
		try {
			this.state = 194;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 11, this._ctx) ) {
			case 1:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 179;
				this.match(toy_asmParser.T__17);
				this.state = 180;
				this.reg();
				this.state = 181;
				this.match(toy_asmParser.T__12);
				this.state = 182;
				this.num();
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 184;
				this.match(toy_asmParser.T__17);
				this.state = 185;
				this.reg();
				this.state = 186;
				this.match(toy_asmParser.T__12);
				this.state = 187;
				this.reg();
				}
				break;
			case 3:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 189;
				this.match(toy_asmParser.T__17);
				this.state = 190;
				this.reg();
				this.state = 191;
				this.match(toy_asmParser.T__12);
				this.state = 192;
				this.mem();
				}
				break;
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public jump(): JumpContext {
		let localctx: JumpContext = new JumpContext(this, this._ctx, this.state);
		this.enterRule(localctx, 26, toy_asmParser.RULE_jump);
		try {
			this.state = 210;
			this._errHandler.sync(this);
			switch (this._input.LA(1)) {
			case 19:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 196;
				this.match(toy_asmParser.T__18);
				this.state = 197;
				this.match(toy_asmParser.Label);
				}
				break;
			case 20:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 198;
				this.match(toy_asmParser.T__19);
				this.state = 199;
				this.match(toy_asmParser.Label);
				}
				break;
			case 21:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 200;
				this.match(toy_asmParser.T__20);
				this.state = 201;
				this.match(toy_asmParser.Label);
				}
				break;
			case 22:
				this.enterOuterAlt(localctx, 4);
				{
				this.state = 202;
				this.match(toy_asmParser.T__21);
				this.state = 203;
				this.match(toy_asmParser.Label);
				}
				break;
			case 23:
				this.enterOuterAlt(localctx, 5);
				{
				this.state = 204;
				this.match(toy_asmParser.T__22);
				this.state = 205;
				this.match(toy_asmParser.Label);
				}
				break;
			case 24:
				this.enterOuterAlt(localctx, 6);
				{
				this.state = 206;
				this.match(toy_asmParser.T__23);
				this.state = 207;
				this.match(toy_asmParser.Label);
				}
				break;
			case 25:
				this.enterOuterAlt(localctx, 7);
				{
				this.state = 208;
				this.match(toy_asmParser.T__24);
				this.state = 209;
				this.match(toy_asmParser.Label);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public call(): CallContext {
		let localctx: CallContext = new CallContext(this, this._ctx, this.state);
		this.enterRule(localctx, 28, toy_asmParser.RULE_call);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 212;
			this.match(toy_asmParser.T__25);
			this.state = 213;
			this.match(toy_asmParser.Label);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public ret(): RetContext {
		let localctx: RetContext = new RetContext(this, this._ctx, this.state);
		this.enterRule(localctx, 30, toy_asmParser.RULE_ret);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 215;
			this.match(toy_asmParser.T__26);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public push(): PushContext {
		let localctx: PushContext = new PushContext(this, this._ctx, this.state);
		this.enterRule(localctx, 32, toy_asmParser.RULE_push);
		try {
			this.state = 222;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 13, this._ctx) ) {
			case 1:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 217;
				this.match(toy_asmParser.T__27);
				this.state = 218;
				this.num();
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 219;
				this.match(toy_asmParser.T__27);
				this.state = 220;
				this.reg();
				}
				break;
			case 3:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 221;
				this.match(toy_asmParser.T__28);
				}
				break;
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public pop(): PopContext {
		let localctx: PopContext = new PopContext(this, this._ctx, this.state);
		this.enterRule(localctx, 34, toy_asmParser.RULE_pop);
		try {
			this.state = 228;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 14, this._ctx) ) {
			case 1:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 224;
				this.match(toy_asmParser.T__29);
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 225;
				this.match(toy_asmParser.T__29);
				this.state = 226;
				this.reg();
				}
				break;
			case 3:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 227;
				this.match(toy_asmParser.T__30);
				}
				break;
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public input(): InputContext {
		let localctx: InputContext = new InputContext(this, this._ctx, this.state);
		this.enterRule(localctx, 36, toy_asmParser.RULE_input);
		try {
			this.state = 234;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 15, this._ctx) ) {
			case 1:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 230;
				this.match(toy_asmParser.T__31);
				this.state = 231;
				this.reg();
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 232;
				this.match(toy_asmParser.T__31);
				this.state = 233;
				this.mem();
				}
				break;
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public str(): StrContext {
		let localctx: StrContext = new StrContext(this, this._ctx, this.state);
		this.enterRule(localctx, 38, toy_asmParser.RULE_str);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 236;
			this.match(toy_asmParser.STR);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public print(): PrintContext {
		let localctx: PrintContext = new PrintContext(this, this._ctx, this.state);
		this.enterRule(localctx, 40, toy_asmParser.RULE_print);
		try {
			this.state = 255;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 16, this._ctx) ) {
			case 1:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 238;
				this.match(toy_asmParser.T__32);
				this.state = 239;
				this.num();
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 240;
				this.match(toy_asmParser.T__32);
				this.state = 241;
				this.reg();
				}
				break;
			case 3:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 242;
				this.match(toy_asmParser.T__32);
				this.state = 243;
				this.mem();
				}
				break;
			case 4:
				this.enterOuterAlt(localctx, 4);
				{
				this.state = 244;
				this.match(toy_asmParser.T__32);
				this.state = 245;
				this.str();
				}
				break;
			case 5:
				this.enterOuterAlt(localctx, 5);
				{
				this.state = 246;
				this.match(toy_asmParser.T__33);
				this.state = 247;
				this.num();
				}
				break;
			case 6:
				this.enterOuterAlt(localctx, 6);
				{
				this.state = 248;
				this.match(toy_asmParser.T__33);
				this.state = 249;
				this.reg();
				}
				break;
			case 7:
				this.enterOuterAlt(localctx, 7);
				{
				this.state = 250;
				this.match(toy_asmParser.T__33);
				this.state = 251;
				this.mem();
				}
				break;
			case 8:
				this.enterOuterAlt(localctx, 8);
				{
				this.state = 252;
				this.match(toy_asmParser.T__33);
				this.state = 253;
				this.str();
				}
				break;
			case 9:
				this.enterOuterAlt(localctx, 9);
				{
				this.state = 254;
				this.match(toy_asmParser.T__33);
				}
				break;
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public rand(): RandContext {
		let localctx: RandContext = new RandContext(this, this._ctx, this.state);
		this.enterRule(localctx, 42, toy_asmParser.RULE_rand);
		try {
			this.state = 261;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 17, this._ctx) ) {
			case 1:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 257;
				this.match(toy_asmParser.T__34);
				this.state = 258;
				this.reg();
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 259;
				this.match(toy_asmParser.T__34);
				this.state = 260;
				this.mem();
				}
				break;
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public pause(): PauseContext {
		let localctx: PauseContext = new PauseContext(this, this._ctx, this.state);
		this.enterRule(localctx, 44, toy_asmParser.RULE_pause);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 263;
			this.match(toy_asmParser.T__35);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public halt(): HaltContext {
		let localctx: HaltContext = new HaltContext(this, this._ctx, this.state);
		this.enterRule(localctx, 46, toy_asmParser.RULE_halt);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 265;
			this.match(toy_asmParser.T__36);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}
	// @RuleVersion(0)
	public nop(): NopContext {
		let localctx: NopContext = new NopContext(this, this._ctx, this.state);
		this.enterRule(localctx, 48, toy_asmParser.RULE_nop);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 267;
			this.match(toy_asmParser.T__37);
			}
		}
		catch (re) {
			if (re instanceof RecognitionException) {
				localctx.exception = re;
				this._errHandler.reportError(this, re);
				this._errHandler.recover(this, re);
			} else {
				throw re;
			}
		}
		finally {
			this.exitRule();
		}
		return localctx;
	}

	public static readonly _serializedATN: number[] = [4,1,43,270,2,0,7,0,2,
	1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,
	10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,
	7,17,2,18,7,18,2,19,7,19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,
	24,1,0,1,0,1,0,5,0,54,8,0,10,0,12,0,57,9,0,1,0,1,0,1,1,1,1,1,1,1,2,1,2,
	1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,81,8,2,
	1,3,3,3,84,8,3,1,3,1,3,1,3,3,3,89,8,3,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,3,
	6,99,8,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
	7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,128,8,7,1,8,1,8,1,8,1,
	8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,145,8,8,1,9,1,9,1,9,1,
	9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,162,8,9,1,10,1,10,1,10,
	1,10,1,10,1,10,3,10,170,8,10,1,11,1,11,1,11,1,11,1,11,1,11,3,11,178,8,11,
	1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,
	12,3,12,195,8,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
	1,13,1,13,1,13,3,13,211,8,13,1,14,1,14,1,14,1,15,1,15,1,16,1,16,1,16,1,
	16,1,16,3,16,223,8,16,1,17,1,17,1,17,1,17,3,17,229,8,17,1,18,1,18,1,18,
	1,18,3,18,235,8,18,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,
	20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,256,8,20,1,21,1,21,1,21,
	1,21,3,21,262,8,21,1,22,1,22,1,23,1,23,1,24,1,24,1,24,0,0,25,0,2,4,6,8,
	10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,0,2,1,0,4,9,
	1,0,2,3,300,0,55,1,0,0,0,2,60,1,0,0,0,4,80,1,0,0,0,6,88,1,0,0,0,8,90,1,
	0,0,0,10,92,1,0,0,0,12,95,1,0,0,0,14,127,1,0,0,0,16,144,1,0,0,0,18,161,
	1,0,0,0,20,169,1,0,0,0,22,177,1,0,0,0,24,194,1,0,0,0,26,210,1,0,0,0,28,
	212,1,0,0,0,30,215,1,0,0,0,32,222,1,0,0,0,34,228,1,0,0,0,36,234,1,0,0,0,
	38,236,1,0,0,0,40,255,1,0,0,0,42,261,1,0,0,0,44,263,1,0,0,0,46,265,1,0,
	0,0,48,267,1,0,0,0,50,54,5,39,0,0,51,54,3,2,1,0,52,54,3,4,2,0,53,50,1,0,
	0,0,53,51,1,0,0,0,53,52,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,
	0,56,58,1,0,0,0,57,55,1,0,0,0,58,59,5,0,0,1,59,1,1,0,0,0,60,61,5,41,0,0,
	61,62,5,1,0,0,62,3,1,0,0,0,63,81,3,14,7,0,64,81,3,16,8,0,65,81,3,18,9,0,
	66,81,3,20,10,0,67,81,3,22,11,0,68,81,3,24,12,0,69,81,3,26,13,0,70,81,3,
	28,14,0,71,81,3,30,15,0,72,81,3,32,16,0,73,81,3,34,17,0,74,81,3,36,18,0,
	75,81,3,40,20,0,76,81,3,42,21,0,77,81,3,44,22,0,78,81,3,46,23,0,79,81,3,
	48,24,0,80,63,1,0,0,0,80,64,1,0,0,0,80,65,1,0,0,0,80,66,1,0,0,0,80,67,1,
	0,0,0,80,68,1,0,0,0,80,69,1,0,0,0,80,70,1,0,0,0,80,71,1,0,0,0,80,72,1,0,
	0,0,80,73,1,0,0,0,80,74,1,0,0,0,80,75,1,0,0,0,80,76,1,0,0,0,80,77,1,0,0,
	0,80,78,1,0,0,0,80,79,1,0,0,0,81,5,1,0,0,0,82,84,5,2,0,0,83,82,1,0,0,0,
	83,84,1,0,0,0,84,85,1,0,0,0,85,89,5,40,0,0,86,87,5,3,0,0,87,89,5,40,0,0,
	88,83,1,0,0,0,88,86,1,0,0,0,89,7,1,0,0,0,90,91,7,0,0,0,91,9,1,0,0,0,92,
	93,7,1,0,0,93,94,5,40,0,0,94,11,1,0,0,0,95,96,5,10,0,0,96,98,3,8,4,0,97,
	99,3,10,5,0,98,97,1,0,0,0,98,99,1,0,0,0,99,100,1,0,0,0,100,101,5,11,0,0,
	101,13,1,0,0,0,102,103,5,12,0,0,103,104,3,8,4,0,104,105,5,13,0,0,105,106,
	3,6,3,0,106,128,1,0,0,0,107,108,5,12,0,0,108,109,3,8,4,0,109,110,5,13,0,
	0,110,111,3,8,4,0,111,128,1,0,0,0,112,113,5,12,0,0,113,114,3,8,4,0,114,
	115,5,13,0,0,115,116,3,12,6,0,116,128,1,0,0,0,117,118,5,12,0,0,118,119,
	3,12,6,0,119,120,5,13,0,0,120,121,3,6,3,0,121,128,1,0,0,0,122,123,5,12,
	0,0,123,124,3,12,6,0,124,125,5,13,0,0,125,126,3,8,4,0,126,128,1,0,0,0,127,
	102,1,0,0,0,127,107,1,0,0,0,127,112,1,0,0,0,127,117,1,0,0,0,127,122,1,0,
	0,0,128,15,1,0,0,0,129,130,5,14,0,0,130,131,3,8,4,0,131,132,5,13,0,0,132,
	133,3,6,3,0,133,145,1,0,0,0,134,135,5,14,0,0,135,136,3,8,4,0,136,137,5,
	13,0,0,137,138,3,8,4,0,138,145,1,0,0,0,139,140,5,14,0,0,140,141,3,8,4,0,
	141,142,5,13,0,0,142,143,3,12,6,0,143,145,1,0,0,0,144,129,1,0,0,0,144,134,
	1,0,0,0,144,139,1,0,0,0,145,17,1,0,0,0,146,147,5,15,0,0,147,148,3,8,4,0,
	148,149,5,13,0,0,149,150,3,6,3,0,150,162,1,0,0,0,151,152,5,15,0,0,152,153,
	3,8,4,0,153,154,5,13,0,0,154,155,3,8,4,0,155,162,1,0,0,0,156,157,5,15,0,
	0,157,158,3,8,4,0,158,159,5,13,0,0,159,160,3,12,6,0,160,162,1,0,0,0,161,
	146,1,0,0,0,161,151,1,0,0,0,161,156,1,0,0,0,162,19,1,0,0,0,163,164,5,16,
	0,0,164,170,3,6,3,0,165,166,5,16,0,0,166,170,3,8,4,0,167,168,5,16,0,0,168,
	170,3,12,6,0,169,163,1,0,0,0,169,165,1,0,0,0,169,167,1,0,0,0,170,21,1,0,
	0,0,171,172,5,17,0,0,172,178,3,6,3,0,173,174,5,17,0,0,174,178,3,8,4,0,175,
	176,5,17,0,0,176,178,3,12,6,0,177,171,1,0,0,0,177,173,1,0,0,0,177,175,1,
	0,0,0,178,23,1,0,0,0,179,180,5,18,0,0,180,181,3,8,4,0,181,182,5,13,0,0,
	182,183,3,6,3,0,183,195,1,0,0,0,184,185,5,18,0,0,185,186,3,8,4,0,186,187,
	5,13,0,0,187,188,3,8,4,0,188,195,1,0,0,0,189,190,5,18,0,0,190,191,3,8,4,
	0,191,192,5,13,0,0,192,193,3,12,6,0,193,195,1,0,0,0,194,179,1,0,0,0,194,
	184,1,0,0,0,194,189,1,0,0,0,195,25,1,0,0,0,196,197,5,19,0,0,197,211,5,41,
	0,0,198,199,5,20,0,0,199,211,5,41,0,0,200,201,5,21,0,0,201,211,5,41,0,0,
	202,203,5,22,0,0,203,211,5,41,0,0,204,205,5,23,0,0,205,211,5,41,0,0,206,
	207,5,24,0,0,207,211,5,41,0,0,208,209,5,25,0,0,209,211,5,41,0,0,210,196,
	1,0,0,0,210,198,1,0,0,0,210,200,1,0,0,0,210,202,1,0,0,0,210,204,1,0,0,0,
	210,206,1,0,0,0,210,208,1,0,0,0,211,27,1,0,0,0,212,213,5,26,0,0,213,214,
	5,41,0,0,214,29,1,0,0,0,215,216,5,27,0,0,216,31,1,0,0,0,217,218,5,28,0,
	0,218,223,3,6,3,0,219,220,5,28,0,0,220,223,3,8,4,0,221,223,5,29,0,0,222,
	217,1,0,0,0,222,219,1,0,0,0,222,221,1,0,0,0,223,33,1,0,0,0,224,229,5,30,
	0,0,225,226,5,30,0,0,226,229,3,8,4,0,227,229,5,31,0,0,228,224,1,0,0,0,228,
	225,1,0,0,0,228,227,1,0,0,0,229,35,1,0,0,0,230,231,5,32,0,0,231,235,3,8,
	4,0,232,233,5,32,0,0,233,235,3,12,6,0,234,230,1,0,0,0,234,232,1,0,0,0,235,
	37,1,0,0,0,236,237,5,42,0,0,237,39,1,0,0,0,238,239,5,33,0,0,239,256,3,6,
	3,0,240,241,5,33,0,0,241,256,3,8,4,0,242,243,5,33,0,0,243,256,3,12,6,0,
	244,245,5,33,0,0,245,256,3,38,19,0,246,247,5,34,0,0,247,256,3,6,3,0,248,
	249,5,34,0,0,249,256,3,8,4,0,250,251,5,34,0,0,251,256,3,12,6,0,252,253,
	5,34,0,0,253,256,3,38,19,0,254,256,5,34,0,0,255,238,1,0,0,0,255,240,1,0,
	0,0,255,242,1,0,0,0,255,244,1,0,0,0,255,246,1,0,0,0,255,248,1,0,0,0,255,
	250,1,0,0,0,255,252,1,0,0,0,255,254,1,0,0,0,256,41,1,0,0,0,257,258,5,35,
	0,0,258,262,3,8,4,0,259,260,5,35,0,0,260,262,3,12,6,0,261,257,1,0,0,0,261,
	259,1,0,0,0,262,43,1,0,0,0,263,264,5,36,0,0,264,45,1,0,0,0,265,266,5,37,
	0,0,266,47,1,0,0,0,267,268,5,38,0,0,268,49,1,0,0,0,18,53,55,80,83,88,98,
	127,144,161,169,177,194,210,222,228,234,255,261];

	private static __ATN: ATN;
	public static get _ATN(): ATN {
		if (!toy_asmParser.__ATN) {
			toy_asmParser.__ATN = new ATNDeserializer().deserialize(toy_asmParser._serializedATN);
		}

		return toy_asmParser.__ATN;
	}


	static DecisionsToDFA = toy_asmParser._ATN.decisionToState.map( (ds: DecisionState, index: number) => new DFA(ds, index) );

}

export class ProgramContext extends ParserRuleContext {
	constructor(parser?: toy_asmParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public EOF(): TerminalNode {
		return this.getToken(toy_asmParser.EOF, 0);
	}
	public Comment_list(): TerminalNode[] {
	    	return this.getTokens(toy_asmParser.Comment);
	}
	public Comment(i: number): TerminalNode {
		return this.getToken(toy_asmParser.Comment, i);
	}
	public opLabel_list(): OpLabelContext[] {
		return this.getTypedRuleContexts(OpLabelContext) as OpLabelContext[];
	}
	public opLabel(i: number): OpLabelContext {
		return this.getTypedRuleContext(OpLabelContext, i) as OpLabelContext;
	}
	public op_list(): OpContext[] {
		return this.getTypedRuleContexts(OpContext) as OpContext[];
	}
	public op(i: number): OpContext {
		return this.getTypedRuleContext(OpContext, i) as OpContext;
	}
    public get ruleIndex(): number {
    	return toy_asmParser.RULE_program;
	}
	public enterRule(listener: toy_asmListener): void {
	    if(listener.enterProgram) {
	 		listener.enterProgram(this);
		}
	}
	public exitRule(listener: toy_asmListener): void {
	    if(listener.exitProgram) {
	 		listener.exitProgram(this);
		}
	}
	// @Override
	public accept<Result>(visitor: toy_asmVisitor<Result>): Result {
		if (visitor.visitProgram) {
			return visitor.visitProgram(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class OpLabelContext extends ParserRuleContext {
	constructor(parser?: toy_asmParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public Label(): TerminalNode {
		return this.getToken(toy_asmParser.Label, 0);
	}
    public get ruleIndex(): number {
    	return toy_asmParser.RULE_opLabel;
	}
	public enterRule(listener: toy_asmListener): void {
	    if(listener.enterOpLabel) {
	 		listener.enterOpLabel(this);
		}
	}
	public exitRule(listener: toy_asmListener): void {
	    if(listener.exitOpLabel) {
	 		listener.exitOpLabel(this);
		}
	}
	// @Override
	public accept<Result>(visitor: toy_asmVisitor<Result>): Result {
		if (visitor.visitOpLabel) {
			return visitor.visitOpLabel(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class OpContext extends ParserRuleContext {
	constructor(parser?: toy_asmParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public move(): MoveContext {
		return this.getTypedRuleContext(MoveContext, 0) as MoveContext;
	}
	public add(): AddContext {
		return this.getTypedRuleContext(AddContext, 0) as AddContext;
	}
	public sub(): SubContext {
		return this.getTypedRuleContext(SubContext, 0) as SubContext;
	}
	public mul(): MulContext {
		return this.getTypedRuleContext(MulContext, 0) as MulContext;
	}
	public div(): DivContext {
		return this.getTypedRuleContext(DivContext, 0) as DivContext;
	}
	public cmp(): CmpContext {
		return this.getTypedRuleContext(CmpContext, 0) as CmpContext;
	}
	public jump(): JumpContext {
		return this.getTypedRuleContext(JumpContext, 0) as JumpContext;
	}
	public call(): CallContext {
		return this.getTypedRuleContext(CallContext, 0) as CallContext;
	}
	public ret(): RetContext {
		return this.getTypedRuleContext(RetContext, 0) as RetContext;
	}
	public push(): PushContext {
		return this.getTypedRuleContext(PushContext, 0) as PushContext;
	}
	public pop(): PopContext {
		return this.getTypedRuleContext(PopContext, 0) as PopContext;
	}
	public input(): InputContext {
		return this.getTypedRuleContext(InputContext, 0) as InputContext;
	}
	public print(): PrintContext {
		return this.getTypedRuleContext(PrintContext, 0) as PrintContext;
	}
	public rand(): RandContext {
		return this.getTypedRuleContext(RandContext, 0) as RandContext;
	}
	public pause(): PauseContext {
		return this.getTypedRuleContext(PauseContext, 0) as PauseContext;
	}
	public halt(): HaltContext {
		return this.getTypedRuleContext(HaltContext, 0) as HaltContext;
	}
	public nop(): NopContext {
		return this.getTypedRuleContext(NopContext, 0) as NopContext;
	}
    public get ruleIndex(): number {
    	return toy_asmParser.RULE_op;
	}
	public enterRule(listener: toy_asmListener): void {
	    if(listener.enterOp) {
	 		listener.enterOp(this);
		}
	}
	public exitRule(listener: toy_asmListener): void {
	    if(listener.exitOp) {
	 		listener.exitOp(this);
		}
	}
	// @Override
	public accept<Result>(visitor: toy_asmVisitor<Result>): Result {
		if (visitor.visitOp) {
			return visitor.visitOp(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class NumContext extends ParserRuleContext {
	constructor(parser?: toy_asmParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public INT(): TerminalNode {
		return this.getToken(toy_asmParser.INT, 0);
	}
    public get ruleIndex(): number {
    	return toy_asmParser.RULE_num;
	}
	public enterRule(listener: toy_asmListener): void {
	    if(listener.enterNum) {
	 		listener.enterNum(this);
		}
	}
	public exitRule(listener: toy_asmListener): void {
	    if(listener.exitNum) {
	 		listener.exitNum(this);
		}
	}
	// @Override
	public accept<Result>(visitor: toy_asmVisitor<Result>): Result {
		if (visitor.visitNum) {
			return visitor.visitNum(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class RegContext extends ParserRuleContext {
	constructor(parser?: toy_asmParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
    public get ruleIndex(): number {
    	return toy_asmParser.RULE_reg;
	}
	public enterRule(listener: toy_asmListener): void {
	    if(listener.enterReg) {
	 		listener.enterReg(this);
		}
	}
	public exitRule(listener: toy_asmListener): void {
	    if(listener.exitReg) {
	 		listener.exitReg(this);
		}
	}
	// @Override
	public accept<Result>(visitor: toy_asmVisitor<Result>): Result {
		if (visitor.visitReg) {
			return visitor.visitReg(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class OffsetContext extends ParserRuleContext {
	constructor(parser?: toy_asmParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public INT(): TerminalNode {
		return this.getToken(toy_asmParser.INT, 0);
	}
    public get ruleIndex(): number {
    	return toy_asmParser.RULE_offset;
	}
	public enterRule(listener: toy_asmListener): void {
	    if(listener.enterOffset) {
	 		listener.enterOffset(this);
		}
	}
	public exitRule(listener: toy_asmListener): void {
	    if(listener.exitOffset) {
	 		listener.exitOffset(this);
		}
	}
	// @Override
	public accept<Result>(visitor: toy_asmVisitor<Result>): Result {
		if (visitor.visitOffset) {
			return visitor.visitOffset(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class MemContext extends ParserRuleContext {
	constructor(parser?: toy_asmParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public reg(): RegContext {
		return this.getTypedRuleContext(RegContext, 0) as RegContext;
	}
	public offset(): OffsetContext {
		return this.getTypedRuleContext(OffsetContext, 0) as OffsetContext;
	}
    public get ruleIndex(): number {
    	return toy_asmParser.RULE_mem;
	}
	public enterRule(listener: toy_asmListener): void {
	    if(listener.enterMem) {
	 		listener.enterMem(this);
		}
	}
	public exitRule(listener: toy_asmListener): void {
	    if(listener.exitMem) {
	 		listener.exitMem(this);
		}
	}
	// @Override
	public accept<Result>(visitor: toy_asmVisitor<Result>): Result {
		if (visitor.visitMem) {
			return visitor.visitMem(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class MoveContext extends ParserRuleContext {
	constructor(parser?: toy_asmParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public reg_list(): RegContext[] {
		return this.getTypedRuleContexts(RegContext) as RegContext[];
	}
	public reg(i: number): RegContext {
		return this.getTypedRuleContext(RegContext, i) as RegContext;
	}
	public num(): NumContext {
		return this.getTypedRuleContext(NumContext, 0) as NumContext;
	}
	public mem(): MemContext {
		return this.getTypedRuleContext(MemContext, 0) as MemContext;
	}
    public get ruleIndex(): number {
    	return toy_asmParser.RULE_move;
	}
	public enterRule(listener: toy_asmListener): void {
	    if(listener.enterMove) {
	 		listener.enterMove(this);
		}
	}
	public exitRule(listener: toy_asmListener): void {
	    if(listener.exitMove) {
	 		listener.exitMove(this);
		}
	}
	// @Override
	public accept<Result>(visitor: toy_asmVisitor<Result>): Result {
		if (visitor.visitMove) {
			return visitor.visitMove(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class AddContext extends ParserRuleContext {
	constructor(parser?: toy_asmParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public reg_list(): RegContext[] {
		return this.getTypedRuleContexts(RegContext) as RegContext[];
	}
	public reg(i: number): RegContext {
		return this.getTypedRuleContext(RegContext, i) as RegContext;
	}
	public num(): NumContext {
		return this.getTypedRuleContext(NumContext, 0) as NumContext;
	}
	public mem(): MemContext {
		return this.getTypedRuleContext(MemContext, 0) as MemContext;
	}
    public get ruleIndex(): number {
    	return toy_asmParser.RULE_add;
	}
	public enterRule(listener: toy_asmListener): void {
	    if(listener.enterAdd) {
	 		listener.enterAdd(this);
		}
	}
	public exitRule(listener: toy_asmListener): void {
	    if(listener.exitAdd) {
	 		listener.exitAdd(this);
		}
	}
	// @Override
	public accept<Result>(visitor: toy_asmVisitor<Result>): Result {
		if (visitor.visitAdd) {
			return visitor.visitAdd(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class SubContext extends ParserRuleContext {
	constructor(parser?: toy_asmParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public reg_list(): RegContext[] {
		return this.getTypedRuleContexts(RegContext) as RegContext[];
	}
	public reg(i: number): RegContext {
		return this.getTypedRuleContext(RegContext, i) as RegContext;
	}
	public num(): NumContext {
		return this.getTypedRuleContext(NumContext, 0) as NumContext;
	}
	public mem(): MemContext {
		return this.getTypedRuleContext(MemContext, 0) as MemContext;
	}
    public get ruleIndex(): number {
    	return toy_asmParser.RULE_sub;
	}
	public enterRule(listener: toy_asmListener): void {
	    if(listener.enterSub) {
	 		listener.enterSub(this);
		}
	}
	public exitRule(listener: toy_asmListener): void {
	    if(listener.exitSub) {
	 		listener.exitSub(this);
		}
	}
	// @Override
	public accept<Result>(visitor: toy_asmVisitor<Result>): Result {
		if (visitor.visitSub) {
			return visitor.visitSub(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class MulContext extends ParserRuleContext {
	constructor(parser?: toy_asmParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public num(): NumContext {
		return this.getTypedRuleContext(NumContext, 0) as NumContext;
	}
	public reg(): RegContext {
		return this.getTypedRuleContext(RegContext, 0) as RegContext;
	}
	public mem(): MemContext {
		return this.getTypedRuleContext(MemContext, 0) as MemContext;
	}
    public get ruleIndex(): number {
    	return toy_asmParser.RULE_mul;
	}
	public enterRule(listener: toy_asmListener): void {
	    if(listener.enterMul) {
	 		listener.enterMul(this);
		}
	}
	public exitRule(listener: toy_asmListener): void {
	    if(listener.exitMul) {
	 		listener.exitMul(this);
		}
	}
	// @Override
	public accept<Result>(visitor: toy_asmVisitor<Result>): Result {
		if (visitor.visitMul) {
			return visitor.visitMul(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class DivContext extends ParserRuleContext {
	constructor(parser?: toy_asmParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public num(): NumContext {
		return this.getTypedRuleContext(NumContext, 0) as NumContext;
	}
	public reg(): RegContext {
		return this.getTypedRuleContext(RegContext, 0) as RegContext;
	}
	public mem(): MemContext {
		return this.getTypedRuleContext(MemContext, 0) as MemContext;
	}
    public get ruleIndex(): number {
    	return toy_asmParser.RULE_div;
	}
	public enterRule(listener: toy_asmListener): void {
	    if(listener.enterDiv) {
	 		listener.enterDiv(this);
		}
	}
	public exitRule(listener: toy_asmListener): void {
	    if(listener.exitDiv) {
	 		listener.exitDiv(this);
		}
	}
	// @Override
	public accept<Result>(visitor: toy_asmVisitor<Result>): Result {
		if (visitor.visitDiv) {
			return visitor.visitDiv(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class CmpContext extends ParserRuleContext {
	constructor(parser?: toy_asmParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public reg_list(): RegContext[] {
		return this.getTypedRuleContexts(RegContext) as RegContext[];
	}
	public reg(i: number): RegContext {
		return this.getTypedRuleContext(RegContext, i) as RegContext;
	}
	public num(): NumContext {
		return this.getTypedRuleContext(NumContext, 0) as NumContext;
	}
	public mem(): MemContext {
		return this.getTypedRuleContext(MemContext, 0) as MemContext;
	}
    public get ruleIndex(): number {
    	return toy_asmParser.RULE_cmp;
	}
	public enterRule(listener: toy_asmListener): void {
	    if(listener.enterCmp) {
	 		listener.enterCmp(this);
		}
	}
	public exitRule(listener: toy_asmListener): void {
	    if(listener.exitCmp) {
	 		listener.exitCmp(this);
		}
	}
	// @Override
	public accept<Result>(visitor: toy_asmVisitor<Result>): Result {
		if (visitor.visitCmp) {
			return visitor.visitCmp(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class JumpContext extends ParserRuleContext {
	constructor(parser?: toy_asmParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public Label(): TerminalNode {
		return this.getToken(toy_asmParser.Label, 0);
	}
    public get ruleIndex(): number {
    	return toy_asmParser.RULE_jump;
	}
	public enterRule(listener: toy_asmListener): void {
	    if(listener.enterJump) {
	 		listener.enterJump(this);
		}
	}
	public exitRule(listener: toy_asmListener): void {
	    if(listener.exitJump) {
	 		listener.exitJump(this);
		}
	}
	// @Override
	public accept<Result>(visitor: toy_asmVisitor<Result>): Result {
		if (visitor.visitJump) {
			return visitor.visitJump(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class CallContext extends ParserRuleContext {
	constructor(parser?: toy_asmParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public Label(): TerminalNode {
		return this.getToken(toy_asmParser.Label, 0);
	}
    public get ruleIndex(): number {
    	return toy_asmParser.RULE_call;
	}
	public enterRule(listener: toy_asmListener): void {
	    if(listener.enterCall) {
	 		listener.enterCall(this);
		}
	}
	public exitRule(listener: toy_asmListener): void {
	    if(listener.exitCall) {
	 		listener.exitCall(this);
		}
	}
	// @Override
	public accept<Result>(visitor: toy_asmVisitor<Result>): Result {
		if (visitor.visitCall) {
			return visitor.visitCall(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class RetContext extends ParserRuleContext {
	constructor(parser?: toy_asmParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
    public get ruleIndex(): number {
    	return toy_asmParser.RULE_ret;
	}
	public enterRule(listener: toy_asmListener): void {
	    if(listener.enterRet) {
	 		listener.enterRet(this);
		}
	}
	public exitRule(listener: toy_asmListener): void {
	    if(listener.exitRet) {
	 		listener.exitRet(this);
		}
	}
	// @Override
	public accept<Result>(visitor: toy_asmVisitor<Result>): Result {
		if (visitor.visitRet) {
			return visitor.visitRet(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class PushContext extends ParserRuleContext {
	constructor(parser?: toy_asmParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public num(): NumContext {
		return this.getTypedRuleContext(NumContext, 0) as NumContext;
	}
	public reg(): RegContext {
		return this.getTypedRuleContext(RegContext, 0) as RegContext;
	}
    public get ruleIndex(): number {
    	return toy_asmParser.RULE_push;
	}
	public enterRule(listener: toy_asmListener): void {
	    if(listener.enterPush) {
	 		listener.enterPush(this);
		}
	}
	public exitRule(listener: toy_asmListener): void {
	    if(listener.exitPush) {
	 		listener.exitPush(this);
		}
	}
	// @Override
	public accept<Result>(visitor: toy_asmVisitor<Result>): Result {
		if (visitor.visitPush) {
			return visitor.visitPush(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class PopContext extends ParserRuleContext {
	constructor(parser?: toy_asmParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public reg(): RegContext {
		return this.getTypedRuleContext(RegContext, 0) as RegContext;
	}
    public get ruleIndex(): number {
    	return toy_asmParser.RULE_pop;
	}
	public enterRule(listener: toy_asmListener): void {
	    if(listener.enterPop) {
	 		listener.enterPop(this);
		}
	}
	public exitRule(listener: toy_asmListener): void {
	    if(listener.exitPop) {
	 		listener.exitPop(this);
		}
	}
	// @Override
	public accept<Result>(visitor: toy_asmVisitor<Result>): Result {
		if (visitor.visitPop) {
			return visitor.visitPop(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class InputContext extends ParserRuleContext {
	constructor(parser?: toy_asmParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public reg(): RegContext {
		return this.getTypedRuleContext(RegContext, 0) as RegContext;
	}
	public mem(): MemContext {
		return this.getTypedRuleContext(MemContext, 0) as MemContext;
	}
    public get ruleIndex(): number {
    	return toy_asmParser.RULE_input;
	}
	public enterRule(listener: toy_asmListener): void {
	    if(listener.enterInput) {
	 		listener.enterInput(this);
		}
	}
	public exitRule(listener: toy_asmListener): void {
	    if(listener.exitInput) {
	 		listener.exitInput(this);
		}
	}
	// @Override
	public accept<Result>(visitor: toy_asmVisitor<Result>): Result {
		if (visitor.visitInput) {
			return visitor.visitInput(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class StrContext extends ParserRuleContext {
	constructor(parser?: toy_asmParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public STR(): TerminalNode {
		return this.getToken(toy_asmParser.STR, 0);
	}
    public get ruleIndex(): number {
    	return toy_asmParser.RULE_str;
	}
	public enterRule(listener: toy_asmListener): void {
	    if(listener.enterStr) {
	 		listener.enterStr(this);
		}
	}
	public exitRule(listener: toy_asmListener): void {
	    if(listener.exitStr) {
	 		listener.exitStr(this);
		}
	}
	// @Override
	public accept<Result>(visitor: toy_asmVisitor<Result>): Result {
		if (visitor.visitStr) {
			return visitor.visitStr(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class PrintContext extends ParserRuleContext {
	constructor(parser?: toy_asmParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public num(): NumContext {
		return this.getTypedRuleContext(NumContext, 0) as NumContext;
	}
	public reg(): RegContext {
		return this.getTypedRuleContext(RegContext, 0) as RegContext;
	}
	public mem(): MemContext {
		return this.getTypedRuleContext(MemContext, 0) as MemContext;
	}
	public str(): StrContext {
		return this.getTypedRuleContext(StrContext, 0) as StrContext;
	}
    public get ruleIndex(): number {
    	return toy_asmParser.RULE_print;
	}
	public enterRule(listener: toy_asmListener): void {
	    if(listener.enterPrint) {
	 		listener.enterPrint(this);
		}
	}
	public exitRule(listener: toy_asmListener): void {
	    if(listener.exitPrint) {
	 		listener.exitPrint(this);
		}
	}
	// @Override
	public accept<Result>(visitor: toy_asmVisitor<Result>): Result {
		if (visitor.visitPrint) {
			return visitor.visitPrint(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class RandContext extends ParserRuleContext {
	constructor(parser?: toy_asmParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public reg(): RegContext {
		return this.getTypedRuleContext(RegContext, 0) as RegContext;
	}
	public mem(): MemContext {
		return this.getTypedRuleContext(MemContext, 0) as MemContext;
	}
    public get ruleIndex(): number {
    	return toy_asmParser.RULE_rand;
	}
	public enterRule(listener: toy_asmListener): void {
	    if(listener.enterRand) {
	 		listener.enterRand(this);
		}
	}
	public exitRule(listener: toy_asmListener): void {
	    if(listener.exitRand) {
	 		listener.exitRand(this);
		}
	}
	// @Override
	public accept<Result>(visitor: toy_asmVisitor<Result>): Result {
		if (visitor.visitRand) {
			return visitor.visitRand(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class PauseContext extends ParserRuleContext {
	constructor(parser?: toy_asmParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
    public get ruleIndex(): number {
    	return toy_asmParser.RULE_pause;
	}
	public enterRule(listener: toy_asmListener): void {
	    if(listener.enterPause) {
	 		listener.enterPause(this);
		}
	}
	public exitRule(listener: toy_asmListener): void {
	    if(listener.exitPause) {
	 		listener.exitPause(this);
		}
	}
	// @Override
	public accept<Result>(visitor: toy_asmVisitor<Result>): Result {
		if (visitor.visitPause) {
			return visitor.visitPause(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class HaltContext extends ParserRuleContext {
	constructor(parser?: toy_asmParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
    public get ruleIndex(): number {
    	return toy_asmParser.RULE_halt;
	}
	public enterRule(listener: toy_asmListener): void {
	    if(listener.enterHalt) {
	 		listener.enterHalt(this);
		}
	}
	public exitRule(listener: toy_asmListener): void {
	    if(listener.exitHalt) {
	 		listener.exitHalt(this);
		}
	}
	// @Override
	public accept<Result>(visitor: toy_asmVisitor<Result>): Result {
		if (visitor.visitHalt) {
			return visitor.visitHalt(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class NopContext extends ParserRuleContext {
	constructor(parser?: toy_asmParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
    public get ruleIndex(): number {
    	return toy_asmParser.RULE_nop;
	}
	public enterRule(listener: toy_asmListener): void {
	    if(listener.enterNop) {
	 		listener.enterNop(this);
		}
	}
	public exitRule(listener: toy_asmListener): void {
	    if(listener.exitNop) {
	 		listener.exitNop(this);
		}
	}
	// @Override
	public accept<Result>(visitor: toy_asmVisitor<Result>): Result {
		if (visitor.visitNop) {
			return visitor.visitNop(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}
