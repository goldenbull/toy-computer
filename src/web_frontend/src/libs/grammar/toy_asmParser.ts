// Generated from toy_asm.g4 by ANTLR 4.13.2
// noinspection ES6UnusedImports,JSUnusedGlobalSymbols,JSUnusedLocalSymbols

import {
	ATN,
	ATNDeserializer, type DecisionState, DFA, FailedPredicateException,
	RecognitionException, NoViableAltException, BailErrorStrategy,
	Parser, ParserATNSimulator,
	RuleContext, ParserRuleContext, PredictionMode, PredictionContextCache,
	TerminalNode, RuleNode,
	Token, type TokenStream,
	Interval, IntervalSet
} from 'antlr4';
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
	public static readonly INT = 37;
	public static readonly Label = 38;
	public static readonly STR = 39;
	public static readonly WS = 40;
	public static override readonly EOF = Token.EOF;
	public static readonly RULE_line = 0;
	public static readonly RULE_label = 1;
	public static readonly RULE_label_and_op = 2;
	public static readonly RULE_op = 3;
	public static readonly RULE_num = 4;
	public static readonly RULE_reg = 5;
	public static readonly RULE_offset = 6;
	public static readonly RULE_mem = 7;
	public static readonly RULE_mov = 8;
	public static readonly RULE_add = 9;
	public static readonly RULE_sub = 10;
	public static readonly RULE_mul = 11;
	public static readonly RULE_div = 12;
	public static readonly RULE_cmp = 13;
	public static readonly RULE_jump = 14;
	public static readonly RULE_call = 15;
	public static readonly RULE_ret = 16;
	public static readonly RULE_push = 17;
	public static readonly RULE_pop = 18;
	public static readonly RULE_input = 19;
	public static readonly RULE_str = 20;
	public static readonly RULE_print = 21;
	public static readonly RULE_rand = 22;
	public static readonly RULE_halt = 23;
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
                                                            "'rand'", "'halt'" ];
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
                                                             null, "INT", 
                                                             "Label", "STR", 
                                                             "WS" ];
	// tslint:disable:no-trailing-whitespace
	public static readonly ruleNames: string[] = [
		"line", "label", "label_and_op", "op", "num", "reg", "offset", "mem", 
		"mov", "add", "sub", "mul", "div", "cmp", "jump", "call", "ret", "push", 
		"pop", "input", "str", "print", "rand", "halt",
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
	public line(): LineContext {
		let localctx: LineContext = new LineContext(this, this._ctx, this.state);
		this.enterRule(localctx, 0, toy_asmParser.RULE_line);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 51;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 0, this._ctx) ) {
			case 1:
				{
				this.state = 48;
				this.label();
				}
				break;
			case 2:
				{
				this.state = 49;
				this.label_and_op();
				}
				break;
			case 3:
				{
				this.state = 50;
				this.op();
				}
				break;
			}
			this.state = 53;
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
	public label(): LabelContext {
		let localctx: LabelContext = new LabelContext(this, this._ctx, this.state);
		this.enterRule(localctx, 2, toy_asmParser.RULE_label);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 55;
			this.match(toy_asmParser.Label);
			this.state = 56;
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
	public label_and_op(): Label_and_opContext {
		let localctx: Label_and_opContext = new Label_and_opContext(this, this._ctx, this.state);
		this.enterRule(localctx, 4, toy_asmParser.RULE_label_and_op);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 58;
			this.label();
			this.state = 59;
			this.match(toy_asmParser.T__0);
			this.state = 60;
			this.op();
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
		this.enterRule(localctx, 6, toy_asmParser.RULE_op);
		try {
			this.state = 77;
			this._errHandler.sync(this);
			switch (this._input.LA(1)) {
			case 12:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 62;
				this.mov();
				}
				break;
			case 14:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 63;
				this.add();
				}
				break;
			case 15:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 64;
				this.sub();
				}
				break;
			case 16:
				this.enterOuterAlt(localctx, 4);
				{
				this.state = 65;
				this.mul();
				}
				break;
			case 17:
				this.enterOuterAlt(localctx, 5);
				{
				this.state = 66;
				this.div();
				}
				break;
			case 18:
				this.enterOuterAlt(localctx, 6);
				{
				this.state = 67;
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
				this.state = 68;
				this.jump();
				}
				break;
			case 26:
				this.enterOuterAlt(localctx, 8);
				{
				this.state = 69;
				this.call();
				}
				break;
			case 27:
				this.enterOuterAlt(localctx, 9);
				{
				this.state = 70;
				this.ret();
				}
				break;
			case 28:
			case 29:
				this.enterOuterAlt(localctx, 10);
				{
				this.state = 71;
				this.push();
				}
				break;
			case 30:
			case 31:
				this.enterOuterAlt(localctx, 11);
				{
				this.state = 72;
				this.pop();
				}
				break;
			case 32:
				this.enterOuterAlt(localctx, 12);
				{
				this.state = 73;
				this.input();
				}
				break;
			case 33:
			case 34:
				this.enterOuterAlt(localctx, 13);
				{
				this.state = 74;
				this.print();
				}
				break;
			case 35:
				this.enterOuterAlt(localctx, 14);
				{
				this.state = 75;
				this.rand();
				}
				break;
			case 36:
				this.enterOuterAlt(localctx, 15);
				{
				this.state = 76;
				this.halt();
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
		this.enterRule(localctx, 8, toy_asmParser.RULE_num);
		let _la: number;
		try {
			this.state = 85;
			this._errHandler.sync(this);
			switch (this._input.LA(1)) {
			case 2:
			case 37:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 80;
				this._errHandler.sync(this);
				_la = this._input.LA(1);
				if (_la===2) {
					{
					this.state = 79;
					this.match(toy_asmParser.T__1);
					}
				}

				this.state = 82;
				this.match(toy_asmParser.INT);
				}
				break;
			case 3:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 83;
				this.match(toy_asmParser.T__2);
				this.state = 84;
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
		this.enterRule(localctx, 10, toy_asmParser.RULE_reg);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 87;
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
		this.enterRule(localctx, 12, toy_asmParser.RULE_offset);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 89;
			_la = this._input.LA(1);
			if(!(_la===2 || _la===3)) {
			this._errHandler.recoverInline(this);
			}
			else {
				this._errHandler.reportMatch(this);
			    this.consume();
			}
			this.state = 90;
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
		this.enterRule(localctx, 14, toy_asmParser.RULE_mem);
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 92;
			this.match(toy_asmParser.T__9);
			this.state = 93;
			this.reg();
			this.state = 95;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===2 || _la===3) {
				{
				this.state = 94;
				this.offset();
				}
			}

			this.state = 97;
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
	public mov(): MovContext {
		let localctx: MovContext = new MovContext(this, this._ctx, this.state);
		this.enterRule(localctx, 16, toy_asmParser.RULE_mov);
		try {
			this.state = 124;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 5, this._ctx) ) {
			case 1:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 99;
				this.match(toy_asmParser.T__11);
				this.state = 100;
				this.reg();
				this.state = 101;
				this.match(toy_asmParser.T__12);
				this.state = 102;
				this.num();
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 104;
				this.match(toy_asmParser.T__11);
				this.state = 105;
				this.reg();
				this.state = 106;
				this.match(toy_asmParser.T__12);
				this.state = 107;
				this.reg();
				}
				break;
			case 3:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 109;
				this.match(toy_asmParser.T__11);
				this.state = 110;
				this.reg();
				this.state = 111;
				this.match(toy_asmParser.T__12);
				this.state = 112;
				this.mem();
				}
				break;
			case 4:
				this.enterOuterAlt(localctx, 4);
				{
				this.state = 114;
				this.match(toy_asmParser.T__11);
				this.state = 115;
				this.mem();
				this.state = 116;
				this.match(toy_asmParser.T__12);
				this.state = 117;
				this.num();
				}
				break;
			case 5:
				this.enterOuterAlt(localctx, 5);
				{
				this.state = 119;
				this.match(toy_asmParser.T__11);
				this.state = 120;
				this.mem();
				this.state = 121;
				this.match(toy_asmParser.T__12);
				this.state = 122;
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
		this.enterRule(localctx, 18, toy_asmParser.RULE_add);
		try {
			this.state = 141;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 6, this._ctx) ) {
			case 1:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 126;
				this.match(toy_asmParser.T__13);
				this.state = 127;
				this.reg();
				this.state = 128;
				this.match(toy_asmParser.T__12);
				this.state = 129;
				this.num();
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 131;
				this.match(toy_asmParser.T__13);
				this.state = 132;
				this.reg();
				this.state = 133;
				this.match(toy_asmParser.T__12);
				this.state = 134;
				this.reg();
				}
				break;
			case 3:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 136;
				this.match(toy_asmParser.T__13);
				this.state = 137;
				this.reg();
				this.state = 138;
				this.match(toy_asmParser.T__12);
				this.state = 139;
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
		this.enterRule(localctx, 20, toy_asmParser.RULE_sub);
		try {
			this.state = 158;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 7, this._ctx) ) {
			case 1:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 143;
				this.match(toy_asmParser.T__14);
				this.state = 144;
				this.reg();
				this.state = 145;
				this.match(toy_asmParser.T__12);
				this.state = 146;
				this.num();
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 148;
				this.match(toy_asmParser.T__14);
				this.state = 149;
				this.reg();
				this.state = 150;
				this.match(toy_asmParser.T__12);
				this.state = 151;
				this.reg();
				}
				break;
			case 3:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 153;
				this.match(toy_asmParser.T__14);
				this.state = 154;
				this.reg();
				this.state = 155;
				this.match(toy_asmParser.T__12);
				this.state = 156;
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
		this.enterRule(localctx, 22, toy_asmParser.RULE_mul);
		try {
			this.state = 166;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 8, this._ctx) ) {
			case 1:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 160;
				this.match(toy_asmParser.T__15);
				this.state = 161;
				this.num();
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 162;
				this.match(toy_asmParser.T__15);
				this.state = 163;
				this.reg();
				}
				break;
			case 3:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 164;
				this.match(toy_asmParser.T__15);
				this.state = 165;
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
		this.enterRule(localctx, 24, toy_asmParser.RULE_div);
		try {
			this.state = 174;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 9, this._ctx) ) {
			case 1:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 168;
				this.match(toy_asmParser.T__16);
				this.state = 169;
				this.num();
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 170;
				this.match(toy_asmParser.T__16);
				this.state = 171;
				this.reg();
				}
				break;
			case 3:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 172;
				this.match(toy_asmParser.T__16);
				this.state = 173;
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
		this.enterRule(localctx, 26, toy_asmParser.RULE_cmp);
		try {
			this.state = 191;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 10, this._ctx) ) {
			case 1:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 176;
				this.match(toy_asmParser.T__17);
				this.state = 177;
				this.reg();
				this.state = 178;
				this.match(toy_asmParser.T__12);
				this.state = 179;
				this.num();
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 181;
				this.match(toy_asmParser.T__17);
				this.state = 182;
				this.reg();
				this.state = 183;
				this.match(toy_asmParser.T__12);
				this.state = 184;
				this.reg();
				}
				break;
			case 3:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 186;
				this.match(toy_asmParser.T__17);
				this.state = 187;
				this.reg();
				this.state = 188;
				this.match(toy_asmParser.T__12);
				this.state = 189;
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
		this.enterRule(localctx, 28, toy_asmParser.RULE_jump);
		try {
			this.state = 207;
			this._errHandler.sync(this);
			switch (this._input.LA(1)) {
			case 19:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 193;
				this.match(toy_asmParser.T__18);
				this.state = 194;
				this.match(toy_asmParser.Label);
				}
				break;
			case 20:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 195;
				this.match(toy_asmParser.T__19);
				this.state = 196;
				this.match(toy_asmParser.Label);
				}
				break;
			case 21:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 197;
				this.match(toy_asmParser.T__20);
				this.state = 198;
				this.match(toy_asmParser.Label);
				}
				break;
			case 22:
				this.enterOuterAlt(localctx, 4);
				{
				this.state = 199;
				this.match(toy_asmParser.T__21);
				this.state = 200;
				this.match(toy_asmParser.Label);
				}
				break;
			case 23:
				this.enterOuterAlt(localctx, 5);
				{
				this.state = 201;
				this.match(toy_asmParser.T__22);
				this.state = 202;
				this.match(toy_asmParser.Label);
				}
				break;
			case 24:
				this.enterOuterAlt(localctx, 6);
				{
				this.state = 203;
				this.match(toy_asmParser.T__23);
				this.state = 204;
				this.match(toy_asmParser.Label);
				}
				break;
			case 25:
				this.enterOuterAlt(localctx, 7);
				{
				this.state = 205;
				this.match(toy_asmParser.T__24);
				this.state = 206;
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
		this.enterRule(localctx, 30, toy_asmParser.RULE_call);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 209;
			this.match(toy_asmParser.T__25);
			this.state = 210;
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
		this.enterRule(localctx, 32, toy_asmParser.RULE_ret);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 212;
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
		this.enterRule(localctx, 34, toy_asmParser.RULE_push);
		try {
			this.state = 219;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 12, this._ctx) ) {
			case 1:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 214;
				this.match(toy_asmParser.T__27);
				this.state = 215;
				this.num();
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 216;
				this.match(toy_asmParser.T__27);
				this.state = 217;
				this.reg();
				}
				break;
			case 3:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 218;
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
		this.enterRule(localctx, 36, toy_asmParser.RULE_pop);
		try {
			this.state = 225;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 13, this._ctx) ) {
			case 1:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 221;
				this.match(toy_asmParser.T__29);
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 222;
				this.match(toy_asmParser.T__29);
				this.state = 223;
				this.reg();
				}
				break;
			case 3:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 224;
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
		this.enterRule(localctx, 38, toy_asmParser.RULE_input);
		try {
			this.state = 231;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 14, this._ctx) ) {
			case 1:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 227;
				this.match(toy_asmParser.T__31);
				this.state = 228;
				this.reg();
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 229;
				this.match(toy_asmParser.T__31);
				this.state = 230;
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
		this.enterRule(localctx, 40, toy_asmParser.RULE_str);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 233;
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
		this.enterRule(localctx, 42, toy_asmParser.RULE_print);
		try {
			this.state = 252;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 15, this._ctx) ) {
			case 1:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 235;
				this.match(toy_asmParser.T__32);
				this.state = 236;
				this.num();
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 237;
				this.match(toy_asmParser.T__32);
				this.state = 238;
				this.reg();
				}
				break;
			case 3:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 239;
				this.match(toy_asmParser.T__32);
				this.state = 240;
				this.mem();
				}
				break;
			case 4:
				this.enterOuterAlt(localctx, 4);
				{
				this.state = 241;
				this.match(toy_asmParser.T__32);
				this.state = 242;
				this.str();
				}
				break;
			case 5:
				this.enterOuterAlt(localctx, 5);
				{
				this.state = 243;
				this.match(toy_asmParser.T__33);
				this.state = 244;
				this.num();
				}
				break;
			case 6:
				this.enterOuterAlt(localctx, 6);
				{
				this.state = 245;
				this.match(toy_asmParser.T__33);
				this.state = 246;
				this.reg();
				}
				break;
			case 7:
				this.enterOuterAlt(localctx, 7);
				{
				this.state = 247;
				this.match(toy_asmParser.T__33);
				this.state = 248;
				this.mem();
				}
				break;
			case 8:
				this.enterOuterAlt(localctx, 8);
				{
				this.state = 249;
				this.match(toy_asmParser.T__33);
				this.state = 250;
				this.str();
				}
				break;
			case 9:
				this.enterOuterAlt(localctx, 9);
				{
				this.state = 251;
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
		this.enterRule(localctx, 44, toy_asmParser.RULE_rand);
		try {
			this.state = 258;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 16, this._ctx) ) {
			case 1:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 254;
				this.match(toy_asmParser.T__34);
				this.state = 255;
				this.reg();
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 256;
				this.match(toy_asmParser.T__34);
				this.state = 257;
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
	public halt(): HaltContext {
		let localctx: HaltContext = new HaltContext(this, this._ctx, this.state);
		this.enterRule(localctx, 46, toy_asmParser.RULE_halt);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 260;
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

	public static readonly _serializedATN: number[] = [4,1,40,263,2,0,7,0,2,
	1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,
	10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,
	7,17,2,18,7,18,2,19,7,19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,1,
	0,1,0,3,0,52,8,0,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,
	3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,78,8,3,1,4,3,4,81,8,4,1,4,
	1,4,1,4,3,4,86,8,4,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,3,7,96,8,7,1,7,1,7,1,
	8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
	8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,125,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
	9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,142,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
	1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,159,8,10,1,11,1,11,1,11,1,
	11,1,11,1,11,3,11,167,8,11,1,12,1,12,1,12,1,12,1,12,1,12,3,12,175,8,12,
	1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
	13,3,13,192,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
	1,14,1,14,1,14,3,14,208,8,14,1,15,1,15,1,15,1,16,1,16,1,17,1,17,1,17,1,
	17,1,17,3,17,220,8,17,1,18,1,18,1,18,1,18,3,18,226,8,18,1,19,1,19,1,19,
	1,19,3,19,232,8,19,1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,
	21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,253,8,21,1,22,1,22,1,22,
	1,22,3,22,259,8,22,1,23,1,23,1,23,0,0,24,0,2,4,6,8,10,12,14,16,18,20,22,
	24,26,28,30,32,34,36,38,40,42,44,46,0,2,1,0,4,9,1,0,2,3,291,0,51,1,0,0,
	0,2,55,1,0,0,0,4,58,1,0,0,0,6,77,1,0,0,0,8,85,1,0,0,0,10,87,1,0,0,0,12,
	89,1,0,0,0,14,92,1,0,0,0,16,124,1,0,0,0,18,141,1,0,0,0,20,158,1,0,0,0,22,
	166,1,0,0,0,24,174,1,0,0,0,26,191,1,0,0,0,28,207,1,0,0,0,30,209,1,0,0,0,
	32,212,1,0,0,0,34,219,1,0,0,0,36,225,1,0,0,0,38,231,1,0,0,0,40,233,1,0,
	0,0,42,252,1,0,0,0,44,258,1,0,0,0,46,260,1,0,0,0,48,52,3,2,1,0,49,52,3,
	4,2,0,50,52,3,6,3,0,51,48,1,0,0,0,51,49,1,0,0,0,51,50,1,0,0,0,52,53,1,0,
	0,0,53,54,5,0,0,1,54,1,1,0,0,0,55,56,5,38,0,0,56,57,5,1,0,0,57,3,1,0,0,
	0,58,59,3,2,1,0,59,60,5,1,0,0,60,61,3,6,3,0,61,5,1,0,0,0,62,78,3,16,8,0,
	63,78,3,18,9,0,64,78,3,20,10,0,65,78,3,22,11,0,66,78,3,24,12,0,67,78,3,
	26,13,0,68,78,3,28,14,0,69,78,3,30,15,0,70,78,3,32,16,0,71,78,3,34,17,0,
	72,78,3,36,18,0,73,78,3,38,19,0,74,78,3,42,21,0,75,78,3,44,22,0,76,78,3,
	46,23,0,77,62,1,0,0,0,77,63,1,0,0,0,77,64,1,0,0,0,77,65,1,0,0,0,77,66,1,
	0,0,0,77,67,1,0,0,0,77,68,1,0,0,0,77,69,1,0,0,0,77,70,1,0,0,0,77,71,1,0,
	0,0,77,72,1,0,0,0,77,73,1,0,0,0,77,74,1,0,0,0,77,75,1,0,0,0,77,76,1,0,0,
	0,78,7,1,0,0,0,79,81,5,2,0,0,80,79,1,0,0,0,80,81,1,0,0,0,81,82,1,0,0,0,
	82,86,5,37,0,0,83,84,5,3,0,0,84,86,5,37,0,0,85,80,1,0,0,0,85,83,1,0,0,0,
	86,9,1,0,0,0,87,88,7,0,0,0,88,11,1,0,0,0,89,90,7,1,0,0,90,91,5,37,0,0,91,
	13,1,0,0,0,92,93,5,10,0,0,93,95,3,10,5,0,94,96,3,12,6,0,95,94,1,0,0,0,95,
	96,1,0,0,0,96,97,1,0,0,0,97,98,5,11,0,0,98,15,1,0,0,0,99,100,5,12,0,0,100,
	101,3,10,5,0,101,102,5,13,0,0,102,103,3,8,4,0,103,125,1,0,0,0,104,105,5,
	12,0,0,105,106,3,10,5,0,106,107,5,13,0,0,107,108,3,10,5,0,108,125,1,0,0,
	0,109,110,5,12,0,0,110,111,3,10,5,0,111,112,5,13,0,0,112,113,3,14,7,0,113,
	125,1,0,0,0,114,115,5,12,0,0,115,116,3,14,7,0,116,117,5,13,0,0,117,118,
	3,8,4,0,118,125,1,0,0,0,119,120,5,12,0,0,120,121,3,14,7,0,121,122,5,13,
	0,0,122,123,3,10,5,0,123,125,1,0,0,0,124,99,1,0,0,0,124,104,1,0,0,0,124,
	109,1,0,0,0,124,114,1,0,0,0,124,119,1,0,0,0,125,17,1,0,0,0,126,127,5,14,
	0,0,127,128,3,10,5,0,128,129,5,13,0,0,129,130,3,8,4,0,130,142,1,0,0,0,131,
	132,5,14,0,0,132,133,3,10,5,0,133,134,5,13,0,0,134,135,3,10,5,0,135,142,
	1,0,0,0,136,137,5,14,0,0,137,138,3,10,5,0,138,139,5,13,0,0,139,140,3,14,
	7,0,140,142,1,0,0,0,141,126,1,0,0,0,141,131,1,0,0,0,141,136,1,0,0,0,142,
	19,1,0,0,0,143,144,5,15,0,0,144,145,3,10,5,0,145,146,5,13,0,0,146,147,3,
	8,4,0,147,159,1,0,0,0,148,149,5,15,0,0,149,150,3,10,5,0,150,151,5,13,0,
	0,151,152,3,10,5,0,152,159,1,0,0,0,153,154,5,15,0,0,154,155,3,10,5,0,155,
	156,5,13,0,0,156,157,3,14,7,0,157,159,1,0,0,0,158,143,1,0,0,0,158,148,1,
	0,0,0,158,153,1,0,0,0,159,21,1,0,0,0,160,161,5,16,0,0,161,167,3,8,4,0,162,
	163,5,16,0,0,163,167,3,10,5,0,164,165,5,16,0,0,165,167,3,14,7,0,166,160,
	1,0,0,0,166,162,1,0,0,0,166,164,1,0,0,0,167,23,1,0,0,0,168,169,5,17,0,0,
	169,175,3,8,4,0,170,171,5,17,0,0,171,175,3,10,5,0,172,173,5,17,0,0,173,
	175,3,14,7,0,174,168,1,0,0,0,174,170,1,0,0,0,174,172,1,0,0,0,175,25,1,0,
	0,0,176,177,5,18,0,0,177,178,3,10,5,0,178,179,5,13,0,0,179,180,3,8,4,0,
	180,192,1,0,0,0,181,182,5,18,0,0,182,183,3,10,5,0,183,184,5,13,0,0,184,
	185,3,10,5,0,185,192,1,0,0,0,186,187,5,18,0,0,187,188,3,10,5,0,188,189,
	5,13,0,0,189,190,3,14,7,0,190,192,1,0,0,0,191,176,1,0,0,0,191,181,1,0,0,
	0,191,186,1,0,0,0,192,27,1,0,0,0,193,194,5,19,0,0,194,208,5,38,0,0,195,
	196,5,20,0,0,196,208,5,38,0,0,197,198,5,21,0,0,198,208,5,38,0,0,199,200,
	5,22,0,0,200,208,5,38,0,0,201,202,5,23,0,0,202,208,5,38,0,0,203,204,5,24,
	0,0,204,208,5,38,0,0,205,206,5,25,0,0,206,208,5,38,0,0,207,193,1,0,0,0,
	207,195,1,0,0,0,207,197,1,0,0,0,207,199,1,0,0,0,207,201,1,0,0,0,207,203,
	1,0,0,0,207,205,1,0,0,0,208,29,1,0,0,0,209,210,5,26,0,0,210,211,5,38,0,
	0,211,31,1,0,0,0,212,213,5,27,0,0,213,33,1,0,0,0,214,215,5,28,0,0,215,220,
	3,8,4,0,216,217,5,28,0,0,217,220,3,10,5,0,218,220,5,29,0,0,219,214,1,0,
	0,0,219,216,1,0,0,0,219,218,1,0,0,0,220,35,1,0,0,0,221,226,5,30,0,0,222,
	223,5,30,0,0,223,226,3,10,5,0,224,226,5,31,0,0,225,221,1,0,0,0,225,222,
	1,0,0,0,225,224,1,0,0,0,226,37,1,0,0,0,227,228,5,32,0,0,228,232,3,10,5,
	0,229,230,5,32,0,0,230,232,3,14,7,0,231,227,1,0,0,0,231,229,1,0,0,0,232,
	39,1,0,0,0,233,234,5,39,0,0,234,41,1,0,0,0,235,236,5,33,0,0,236,253,3,8,
	4,0,237,238,5,33,0,0,238,253,3,10,5,0,239,240,5,33,0,0,240,253,3,14,7,0,
	241,242,5,33,0,0,242,253,3,40,20,0,243,244,5,34,0,0,244,253,3,8,4,0,245,
	246,5,34,0,0,246,253,3,10,5,0,247,248,5,34,0,0,248,253,3,14,7,0,249,250,
	5,34,0,0,250,253,3,40,20,0,251,253,5,34,0,0,252,235,1,0,0,0,252,237,1,0,
	0,0,252,239,1,0,0,0,252,241,1,0,0,0,252,243,1,0,0,0,252,245,1,0,0,0,252,
	247,1,0,0,0,252,249,1,0,0,0,252,251,1,0,0,0,253,43,1,0,0,0,254,255,5,35,
	0,0,255,259,3,10,5,0,256,257,5,35,0,0,257,259,3,14,7,0,258,254,1,0,0,0,
	258,256,1,0,0,0,259,45,1,0,0,0,260,261,5,36,0,0,261,47,1,0,0,0,17,51,77,
	80,85,95,124,141,158,166,174,191,207,219,225,231,252,258];

	private static __ATN: ATN;
	public static get _ATN(): ATN {
		if (!toy_asmParser.__ATN) {
			toy_asmParser.__ATN = new ATNDeserializer().deserialize(toy_asmParser._serializedATN);
		}

		return toy_asmParser.__ATN;
	}


	static DecisionsToDFA = toy_asmParser._ATN.decisionToState.map( (ds: DecisionState, index: number) => new DFA(ds, index) );

}

export class LineContext extends ParserRuleContext {
	constructor(parser?: toy_asmParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public EOF(): TerminalNode {
		return this.getToken(toy_asmParser.EOF, 0);
	}
	public label(): LabelContext {
		return this.getTypedRuleContext(LabelContext, 0) as LabelContext;
	}
	public label_and_op(): Label_and_opContext {
		return this.getTypedRuleContext(Label_and_opContext, 0) as Label_and_opContext;
	}
	public op(): OpContext {
		return this.getTypedRuleContext(OpContext, 0) as OpContext;
	}
    public get ruleIndex(): number {
    	return toy_asmParser.RULE_line;
	}
	// @Override
	public accept<Result>(visitor: toy_asmVisitor<Result>): Result {
		if (visitor.visitLine) {
			return visitor.visitLine(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class LabelContext extends ParserRuleContext {
	constructor(parser?: toy_asmParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public Label(): TerminalNode {
		return this.getToken(toy_asmParser.Label, 0);
	}
    public get ruleIndex(): number {
    	return toy_asmParser.RULE_label;
	}
	// @Override
	public accept<Result>(visitor: toy_asmVisitor<Result>): Result {
		if (visitor.visitLabel) {
			return visitor.visitLabel(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class Label_and_opContext extends ParserRuleContext {
	constructor(parser?: toy_asmParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public label(): LabelContext {
		return this.getTypedRuleContext(LabelContext, 0) as LabelContext;
	}
	public op(): OpContext {
		return this.getTypedRuleContext(OpContext, 0) as OpContext;
	}
    public get ruleIndex(): number {
    	return toy_asmParser.RULE_label_and_op;
	}
	// @Override
	public accept<Result>(visitor: toy_asmVisitor<Result>): Result {
		if (visitor.visitLabel_and_op) {
			return visitor.visitLabel_and_op(this);
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
	public mov(): MovContext {
		return this.getTypedRuleContext(MovContext, 0) as MovContext;
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
	public halt(): HaltContext {
		return this.getTypedRuleContext(HaltContext, 0) as HaltContext;
	}
    public get ruleIndex(): number {
    	return toy_asmParser.RULE_op;
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
	// @Override
	public accept<Result>(visitor: toy_asmVisitor<Result>): Result {
		if (visitor.visitMem) {
			return visitor.visitMem(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}


export class MovContext extends ParserRuleContext {
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
    	return toy_asmParser.RULE_mov;
	}
	// @Override
	public accept<Result>(visitor: toy_asmVisitor<Result>): Result {
		if (visitor.visitMov) {
			return visitor.visitMov(this);
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
	// @Override
	public accept<Result>(visitor: toy_asmVisitor<Result>): Result {
		if (visitor.visitRand) {
			return visitor.visitRand(this);
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
	// @Override
	public accept<Result>(visitor: toy_asmVisitor<Result>): Result {
		if (visitor.visitHalt) {
			return visitor.visitHalt(this);
		} else {
			return visitor.visitChildren(this);
		}
	}
}
