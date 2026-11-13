import {CharStream, CommonTokenStream, ErrorListener, RecognitionException, type Recognizer} from 'antlr4';
import toy_asmLexer from './grammar/toy_asmLexer';
import toy_asmParser from './grammar/toy_asmParser';
import {VisitorImpl, type ParsedOp} from './VisitorImpl';
import {Operation} from './Operation';
import {instructionHelp} from './instructionHelp';

// Derive reserved words from the grammar, including instruction and register names.
const reservedWords = new Set(toy_asmLexer.literalNames
    .filter((name): name is string => name !== null && /^'[a-z]+'$/.test(name))
    .map(name => name.slice(1, -1)));

// if parse error
export class CompileError {
    constructor(
        public line: string,
        public lineNum: number,
        public column: number,
        public message: string,
        public length: number = 1
    ) {
    }

    toString(): string {
        return `第 ${this.lineNum + 1} 行，第 ${this.column + 1} 列:\n`
            + `${this.line}\n`
            + `${' '.repeat(this.column)}^ ${this.message}`;
    }
}

interface ParsedLineInfo {
    lineNum: number;
    src: string;
    label: string | null;
    op: ParsedOp | null;
}

export interface CompileResult {
    success: boolean;
    operations: Operation[];
    firstError: CompileError | null;
    errors: CompileError[];
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
        const token = _offendingSymbol?.text;
        let detail = token === '<EOF>'
            ? '指令不完整，行尾缺少操作数或符号。'
            : token ? `无法在此处使用「${token}」。` : '无法识别此处的字符；请检查标点、字符串引号和转义符。';
        if (_recognizer instanceof toy_asmParser && !msg.startsWith('no viable alternative')) {
            const expected = _recognizer.getExpectedTokens().toString(
                toy_asmParser.literalNames.map(name => name ?? ''), toy_asmParser.symbolicNames.map(name => name ?? '')
            ).replace(/<EOF>/g, '行尾').replace(/INT/g, '整数').replace(/Label/g, '标签名')
             .replace(/STR/g, '双引号字符串').replace(/Comma/g, '逗号').replace(/Colon/g, '冒号');
            detail += ` 这里需要：${expected}。`;
        }
        this.errors.push(new CompileError('', 0, column, detail,
            token && token !== '<EOF>' ? token.length : 1));
    }
}

export class Compiler {
    compile(source: string): CompileResult {
        const rawLines = source.split('\n');
        const parsedLines: ParsedLineInfo[] = [];
        const visitor = new VisitorImpl();

        // Keep one primary syntax diagnostic per line to avoid recovery cascades.
        const errors: CompileError[] = [];

        // Stage 1: Parse each line
        for (let i = 0; i < rawLines.length; i++) {
            const line = rawLines[i];
            const labelDefinition = /^(\s*)([a-z_][a-z0-9_]*)\s*[:：]/i.exec(line);
            if (labelDefinition && reservedWords.has(labelDefinition[2].toLowerCase())) {
                const name = labelDefinition[2];
                errors.push(new CompileError(line, i, labelDefinition[1].length,
                    `关键字 ${name} 不能用作标签。`, name.length));
                continue;
            }
            const lexer = new toy_asmLexer(new CharStream(line));
            const tokenStream = new CommonTokenStream(lexer);
            const parser = new toy_asmParser(tokenStream);
            const errorListener = new CompileErrorListener();
            lexer.removeErrorListeners();
            parser.removeErrorListeners();
            lexer.addErrorListener(errorListener);
            parser.addErrorListener(errorListener);

            // compile
            const tree = parser.line();

            // error
            if (errorListener.errors.length > 0) {
                const error = errorListener.errors[0];
                error.line = line;
                error.lineNum = i;
                const instruction = line.replace(/^\s*[a-z_][a-z0-9_]*\s*[:：]/i, '').trim().split(/\s+/)[0].toLowerCase();
                const code = line.replace(/^\s*[a-z_][a-z0-9_]*\s*[:：]/i, '').trim();
                if (['mov', 'add', 'sub', 'cmp'].includes(instruction) && !/[,，]/.test(code.split(/[;；]/)[0])) {
                    error.message = '缺少逗号。两个操作数之间需要用逗号分隔，例如 mov ax, 1。';
                }
                const help = Object.hasOwn(instructionHelp, instruction) ? instructionHelp[instruction] : null;
                error.message += help ? `\n用法：${help}` : '\n请检查指令拼写；标签定义需要以冒号结尾。';
                errors.push(error);
                continue;
            }

            // Reject imprecise literals before converting them to JavaScript numbers.
            const invalidNumber = tokenStream.tokens.find(token => token.type === toy_asmLexer.INT && !Number.isSafeInteger(Number(token.text)));
            if (invalidNumber) {
                errors.push(new CompileError(line, i, invalidNumber.column,
                    '整数超出安全范围。整数及内存偏移必须在 -9007199254740991 到 9007199254740991 之间。', invalidNumber.text.length));
                continue;
            }

            // compile success
            const {label, op} = visitor.visitLine(tree);
            if (label || op) {
                parsedLines.push({lineNum: i, src: line, label, op});
            }
        }


        // Stage 2: Build operations and collect labels
        const operations: Operation[] = [];
        const labels: Record<string, number> = Object.create(null); // label --> op addr
        const labelLines: Record<string, number> = Object.create(null); // label --> first defined lineNum
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
                    errors.push(new CompileError(rawLines[lineNum], lineNum, rawLines[lineNum].indexOf(label), `重复的标签 '${label}'，首次出现在第 ${firstLine} 行。请为此标签改名，并更新对应的跳转。`, label.length));
                }
                if (!(label in labelLines)) labelLines[label] = lineNum;
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

                const operation = new Operation(
                    addr,
                    op.type!,
                    opLabels,
                    op.p1,
                    op.p2,
                    op.action,
                    op.target
                );
                operation.sourceLine = lineNum;
                operation.sourceText = rawLines[lineNum];
                operations.push(operation);
                opInfos.push({op: operation, line: lineNum});
            }
        }


        // Check for dangling labels (labels without following instruction)
        for (const pending of pendingLabels) {
            errors.push(new CompileError(rawLines[pending.line], pending.line, rawLines[pending.line].indexOf(pending.name),
                `标签 '${pending.name}' 后面没有指令。请在其后添加指令（例如 halt），或删除这个标签。`, pending.name.length));
        }

        // Stage 3: Validate and resolve label references
        for (const opInfo of opInfos) {
            const op = opInfo.op;
            if (op.target !== null) {
                if (!(op.target in labels)) {
                    errors.push(new CompileError(rawLines[opInfo.line], opInfo.line, rawLines[opInfo.line].indexOf(op.target), `没有定义标签: '${op.target}'。请添加 ${op.target}: 定义，或检查拼写及大小写。`, op.target.length));
                    continue;
                }
                op.resolveTarget(labels[op.target]);
            }
        }


        errors.sort((a, b) => a.lineNum - b.lineNum || a.column - b.column);
        return {success: errors.length === 0, operations: errors.length ? [] : operations, firstError: errors[0] ?? null, errors};
    }
}
