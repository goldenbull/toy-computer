import toy_asmVisitor from './grammar/toy_asmVisitor';
import {
    LineContext, LabelContext, OpContext, NumContext, RegContext, MemContext, OffsetContext, StrContext,
    MovContext, AddContext, SubContext, MulContext, DivContext, CmpContext,
    JumpContext, CallContext, RetContext, PushContext, PopContext,
    InputContext, PrintContext, RandContext, HaltContext, BreakContext
} from './grammar/toy_asmParser';
import {Operand, OperandType} from './Operand';

// Parsed operation data (before full Operation is created)
export interface ParsedOp {
    type: string;
    p1?: Operand | null;
    p2?: Operand | null;
    action?: string | null;
    target?: string | null;
}

export interface ParseResult {
    label: string | null;
    op: ParsedOp | null;
}

export class VisitorImpl extends toy_asmVisitor<any> {
    visitNum = (ctx: NumContext): Operand => {
        const val = parseInt(ctx.getText(), 10);
        return new Operand(OperandType.Imm, "", 0, val);
    };

    visitReg = (ctx: RegContext): Operand => {
        const regName = ctx.getText().toLowerCase();
        return new Operand(OperandType.Reg, regName);
    };

    visitOffset = (ctx: OffsetContext): number => {
        return parseInt(ctx.getText(), 10);
    };

    visitMem = (ctx: MemContext): Operand => {
        const regName = ctx.reg().getText().toLowerCase();
        const offsetCtx = ctx.offset();
        const offset = offsetCtx ? this.visitOffset(offsetCtx) : 0;
        return new Operand(OperandType.Mem, regName, offset);
    };

    visitStr = (ctx: StrContext): Operand => {
        const raw = ctx.getText();
        // Parse escape sequences for the evaluated form
        const evaluated = raw.slice(1, -1)
                             .replace(/\\n/g, '\n')
                             .replace(/\\t/g, '\t')
                             .replace(/\\r/g, '\r')
                             .replace(/\\"/g, '"')
                             .replace(/\\\\/g, '\\');
        return new Operand(OperandType.Str, "", 0, 0, [raw, evaluated]);
    };

    visitMov = (ctx: MovContext): ParsedOp => {
        const p1 = this.visit(ctx.getChild(1)) as Operand;
        const p2 = this.visit(ctx.getChild(3)) as Operand;
        return {type: 'mov', p1, p2};
    };

    visitAdd = (ctx: AddContext): ParsedOp => {
        const p1 = this.visit(ctx.getChild(1)) as Operand;
        const p2 = this.visit(ctx.getChild(3)) as Operand;
        return {type: 'add', p1, p2};
    };

    visitSub = (ctx: SubContext): ParsedOp => {
        const p1 = this.visit(ctx.getChild(1)) as Operand;
        const p2 = this.visit(ctx.getChild(3)) as Operand;
        return {type: 'sub', p1, p2};
    };

    visitMul = (ctx: MulContext): ParsedOp => {
        const p1 = this.visit(ctx.getChild(1)) as Operand;
        return {type: 'mul', p1};
    };

    visitDiv = (ctx: DivContext): ParsedOp => {
        const p1 = this.visit(ctx.getChild(1)) as Operand;
        return {type: 'div', p1};
    };

    visitCmp = (ctx: CmpContext): ParsedOp => {
        const p1 = this.visit(ctx.getChild(1)) as Operand;
        const p2 = this.visit(ctx.getChild(3)) as Operand;
        return {type: 'cmp', p1, p2};
    };

    visitJump = (ctx: JumpContext): ParsedOp => {
        const label = ctx.Label().getText();
        const action = ctx.getChild(0)!.getText().toLowerCase();
        return {type: 'jump', action, target: label};
    };

    visitCall = (ctx: CallContext): ParsedOp => {
        const label = ctx.Label().getText();
        return {type: 'call', target: label};
    };

    visitRet = (_ctx: RetContext): ParsedOp => {
        return {type: 'ret'};
    };

    visitPush = (ctx: PushContext): ParsedOp => {
        const action = ctx.getChild(0)!.getText().toLowerCase();
        if (action === 'pushf') {
            return {type: 'push', action: 'pushf'};
        }
        const p1 = this.visit(ctx.getChild(1)) as Operand;
        return {type: 'push', action: 'push', p1};
    };

    visitPop = (ctx: PopContext): ParsedOp => {
        const action = ctx.getChild(0)!.getText().toLowerCase();
        if (action === 'popf') {
            return {type: 'pop', action: 'popf'};
        }
        if (ctx.getChildCount() === 1) {
            return {type: 'pop', action: 'pop'};
        }
        const p1 = this.visit(ctx.getChild(1)) as Operand;
        return {type: 'pop', action: 'pop', p1};
    };

    visitInput = (ctx: InputContext): ParsedOp => {
        const p1 = this.visit(ctx.getChild(1)) as Operand;
        return {type: 'input', p1};
    };

    visitPrint = (ctx: PrintContext): ParsedOp => {
        const action = ctx.getChild(0)!.getText().toLowerCase() as 'print' | 'println';
        if (ctx.getChildCount() === 1) {
            return {type: 'print', action, p1: null};
        }
        const p1 = this.visit(ctx.getChild(1)) as Operand;
        return {type: 'print', action, p1};
    };

    visitRand = (ctx: RandContext): ParsedOp => {
        const p1 = this.visit(ctx.getChild(1)) as Operand;
        return {type: 'rand', p1};
    };

    visitBreak = (ctx: BreakContext): ParsedOp => {
        return {type: 'break'};
    }

    visitHalt = (_ctx: HaltContext): ParsedOp => {
        return {type: 'halt'};
    };

    visitLine = (ctx: LineContext): ParseResult => {
        const labelCtx = ctx.label();
        const opCtx = ctx.op();

        const label = labelCtx ? labelCtx.Label().getText() : null;

        let op: ParsedOp | null = null;
        if (opCtx) {
            const child = opCtx.getChild(0);
            if (child) {
                op = this.visit(child) as ParsedOp;
            }
        }

        return {label, op};
    };
}
