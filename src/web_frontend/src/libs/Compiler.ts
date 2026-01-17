import {CharStream, CommonTokenStream, ErrorListener, RecognitionException, type Recognizer} from 'antlr4';
import toy_asmLexer from './grammar/toy_asmLexer';
import toy_asmParser from './grammar/toy_asmParser';
import {VisitorImpl} from './VisitorImpl';
import {Operation} from './Operation';

export interface CompileError {
    line: number; // 1-based line number
    column: number; // 1-based column number
    message: string;
}

export interface CompileResult {
    success: boolean;
    operations: Operation[];
    labels: Record<string, number>;
    errors: CompileError[];
}

// Stores parsed result for each line
interface ParsedLineInfo {
    lineNum: number; // 1-based
    label: string | null;
    op: Partial<Operation> | null;
}

// Custom error listener to capture ANTLR parse errors
class CompileErrorListener extends ErrorListener<any> {
    errors: CompileError[] = [];
    lineNum: number;

    constructor(lineNum: number) {
        super();
        this.lineNum = lineNum;
    }

    syntaxError(
        _recognizer: Recognizer<any>,
        _offendingSymbol: any,
        _line: number,
        column: number,
        msg: string,
        _e: RecognitionException | undefined
    ): void {
        this.errors.push({
            line: this.lineNum,
            column: column + 1,  // Make 1-based
            message: msg
        });
    }
}

export class Compiler {
    compile(source: string): CompileResult {
        const rawLines = source.split('\n');
        const compileErrors: CompileError[] = [];
        const parsedLines: ParsedLineInfo[] = [];

        // Create reusable lexer, token stream, parser, and visitor
        const lexer = new toy_asmLexer(new CharStream(''));
        const tokenStream = new CommonTokenStream(lexer);
        const parser = new toy_asmParser(tokenStream);
        const visitor = new VisitorImpl();

        // Set up error listener (will update lineNum for each line)
        const errorListener = new CompileErrorListener(0);
        lexer.removeErrorListeners();
        lexer.addErrorListener(errorListener);
        parser.removeErrorListeners();
        parser.addErrorListener(errorListener);

        // Stage 1: Parse each line
        for (let i = 0; i < rawLines.length; i++) {
            const lineNum = i + 1;
            const line = rawLines[i];

            // Reset lexer and parser for new input
            errorListener.lineNum = lineNum;
            errorListener.errors = [];
            lexer.inputStream = new CharStream(line);
            tokenStream.setTokenSource(lexer);
            parser.reset();

            const tree = parser.line();

            if (errorListener.errors.length > 0) {
                compileErrors.push(...errorListener.errors);
                continue;
            }

            const {label, op} = visitor.visitLine(tree);
            if (label || op) {
                parsedLines.push({lineNum, label, op});
            }
        }

        if (compileErrors.length > 0) {
            return {success: false, operations: [], labels: {}, errors: compileErrors};
        }

        // Stage 2: Build operations and collect labels
        const operations: Operation[] = [];
        const labels: Record<string, number> = {};
        let pendingLabels: {name: string, line: number}[] = [];

        interface OpInfo {
            op: Operation;
            line: number;
        }
        const opInfos: OpInfo[] = [];

        for (const {lineNum, label, op} of parsedLines) {
            // Collect label if present
            if (label) {
                if (label in labels) {
                    compileErrors.push({
                        line: lineNum,
                        column: 1,
                        message: `Duplicate label '${label}'`
                    });
                } else {
                    pendingLabels.push({name: label, line: lineNum});
                }
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

        // Check for dangling labels (labels without following instruction)
        for (const pending of pendingLabels) {
            compileErrors.push({
                line: pending.line,
                column: 1,
                message: `Label '${pending.name}' has no instruction following it`
            });
        }

        if (compileErrors.length > 0) {
            return {success: false, operations: [], labels: {}, errors: compileErrors};
        }

        // Stage 3: Validate label references
        for (const opInfo of opInfos) {
            const op = opInfo.op;
            if (op.target !== null && !(op.target in labels)) {
                compileErrors.push({
                    line: opInfo.line,
                    column: 1,
                    message: `Undefined label '${op.target}'`
                });
            }
        }

        if (compileErrors.length > 0) {
            return {success: false, operations: [], labels: {}, errors: compileErrors};
        }

        return {success: true, operations, labels, errors: []};
    }

    static formatError(error: CompileError): string {
        return `Line ${error.line}, Column ${error.column}: ${error.message}`;
    }
}
