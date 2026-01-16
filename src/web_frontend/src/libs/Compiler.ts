import { CharStream, CommonTokenStream, ErrorListener, RecognitionException, type Recognizer } from 'antlr4';
import toy_asmLexer from './grammar/toy_asmLexer';
import toy_asmParser from './grammar/toy_asmParser';
import { VisitorImpl, type ParsedLine, type SourcePosition } from './VisitorImpl';
import { Operation } from './Operation';

export interface CompileError {
    line: number;
    column: number;
    message: string;
}

export interface CompileResult {
    success: boolean;
    operations: Operation[];
    labels: Record<string, number>;
    errors: CompileError[];
}

interface PreprocessedLine {
    lineNum: number;
    content: string;
}

interface ParseResult {
    parsed: ParsedLine | null;
    errors: CompileError[];
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
    private preprocess(source: string): { lines: PreprocessedLine[], errors: CompileError[] } {
        const rawLines = source.split('\n');
        const result: PreprocessedLine[] = [];
        const errors: CompileError[] = [];

        for (let i = 0; i < rawLines.length; i++) {
            const lineNum = i + 1;
            const line = rawLines[i];
            const trimmed = line.trim();

            // Skip empty lines
            if (trimmed === '') continue;

            // Skip comment lines
            if (trimmed.startsWith(';')) continue;

            // Remove inline comments (but keep original indentation)
            const commentIdx = line.indexOf(';');
            const content = commentIdx !== -1 ? line.substring(0, commentIdx) : line;

            // Skip if line is only whitespace after removing comment
            if (content.trim() === '') continue;

            result.push({ lineNum, content });
        }

        return { lines: result, errors };
    }

    private parseLine(line: string, lineNum: number): ParseResult {
        const inputStream = new CharStream(line);
        const lexer = new toy_asmLexer(inputStream);
        const tokenStream = new CommonTokenStream(lexer);
        const parser = new toy_asmParser(tokenStream);

        // Set up custom error listener
        const errorListener = new CompileErrorListener(lineNum);
        lexer.removeErrorListeners();
        lexer.addErrorListener(errorListener);
        parser.removeErrorListeners();
        parser.addErrorListener(errorListener);

        const tree = parser.line();

        // If there were parse errors, return them
        if (errorListener.errors.length > 0) {
            return { parsed: null, errors: errorListener.errors };
        }

        const visitor = new VisitorImpl();
        const parsed = visitor.visitLine(tree);
        return { parsed, errors: [] };
    }

    compile(source: string): CompileResult {
        const { lines, errors } = this.preprocess(source);

        if (errors.length > 0) {
            return { success: false, operations: [], labels: {}, errors };
        }

        const operations: Operation[] = [];
        const labels: Record<string, number> = {};
        const labelPositions: Record<string, { line: number, column: number }> = {};  // Track where labels are defined
        const compileErrors: CompileError[] = [];

        // Track pending labels (standalone labels waiting for an instruction)
        let pendingLabels: { name: string, line: number, column: number }[] = [];

        // Track operation positions for error reporting
        interface OpInfo {
            op: Operation;
            line: number;
            column: number;
            targetPosition?: SourcePosition;  // Position of the target label reference
        }
        const opInfos: OpInfo[] = [];

        // First pass: parse all lines and build operations
        for (const preprocessed of lines) {
            const { parsed, errors: parseErrors } = this.parseLine(preprocessed.content, preprocessed.lineNum);

            if (parseErrors.length > 0) {
                compileErrors.push(...parseErrors);
                continue;
            }

            if (!parsed) {
                continue;
            }

            // Collect label if present
            if (parsed.label) {
                const labelName = parsed.label.name;
                if (labelName in labels) {
                    const existingPos = labelPositions[labelName];
                    compileErrors.push({
                        line: preprocessed.lineNum,
                        column: parsed.label.position.column,
                        message: `Duplicate label '${labelName}' (first defined at line ${existingPos.line}, column ${existingPos.column})`
                    });
                } else {
                    pendingLabels.push({
                        name: labelName,
                        line: preprocessed.lineNum,
                        column: parsed.label.position.column
                    });
                }
            }

            // If there's an operation, create it
            if (parsed.op) {
                const addr = operations.length;

                // Register all pending labels for this instruction
                const opLabels: string[] = [];
                for (const pending of pendingLabels) {
                    if (!(pending.name in labels)) {
                        labels[pending.name] = addr;
                        labelPositions[pending.name] = { line: pending.line, column: pending.column };
                        opLabels.push(pending.name);
                    }
                }
                pendingLabels = [];

                const op = new Operation({
                    addr,
                    type: parsed.op.op.type,
                    labels: opLabels,
                    p1: parsed.op.op.p1 || null,
                    p2: parsed.op.op.p2 || null,
                    action: parsed.op.op.action || null,
                    target: parsed.op.op.target || null,
                    cnt: parsed.op.op.cnt || null
                });
                operations.push(op);
                opInfos.push({
                    op,
                    line: preprocessed.lineNum,
                    column: parsed.op.position.column
                });
            }
        }

        // Check for dangling labels (labels without following instruction)
        if (pendingLabels.length > 0) {
            for (const pending of pendingLabels) {
                compileErrors.push({
                    line: pending.line,
                    column: pending.column,
                    message: `Label '${pending.name}' has no instruction following it`
                });
            }
        }

        if (compileErrors.length > 0) {
            return { success: false, operations: [], labels: {}, errors: compileErrors };
        }

        // Second pass: validate label references
        for (const opInfo of opInfos) {
            const op = opInfo.op;
            if (op.target !== null && !(op.target in labels)) {
                compileErrors.push({
                    line: opInfo.line,
                    column: opInfo.column,
                    message: `Undefined label '${op.target}'`
                });
            }
        }

        if (compileErrors.length > 0) {
            return { success: false, operations: [], labels: {}, errors: compileErrors };
        }

        return { success: true, operations, labels, errors: [] };
    }

    // Helper to format error message with line and column
    static formatError(error: CompileError): string {
        return `Line ${error.line}, Column ${error.column}: ${error.message}`;
    }
}
