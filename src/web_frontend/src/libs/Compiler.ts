import {CharStream, CommonTokenStream, ErrorListener, RecognitionException, type Recognizer} from 'antlr4';
import toy_asmLexer from './grammar/toy_asmLexer';
import toy_asmParser from './grammar/toy_asmParser';
import {VisitorImpl} from './VisitorImpl';
import {Operation} from './Operation';

// if parse error
export class CompileError {
    constructor(
        public line: string,
        public lineNum: number,
        public column: number,
        public message: string
    ) {
    }

    toString(): string {
        return `第 ${this.lineNum + 1} 行:\n`
            + `${this.line}\n`
            + `${' '.repeat(this.column)}^ ${this.message}`;
    }
}

// if parse success
interface ParsedLineInfo {
    lineNum: number;
    src: string; // source code
    label: string | null;
    op: Partial<Operation> | null;
}

export interface CompileResult {
    success: boolean;
    operations: Operation[];
    labels: Record<string, number>;
    firstError: CompileError | null;
}

// Custom error listener to capture ANTLR parse errors
class CompileErrorListener extends ErrorListener<any> {
    errors: CompileError[] = [];

    syntaxError(
        _recognizer: Recognizer<any>,
        _offendingSymbol: any,
        _line: number,
        column: number,
        msg: string,
        _e: RecognitionException | undefined
    ): void {
        // set source and lineNum later
        // and we do not use antlr professional message
        this.errors.push(new CompileError("", 0, column, "语法错误，请检查"));
    }
}

export class Compiler {
    compile(source: string): CompileResult {
        const rawLines = source.split('\n');
        const parsedLines: ParsedLineInfo[] = [];
        const visitor = new VisitorImpl();

        // stop on first compile error
        let firstError: CompileError | null = null;

        // Stage 1: Parse each line
        for (let i = 0; i < rawLines.length; i++) {
            const line = rawLines[i];
            const lexer = new toy_asmLexer(new CharStream(line));
            const tokenStream = new CommonTokenStream(lexer);
            const parser = new toy_asmParser(tokenStream);
            const errorListener = new CompileErrorListener();
            lexer.addErrorListener(errorListener);
            parser.addErrorListener(errorListener);

            // compile
            const tree = parser.line();

            // error
            if (errorListener.errors.length > 0) {
                firstError = errorListener.errors[0];
                firstError.line = line;
                firstError.lineNum = i;
                break;
            }

            // compile success
            const {label, op} = visitor.visitLine(tree);
            if (label || op) {
                parsedLines.push({lineNum: i, src: line, label, op});
            }
        }

        if (firstError != null) {
            return {success: false, operations: [], labels: {}, firstError};
        }

        // Stage 2: Build operations and collect labels
        const operations: Operation[] = [];
        const labels: Record<string, number> = {}; // label --> op addr
        const labelLines: Record<string, number> = {}; // label --> first defined lineNum
        let pendingLabels: { name: string, line: number }[] = [];

        interface OpInfo {
            op: Operation;
            line: number;
        }

        const opInfos: OpInfo[] = [];

        for (const {lineNum, label, op} of parsedLines) {
            // Collect label if present
            if (label) {
                if (label in labelLines) {
                    const firstLine = labelLines[label] + 1; // 1-based for display
                    firstError = new CompileError(rawLines[lineNum], lineNum, 0, `重复的标签 '${label}'，首次出现在第 ${firstLine} 行`);
                    break;
                }
                labelLines[label] = lineNum;
                pendingLabels.push({name: label, line: lineNum});
            }

            // If there's an operation, create it
            if (op) {
                const addr = operations.length;

                // Register all pending labels for this instruction
                const opLabels: string[] = [];
                for (const pending of pendingLabels) {
                    if (!(pending.name in labels)) {
                        labels[pending.name] = addr;
                        opLabels.push(pending.name);
                    }
                }
                pendingLabels = [];

                const operation = new Operation({
                                                    addr,
                                                    type: op.type,
                                                    labels: opLabels,
                                                    p1: op.p1 || null,
                                                    p2: op.p2 || null,
                                                    action: op.action || null,
                                                    target: op.target || null,
                                                    cnt: op.cnt || null
                                                });
                operations.push(operation);
                opInfos.push({op: operation, line: lineNum});
            }
        }

        if (firstError != null) {
            return {success: false, operations: [], labels: {}, firstError};
        }

        // Check for dangling labels (labels without following instruction)
        if (pendingLabels.length > 0) {
            const pending = pendingLabels[0];
            firstError = new CompileError(rawLines[pending.line], pending.line, 0, `标签 '${pending.name}' 后面没有指令`);
            return {success: false, operations: [], labels: {}, firstError};
        }

        // Stage 3: Validate label references
        for (const opInfo of opInfos) {
            const op = opInfo.op;
            if (op.target !== null && !(op.target in labels)) {
                firstError = new CompileError(rawLines[opInfo.line], opInfo.line, 0, `没有定义标签: '${op.target}'`);
            }
        }

        if (firstError != null) {
            return {success: false, operations: [], labels: {}, firstError};
        }

        return {success: true, operations, labels, firstError};
    }
}
