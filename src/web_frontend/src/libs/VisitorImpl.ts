import toy_asmVisitor from './grammar/toy_asmVisitor';
import {
    LineContext, LabelContext, Label_and_opContext, OpContext, NumContext, RegContext, MemContext, OffsetContext, StrContext,
    MovContext, AddContext, SubContext, MulContext, DivContext, CmpContext,
    JumpContext, CallContext, RetContext, PushContext, PopContext,
    InputContext, PrintContext, RandContext, HaltContext
} from './grammar/toy_asmParser';
import {Operation} from './Operation';
import {Operand, OperandType} from './Operand';

export interface SourcePosition {
    line: number;
    column: number;
}

export interface ParsedLabel {
    name: string;
    position: SourcePosition;
}

export interface ParsedOp {
    op: Partial<Operation>;
    position: SourcePosition;
}

export interface ParsedLine {
    op: ParsedOp | null;
    label: ParsedLabel | null;
}

type PartialOp = Partial<Operation>;

export class VisitorImpl extends toy_asmVisitor<any> {
    visitNum = (ctx: NumContext): Operand => {
        const text = ctx.getText();
        const val = parseInt(text, 10);
        return new Operand({tp: OperandType.Imm, immVal: val});
    };

    visitReg = (ctx: RegContext): Operand => {
        const regName = ctx.getText();
        return new Operand({tp: OperandType.Reg, reg: regName});
    };

    visitOffset = (ctx: OffsetContext): number => {
        const text = ctx.getText();
        return parseInt(text, 10);
    };

    visitMem = (ctx: MemContext): Operand => {
        const regCtx = ctx.reg();
        const reg = regCtx.getText();
        const offsetCtx = ctx.offset();
        const offset = offsetCtx ? this.visitOffset(offsetCtx) : 0;
        return new Operand({tp: OperandType.Mem, reg, offset});
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
        return new Operand({tp: OperandType.Str, text: [raw, evaluated]});
    };

    visitMov = (ctx: MovContext): Partial<Operation> => {
        // Grammar: 'mov' (reg|mem) ',' (num|reg|mem)
        // Children[0] = 'mov', Children[1] = first operand, Children[2] = ',', Children[3] = second operand
        const p1 = this.visit(ctx.getChild(1)) as Operand;
        const p2 = this.visit(ctx.getChild(3)) as Operand;
        return {type: 'mov', p1, p2};
    };

    visitAdd = (ctx: AddContext): Partial<Operation> => {
        // Grammar: 'add' reg ',' (num|reg|mem)
        const p1 = this.visit(ctx.getChild(1)) as Operand;
        const p2 = this.visit(ctx.getChild(3)) as Operand;
        return {type: 'add', p1, p2};
    };

    visitSub = (ctx: SubContext): Partial<Operation> => {
        // Grammar: 'sub' reg ',' (num|reg|mem)
        const p1 = this.visit(ctx.getChild(1)) as Operand;
        const p2 = this.visit(ctx.getChild(3)) as Operand;
        return {type: 'sub', p1, p2};
    };

    visitMul = (ctx: MulContext): Partial<Operation> => {
        // Grammar: 'mul' (num|reg|mem)
        const p1 = this.visit(ctx.getChild(1)) as Operand;
        return {type: 'mul', p1};
    };

    visitDiv = (ctx: DivContext): Partial<Operation> => {
        // Grammar: 'div' (num|reg|mem)
        const p1 = this.visit(ctx.getChild(1)) as Operand;
        return {type: 'div', p1};
    };

    visitCmp = (ctx: CmpContext): Partial<Operation> => {
        // Grammar: 'cmp' reg ',' (num|reg|mem)
        const p1 = this.visit(ctx.getChild(1)) as Operand;
        const p2 = this.visit(ctx.getChild(3)) as Operand;
        return {type: 'cmp', p1, p2};
    };

