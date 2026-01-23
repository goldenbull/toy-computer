import { StreamLanguage, LanguageSupport } from "@codemirror/language";

// Token types for toy assembly language
const instructions = new Set([
    "mov", "add", "sub", "mul", "div", "cmp",
    "jmp", "je", "jne", "jg", "jge", "jl", "jle",
    "call", "ret", "push", "pop", "pushf", "popf",
    "input", "print", "println", "rand",
    "break", "halt"
]);

const registers = new Set([
    "ax", "bx", "cx", "dx", "bp", "sp"
]);

// Stream parser for toy assembly
export const toyAsmLanguage = StreamLanguage.define({
    name: "toyasm",

    token(stream) {
        // Skip whitespace but track if we were at line start before whitespace
        const atLineStart = stream.sol();
        if (stream.eatSpace()) {
            return null;
        }

        // Comments start with ; or ；
        if (stream.match(/^[;；].*$/)) {
            return "comment";
        }

        // String literals
        if (stream.match(/^"(?:[^"\\]|\\.)*"/)) {
            return "string";
        }

        // Check for label definition (identifier followed by : or ：)
        // Labels can only appear at the start of a line (possibly after whitespace)
        if (atLineStart || stream.sol()) {
            const labelMatch = stream.match(/^[a-z_][a-z0-9_]*(?=\s*[:：])/i);
            if (labelMatch) {
                return "labelName";
            }
        }

        // Colon (label separator)
        if (stream.match(/^[:：]/)) {
            return "punctuation";
        }

        // Memory access brackets
        if (stream.match(/^[\[\]]/)) {
            return "bracket";
        }

        // Comma separator
        if (stream.match(/^[,，]/)) {
            return "punctuation";
        }

        // Numbers (with optional sign)
        if (stream.match(/^[+-]?\d+/)) {
            return "number";
        }

        // Words (instructions, registers, labels)
        const word = stream.match(/^[a-z_][a-z0-9_]*/i);
        if (Array.isArray(word)) {
            const w = word[0].toLowerCase();

            if (instructions.has(w)) {
                return "keyword";
            }

            if (registers.has(w)) {
                return "variableName";
            }

            // Label reference (used with jmp, call, etc.)
            return "labelName";
        }

        // Sign operators in memory offset
        if (stream.match(/^[+-]/)) {
            return "operator";
        }

        // Skip unknown character
        stream.next();
        return null;
    },

    languageData: {
        commentTokens: { line: ";" }
    }
});

// Export wrapped in LanguageSupport for use with CodeMirror's lang prop
export const toyAsm = new LanguageSupport(toyAsmLanguage);
