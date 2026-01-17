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
	public static readonly Comma = 35;
	public static readonly Colon = 36;
	public static readonly Comment = 37;
	public static readonly INT = 38;
	public static readonly Label = 39;
	public static readonly STR = 40;
	public static readonly WS = 41;
	public static override readonly EOF = Token.EOF;
	public static readonly RULE_line = 0;
	public static readonly RULE_label = 1;
	public static readonly RULE_comment = 2;
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
	public static readonly literalNames: (string | null)[] = [ null, "'+'", 
                                                            "'-'", "'ax'", 
                                                            "'bx'", "'cx'", 
                                                            "'dx'", "'bp'", 
                                                            "'sp'", "'['", 
                                                            "']'", "'mov'", 
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
                                                             null, "Comma", 
                                                             "Colon", "Comment", 
                                                             "INT", "Label", 
                                                             "STR", "WS" ];
	// tslint:disable:no-trailing-whitespace
	public static readonly ruleNames: string[] = [
		"line", "label", "comment", "op", "num", "reg", "offset", "mem", "mov", 
		"add", "sub", "mul", "div", "cmp", "jump", "call", "ret", "push", "pop", 
		"input", "str", "print", "rand", "halt",
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
		let _la: number;
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 49;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===39) {
				{
				this.state = 48;
				this.label();
				}
			}

			this.state = 52;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (((((_la - 11)) & ~0x1F) === 0 && ((1 << (_la - 11)) & 16777215) !== 0)) {
				{
				this.state = 51;
				this.op();
				}
			}

			this.state = 55;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===37) {
				{
				this.state = 54;
				this.comment();
				}
			}

			this.state = 57;
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
			this.state = 59;
			this.match(toy_asmParser.Label);
			this.state = 60;
			this.match(toy_asmParser.Colon);
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
	public comment(): CommentContext {
		let localctx: CommentContext = new CommentContext(this, this._ctx, this.state);
		this.enterRule(localctx, 4, toy_asmParser.RULE_comment);
		try {
			this.enterOuterAlt(localctx, 1);
			{
			this.state = 62;
			this.match(toy_asmParser.Comment);
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
			this.state = 79;
			this._errHandler.sync(this);
			switch (this._input.LA(1)) {
			case 11:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 64;
				this.mov();
				}
				break;
			case 12:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 65;
				this.add();
				}
				break;
			case 13:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 66;
				this.sub();
				}
				break;
			case 14:
				this.enterOuterAlt(localctx, 4);
				{
				this.state = 67;
				this.mul();
				}
				break;
			case 15:
				this.enterOuterAlt(localctx, 5);
				{
				this.state = 68;
				this.div();
				}
				break;
			case 16:
				this.enterOuterAlt(localctx, 6);
				{
				this.state = 69;
				this.cmp();
				}
				break;
			case 17:
			case 18:
			case 19:
			case 20:
			case 21:
			case 22:
			case 23:
				this.enterOuterAlt(localctx, 7);
				{
				this.state = 70;
				this.jump();
				}
				break;
			case 24:
				this.enterOuterAlt(localctx, 8);
				{
				this.state = 71;
				this.call();
				}
				break;
			case 25:
				this.enterOuterAlt(localctx, 9);
				{
				this.state = 72;
				this.ret();
				}
				break;
			case 26:
			case 27:
				this.enterOuterAlt(localctx, 10);
				{
				this.state = 73;
				this.push();
				}
				break;
			case 28:
			case 29:
				this.enterOuterAlt(localctx, 11);
				{
				this.state = 74;
				this.pop();
				}
				break;
			case 30:
				this.enterOuterAlt(localctx, 12);
				{
				this.state = 75;
				this.input();
				}
				break;
			case 31:
			case 32:
				this.enterOuterAlt(localctx, 13);
				{
				this.state = 76;
				this.print();
				}
				break;
			case 33:
				this.enterOuterAlt(localctx, 14);
				{
				this.state = 77;
				this.rand();
				}
				break;
			case 34:
				this.enterOuterAlt(localctx, 15);
				{
				this.state = 78;
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
			this.state = 87;
			this._errHandler.sync(this);
			switch (this._input.LA(1)) {
			case 1:
			case 38:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 82;
				this._errHandler.sync(this);
				_la = this._input.LA(1);
				if (_la===1) {
					{
					this.state = 81;
					this.match(toy_asmParser.T__0);
					}
				}

				this.state = 84;
				this.match(toy_asmParser.INT);
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 85;
				this.match(toy_asmParser.T__1);
				this.state = 86;
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
			this.state = 89;
			_la = this._input.LA(1);
			if(!((((_la) & ~0x1F) === 0 && ((1 << _la) & 504) !== 0))) {
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
			this.state = 91;
			_la = this._input.LA(1);
			if(!(_la===1 || _la===2)) {
			this._errHandler.recoverInline(this);
			}
			else {
				this._errHandler.reportMatch(this);
			    this.consume();
			}
			this.state = 92;
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
			this.state = 94;
			this.match(toy_asmParser.T__8);
			this.state = 95;
			this.reg();
			this.state = 97;
			this._errHandler.sync(this);
			_la = this._input.LA(1);
			if (_la===1 || _la===2) {
				{
				this.state = 96;
				this.offset();
				}
			}

			this.state = 99;
			this.match(toy_asmParser.T__9);
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
			this.state = 126;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 7, this._ctx) ) {
			case 1:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 101;
				this.match(toy_asmParser.T__10);
				this.state = 102;
				this.reg();
				this.state = 103;
				this.match(toy_asmParser.Comma);
				this.state = 104;
				this.num();
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 106;
				this.match(toy_asmParser.T__10);
				this.state = 107;
				this.reg();
				this.state = 108;
				this.match(toy_asmParser.Comma);
				this.state = 109;
				this.reg();
				}
				break;
			case 3:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 111;
				this.match(toy_asmParser.T__10);
				this.state = 112;
				this.reg();
				this.state = 113;
				this.match(toy_asmParser.Comma);
				this.state = 114;
				this.mem();
				}
				break;
			case 4:
				this.enterOuterAlt(localctx, 4);
				{
				this.state = 116;
				this.match(toy_asmParser.T__10);
				this.state = 117;
				this.mem();
				this.state = 118;
				this.match(toy_asmParser.Comma);
				this.state = 119;
				this.num();
				}
				break;
			case 5:
				this.enterOuterAlt(localctx, 5);
				{
				this.state = 121;
				this.match(toy_asmParser.T__10);
				this.state = 122;
				this.mem();
				this.state = 123;
				this.match(toy_asmParser.Comma);
				this.state = 124;
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
			this.state = 143;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 8, this._ctx) ) {
			case 1:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 128;
				this.match(toy_asmParser.T__11);
				this.state = 129;
				this.reg();
				this.state = 130;
				this.match(toy_asmParser.Comma);
				this.state = 131;
				this.num();
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 133;
				this.match(toy_asmParser.T__11);
				this.state = 134;
				this.reg();
				this.state = 135;
				this.match(toy_asmParser.Comma);
				this.state = 136;
				this.reg();
				}
				break;
			case 3:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 138;
				this.match(toy_asmParser.T__11);
				this.state = 139;
				this.reg();
				this.state = 140;
				this.match(toy_asmParser.Comma);
				this.state = 141;
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
			this.state = 160;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 9, this._ctx) ) {
			case 1:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 145;
				this.match(toy_asmParser.T__12);
				this.state = 146;
				this.reg();
				this.state = 147;
				this.match(toy_asmParser.Comma);
				this.state = 148;
				this.num();
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 150;
				this.match(toy_asmParser.T__12);
				this.state = 151;
				this.reg();
				this.state = 152;
				this.match(toy_asmParser.Comma);
				this.state = 153;
				this.reg();
				}
				break;
			case 3:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 155;
				this.match(toy_asmParser.T__12);
				this.state = 156;
				this.reg();
				this.state = 157;
				this.match(toy_asmParser.Comma);
				this.state = 158;
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
			this.state = 168;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 10, this._ctx) ) {
			case 1:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 162;
				this.match(toy_asmParser.T__13);
				this.state = 163;
				this.num();
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 164;
				this.match(toy_asmParser.T__13);
				this.state = 165;
				this.reg();
				}
				break;
			case 3:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 166;
				this.match(toy_asmParser.T__13);
				this.state = 167;
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
			this.state = 176;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 11, this._ctx) ) {
			case 1:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 170;
				this.match(toy_asmParser.T__14);
				this.state = 171;
				this.num();
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 172;
				this.match(toy_asmParser.T__14);
				this.state = 173;
				this.reg();
				}
				break;
			case 3:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 174;
				this.match(toy_asmParser.T__14);
				this.state = 175;
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
			this.state = 193;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 12, this._ctx) ) {
			case 1:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 178;
				this.match(toy_asmParser.T__15);
				this.state = 179;
				this.reg();
				this.state = 180;
				this.match(toy_asmParser.Comma);
				this.state = 181;
				this.num();
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 183;
				this.match(toy_asmParser.T__15);
				this.state = 184;
				this.reg();
				this.state = 185;
				this.match(toy_asmParser.Comma);
				this.state = 186;
				this.reg();
				}
				break;
			case 3:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 188;
				this.match(toy_asmParser.T__15);
				this.state = 189;
				this.reg();
				this.state = 190;
				this.match(toy_asmParser.Comma);
				this.state = 191;
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
			this.state = 209;
			this._errHandler.sync(this);
			switch (this._input.LA(1)) {
			case 17:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 195;
				this.match(toy_asmParser.T__16);
				this.state = 196;
				this.match(toy_asmParser.Label);
				}
				break;
			case 18:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 197;
				this.match(toy_asmParser.T__17);
				this.state = 198;
				this.match(toy_asmParser.Label);
				}
				break;
			case 19:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 199;
				this.match(toy_asmParser.T__18);
				this.state = 200;
				this.match(toy_asmParser.Label);
				}
				break;
			case 20:
				this.enterOuterAlt(localctx, 4);
				{
				this.state = 201;
				this.match(toy_asmParser.T__19);
				this.state = 202;
				this.match(toy_asmParser.Label);
				}
				break;
			case 21:
				this.enterOuterAlt(localctx, 5);
				{
				this.state = 203;
				this.match(toy_asmParser.T__20);
				this.state = 204;
				this.match(toy_asmParser.Label);
				}
				break;
			case 22:
				this.enterOuterAlt(localctx, 6);
				{
				this.state = 205;
				this.match(toy_asmParser.T__21);
				this.state = 206;
				this.match(toy_asmParser.Label);
				}
				break;
			case 23:
				this.enterOuterAlt(localctx, 7);
				{
				this.state = 207;
				this.match(toy_asmParser.T__22);
				this.state = 208;
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
			this.state = 211;
			this.match(toy_asmParser.T__23);
			this.state = 212;
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
			this.state = 214;
			this.match(toy_asmParser.T__24);
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
			this.state = 221;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 14, this._ctx) ) {
			case 1:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 216;
				this.match(toy_asmParser.T__25);
				this.state = 217;
				this.num();
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 218;
				this.match(toy_asmParser.T__25);
				this.state = 219;
				this.reg();
				}
				break;
			case 3:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 220;
				this.match(toy_asmParser.T__26);
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
			this.state = 227;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 15, this._ctx) ) {
			case 1:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 223;
				this.match(toy_asmParser.T__27);
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 224;
				this.match(toy_asmParser.T__27);
				this.state = 225;
				this.reg();
				}
				break;
			case 3:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 226;
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
	public input(): InputContext {
		let localctx: InputContext = new InputContext(this, this._ctx, this.state);
		this.enterRule(localctx, 38, toy_asmParser.RULE_input);
		try {
			this.state = 233;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 16, this._ctx) ) {
			case 1:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 229;
				this.match(toy_asmParser.T__29);
				this.state = 230;
				this.reg();
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 231;
				this.match(toy_asmParser.T__29);
				this.state = 232;
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
			this.state = 235;
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
			this.state = 254;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 17, this._ctx) ) {
			case 1:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 237;
				this.match(toy_asmParser.T__30);
				this.state = 238;
				this.num();
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 239;
				this.match(toy_asmParser.T__30);
				this.state = 240;
				this.reg();
				}
				break;
			case 3:
				this.enterOuterAlt(localctx, 3);
				{
				this.state = 241;
				this.match(toy_asmParser.T__30);
				this.state = 242;
				this.mem();
				}
				break;
			case 4:
				this.enterOuterAlt(localctx, 4);
				{
				this.state = 243;
				this.match(toy_asmParser.T__30);
				this.state = 244;
				this.str();
				}
				break;
			case 5:
				this.enterOuterAlt(localctx, 5);
				{
				this.state = 245;
				this.match(toy_asmParser.T__31);
				this.state = 246;
				this.num();
				}
				break;
			case 6:
				this.enterOuterAlt(localctx, 6);
				{
				this.state = 247;
				this.match(toy_asmParser.T__31);
				this.state = 248;
				this.reg();
				}
				break;
			case 7:
				this.enterOuterAlt(localctx, 7);
				{
				this.state = 249;
				this.match(toy_asmParser.T__31);
				this.state = 250;
				this.mem();
				}
				break;
			case 8:
				this.enterOuterAlt(localctx, 8);
				{
				this.state = 251;
				this.match(toy_asmParser.T__31);
				this.state = 252;
				this.str();
				}
				break;
			case 9:
				this.enterOuterAlt(localctx, 9);
				{
				this.state = 253;
				this.match(toy_asmParser.T__31);
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
			this.state = 260;
			this._errHandler.sync(this);
			switch ( this._interp.adaptivePredict(this._input, 18, this._ctx) ) {
			case 1:
				this.enterOuterAlt(localctx, 1);
				{
				this.state = 256;
				this.match(toy_asmParser.T__32);
				this.state = 257;
				this.reg();
				}
				break;
			case 2:
				this.enterOuterAlt(localctx, 2);
				{
				this.state = 258;
				this.match(toy_asmParser.T__32);
				this.state = 259;
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
			this.state = 262;
			this.match(toy_asmParser.T__33);
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

	public static readonly _serializedATN: number[] = [4,1,41,265,2,0,7,0,2,
	1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,
	10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,
	7,17,2,18,7,18,2,19,7,19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,3,
	0,50,8,0,1,0,3,0,53,8,0,1,0,3,0,56,8,0,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,3,
	1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,80,8,3,1,4,
	3,4,83,8,4,1,4,1,4,1,4,3,4,88,8,4,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,3,7,98,
	8,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
	1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,127,8,8,1,9,1,9,1,9,1,9,1,9,
	1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,144,8,9,1,10,1,10,1,10,1,10,
	1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,161,8,10,1,
	11,1,11,1,11,1,11,1,11,1,11,3,11,169,8,11,1,12,1,12,1,12,1,12,1,12,1,12,
	3,12,177,8,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
	13,1,13,1,13,1,13,3,13,194,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
	1,14,1,14,1,14,1,14,1,14,1,14,3,14,210,8,14,1,15,1,15,1,15,1,16,1,16,1,
	17,1,17,1,17,1,17,1,17,3,17,222,8,17,1,18,1,18,1,18,1,18,3,18,228,8,18,
	1,19,1,19,1,19,1,19,3,19,234,8,19,1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,
	21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,255,8,21,
	1,22,1,22,1,22,1,22,3,22,261,8,22,1,23,1,23,1,23,0,0,24,0,2,4,6,8,10,12,
	14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,0,2,1,0,3,8,1,0,1,2,
	294,0,49,1,0,0,0,2,59,1,0,0,0,4,62,1,0,0,0,6,79,1,0,0,0,8,87,1,0,0,0,10,
	89,1,0,0,0,12,91,1,0,0,0,14,94,1,0,0,0,16,126,1,0,0,0,18,143,1,0,0,0,20,
	160,1,0,0,0,22,168,1,0,0,0,24,176,1,0,0,0,26,193,1,0,0,0,28,209,1,0,0,0,
	30,211,1,0,0,0,32,214,1,0,0,0,34,221,1,0,0,0,36,227,1,0,0,0,38,233,1,0,
	0,0,40,235,1,0,0,0,42,254,1,0,0,0,44,260,1,0,0,0,46,262,1,0,0,0,48,50,3,
	2,1,0,49,48,1,0,0,0,49,50,1,0,0,0,50,52,1,0,0,0,51,53,3,6,3,0,52,51,1,0,
	0,0,52,53,1,0,0,0,53,55,1,0,0,0,54,56,3,4,2,0,55,54,1,0,0,0,55,56,1,0,0,
	0,56,57,1,0,0,0,57,58,5,0,0,1,58,1,1,0,0,0,59,60,5,39,0,0,60,61,5,36,0,
	0,61,3,1,0,0,0,62,63,5,37,0,0,63,5,1,0,0,0,64,80,3,16,8,0,65,80,3,18,9,
	0,66,80,3,20,10,0,67,80,3,22,11,0,68,80,3,24,12,0,69,80,3,26,13,0,70,80,
	3,28,14,0,71,80,3,30,15,0,72,80,3,32,16,0,73,80,3,34,17,0,74,80,3,36,18,
	0,75,80,3,38,19,0,76,80,3,42,21,0,77,80,3,44,22,0,78,80,3,46,23,0,79,64,
	1,0,0,0,79,65,1,0,0,0,79,66,1,0,0,0,79,67,1,0,0,0,79,68,1,0,0,0,79,69,1,
	0,0,0,79,70,1,0,0,0,79,71,1,0,0,0,79,72,1,0,0,0,79,73,1,0,0,0,79,74,1,0,
	0,0,79,75,1,0,0,0,79,76,1,0,0,0,79,77,1,0,0,0,79,78,1,0,0,0,80,7,1,0,0,
	0,81,83,5,1,0,0,82,81,1,0,0,0,82,83,1,0,0,0,83,84,1,0,0,0,84,88,5,38,0,
	0,85,86,5,2,0,0,86,88,5,38,0,0,87,82,1,0,0,0,87,85,1,0,0,0,88,9,1,0,0,0,
	89,90,7,0,0,0,90,11,1,0,0,0,91,92,7,1,0,0,92,93,5,38,0,0,93,13,1,0,0,0,
	94,95,5,9,0,0,95,97,3,10,5,0,96,98,3,12,6,0,97,96,1,0,0,0,97,98,1,0,0,0,
	98,99,1,0,0,0,99,100,5,10,0,0,100,15,1,0,0,0,101,102,5,11,0,0,102,103,3,
	10,5,0,103,104,5,35,0,0,104,105,3,8,4,0,105,127,1,0,0,0,106,107,5,11,0,
	0,107,108,3,10,5,0,108,109,5,35,0,0,109,110,3,10,5,0,110,127,1,0,0,0,111,
	112,5,11,0,0,112,113,3,10,5,0,113,114,5,35,0,0,114,115,3,14,7,0,115,127,
	1,0,0,0,116,117,5,11,0,0,117,118,3,14,7,0,118,119,5,35,0,0,119,120,3,8,
	4,0,120,127,1,0,0,0,121,122,5,11,0,0,122,123,3,14,7,0,123,124,5,35,0,0,
	124,125,3,10,5,0,125,127,1,0,0,0,126,101,1,0,0,0,126,106,1,0,0,0,126,111,
	1,0,0,0,126,116,1,0,0,0,126,121,1,0,0,0,127,17,1,0,0,0,128,129,5,12,0,0,
	129,130,3,10,5,0,130,131,5,35,0,0,131,132,3,8,4,0,132,144,1,0,0,0,133,134,
	5,12,0,0,134,135,3,10,5,0,135,136,5,35,0,0,136,137,3,10,5,0,137,144,1,0,
	0,0,138,139,5,12,0,0,139,140,3,10,5,0,140,141,5,35,0,0,141,142,3,14,7,0,
	142,144,1,0,0,0,143,128,1,0,0,0,143,133,1,0,0,0,143,138,1,0,0,0,144,19,
	1,0,0,0,145,146,5,13,0,0,146,147,3,10,5,0,147,148,5,35,0,0,148,149,3,8,
	4,0,149,161,1,0,0,0,150,151,5,13,0,0,151,152,3,10,5,0,152,153,5,35,0,0,
	153,154,3,10,5,0,154,161,1,0,0,0,155,156,5,13,0,0,156,157,3,10,5,0,157,
	158,5,35,0,0,158,159,3,14,7,0,159,161,1,0,0,0,160,145,1,0,0,0,160,150,1,
	0,0,0,160,155,1,0,0,0,161,21,1,0,0,0,162,163,5,14,0,0,163,169,3,8,4,0,164,
	165,5,14,0,0,165,169,3,10,5,0,166,167,5,14,0,0,167,169,3,14,7,0,168,162,
	1,0,0,0,168,164,1,0,0,0,168,166,1,0,0,0,169,23,1,0,0,0,170,171,5,15,0,0,
	171,177,3,8,4,0,172,173,5,15,0,0,173,177,3,10,5,0,174,175,5,15,0,0,175,
	177,3,14,7,0,176,170,1,0,0,0,176,172,1,0,0,0,176,174,1,0,0,0,177,25,1,0,
	0,0,178,179,5,16,0,0,179,180,3,10,5,0,180,181,5,35,0,0,181,182,3,8,4,0,
	182,194,1,0,0,0,183,184,5,16,0,0,184,185,3,10,5,0,185,186,5,35,0,0,186,
	187,3,10,5,0,187,194,1,0,0,0,188,189,5,16,0,0,189,190,3,10,5,0,190,191,
	5,35,0,0,191,192,3,14,7,0,192,194,1,0,0,0,193,178,1,0,0,0,193,183,1,0,0,
	0,193,188,1,0,0,0,194,27,1,0,0,0,195,196,5,17,0,0,196,210,5,39,0,0,197,
	198,5,18,0,0,198,210,5,39,0,0,199,200,5,19,0,0,200,210,5,39,0,0,201,202,
	5,20,0,0,202,210,5,39,0,0,203,204,5,21,0,0,204,210,5,39,0,0,205,206,5,22,
	0,0,206,210,5,39,0,0,207,208,5,23,0,0,208,210,5,39,0,0,209,195,1,0,0,0,
	209,197,1,0,0,0,209,199,1,0,0,0,209,201,1,0,0,0,209,203,1,0,0,0,209,205,
	1,0,0,0,209,207,1,0,0,0,210,29,1,0,0,0,211,212,5,24,0,0,212,213,5,39,0,
	0,213,31,1,0,0,0,214,215,5,25,0,0,215,33,1,0,0,0,216,217,5,26,0,0,217,222,
	3,8,4,0,218,219,5,26,0,0,219,222,3,10,5,0,220,222,5,27,0,0,221,216,1,0,
	0,0,221,218,1,0,0,0,221,220,1,0,0,0,222,35,1,0,0,0,223,228,5,28,0,0,224,
	225,5,28,0,0,225,228,3,10,5,0,226,228,5,29,0,0,227,223,1,0,0,0,227,224,
	1,0,0,0,227,226,1,0,0,0,228,37,1,0,0,0,229,230,5,30,0,0,230,234,3,10,5,
	0,231,232,5,30,0,0,232,234,3,14,7,0,233,229,1,0,0,0,233,231,1,0,0,0,234,
	39,1,0,0,0,235,236,5,40,0,0,236,41,1,0,0,0,237,238,5,31,0,0,238,255,3,8,
	4,0,239,240,5,31,0,0,240,255,3,10,5,0,241,242,5,31,0,0,242,255,3,14,7,0,
	243,244,5,31,0,0,244,255,3,40,20,0,245,246,5,32,0,0,246,255,3,8,4,0,247,
	248,5,32,0,0,248,255,3,10,5,0,249,250,5,32,0,0,250,255,3,14,7,0,251,252,
	5,32,0,0,252,255,3,40,20,0,253,255,5,32,0,0,254,237,1,0,0,0,254,239,1,0,
	0,0,254,241,1,0,0,0,254,243,1,0,0,0,254,245,1,0,0,0,254,247,1,0,0,0,254,
	249,1,0,0,0,254,251,1,0,0,0,254,253,1,0,0,0,255,43,1,0,0,0,256,257,5,33,
	0,0,257,261,3,10,5,0,258,259,5,33,0,0,259,261,3,14,7,0,260,256,1,0,0,0,
	260,258,1,0,0,0,261,45,1,0,0,0,262,263,5,34,0,0,263,47,1,0,0,0,19,49,52,
	55,79,82,87,97,126,143,160,168,176,193,209,221,227,233,254,260];

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
	public op(): OpContext {
		return this.getTypedRuleContext(OpContext, 0) as OpContext;
	}
	public comment(): CommentContext {
		return this.getTypedRuleContext(CommentContext, 0) as CommentContext;
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
	public Colon(): TerminalNode {
		return this.getToken(toy_asmParser.Colon, 0);
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


export class CommentContext extends ParserRuleContext {
	constructor(parser?: toy_asmParser, parent?: ParserRuleContext, invokingState?: number) {
		super(parent, invokingState);
    	this.parser = parser;
	}
	public Comment(): TerminalNode {
		return this.getToken(toy_asmParser.Comment, 0);
	}
    public get ruleIndex(): number {
    	return toy_asmParser.RULE_comment;
	}
	// @Override
	public accept<Result>(visitor: toy_asmVisitor<Result>): Result {
		if (visitor.visitComment) {
			return visitor.visitComment(this);
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
	public Comma(): TerminalNode {
		return this.getToken(toy_asmParser.Comma, 0);
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
	public Comma(): TerminalNode {
		return this.getToken(toy_asmParser.Comma, 0);
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
	public Comma(): TerminalNode {
		return this.getToken(toy_asmParser.Comma, 0);
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
	public Comma(): TerminalNode {
		return this.getToken(toy_asmParser.Comma, 0);
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