    visitJump = (ctx: JumpContext): Partial<Operation> => {
        const label = ctx.Label().getText();
        const action = ctx.getChild(0)!.getText();
        return {type: 'jump', action, target: label};
    };

    visitCall = (ctx: CallContext): Partial<Operation> => {
        const label = ctx.Label().getText();
        return {type: 'call', target: label};
    };

    visitRet = (_ctx: RetContext): Partial<Operation> => {
        return {type: 'ret'};
    };

    visitPush = (ctx: PushContext): Partial<Operation> => {
        // Grammar: 'push' (num|reg) | 'pushf'
        const action = ctx.getChild(0)!.getText();
        if (action === 'pushf') {
            return {type: 'push', action: 'pushf'};
        }
        const p1 = this.visit(ctx.getChild(1)) as Operand;
        return {type: 'push', action: 'push', p1};
    };

    visitPop = (ctx: PopContext): Partial<Operation> => {
        // Grammar: 'pop' | 'pop' reg | 'popf'
        const action = ctx.getChild(0)!.getText();
        if (action === 'popf') {
            return {type: 'pop', action: 'popf'};
        }
        if (ctx.getChildCount() === 1) {
            return {type: 'pop', action: 'pop'};
        }
        const p1 = this.visit(ctx.getChild(1)) as Operand;
        return {type: 'pop', action: 'pop', p1};
    };

    visitInput = (ctx: InputContext): Partial<Operation> => {
        // Grammar: 'input' (reg|mem)
        const p1 = this.visit(ctx.getChild(1)) as Operand;
        return {type: 'input', p1};
    };

    visitPrint = (ctx: PrintContext): Partial<Operation> => {
        // Grammar: 'print'/'println' (num|reg|mem|str)?
        const action = ctx.getChild(0)!.getText() as 'print' | 'println';
        if (ctx.getChildCount() === 1) {
            return {type: 'print', action, p1: null};
        }
        const p1 = this.visit(ctx.getChild(1)) as Operand;
        return {type: 'print', action, p1};
    };

    visitRand = (ctx: RandContext): Partial<Operation> => {
        // Grammar: 'rand' (reg|mem)
        const p1 = this.visit(ctx.getChild(1)) as Operand;
        return {type: 'rand', p1};
    };

    visitHalt = (_ctx: HaltContext): Partial<Operation> => {
        return {type: 'halt'};
    };

    visitLabel = (ctx: LabelContext): ParsedLabel => {
        const token = ctx.Label().symbol;
        return {
            name: ctx.Label().getText(),
            position: {
                line: token.line,
                column: token.column + 1  // ANTLR columns are 0-based, make 1-based
            }
        };
    };

    private parseOp = (opCtx: OpContext): ParsedOp => {
        const child = opCtx.getChild(0);
        if (!child) {
            throw new Error('Can not compile operation');
        }
        const op = this.visit(child) as Partial<Operation>;
        const startToken = opCtx.start;
        return {
            op,
            position: {
                line: startToken.line,
                column: startToken.column + 1  // ANTLR columns are 0-based, make 1-based
            }
        };
    };

    visitLabel_and_op = (ctx: Label_and_opContext): ParsedLine => {
        const label = this.visitLabel(ctx.label());
        const parsedOp = this.parseOp(ctx.op());
        return { op: parsedOp, label };
    };

    visitLine = (ctx: LineContext): ParsedLine => {
        // Check which alternative was matched
        const labelCtx = ctx.label();
        const labelAndOpCtx = ctx.label_and_op();
        const opCtx = ctx.op();

        if (labelAndOpCtx) {
            // label_and_op: label ':' op
            return this.visitLabel_and_op(labelAndOpCtx);
        } else if (labelCtx) {
            // label: Label ':' (standalone label, no op)
            const label = this.visitLabel(labelCtx);
            return { op: null, label };
        } else if (opCtx) {
            // op: just an operation
            const parsedOp = this.parseOp(opCtx);
            return { op: parsedOp, label: null };
        }

        throw new Error('Can not parse line');
    };
}
