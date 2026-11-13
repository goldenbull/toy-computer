import type {CompletionContext} from '@codemirror/autocomplete';
import {instructionHelp} from './instructionHelp';
import { StreamLanguage, LanguageSupport } from "@codemirror/language";

// Token types for toy assembly language
const instructions = new Set([
    "mov", "add", "sub", "mul", "div", "cmp",
    "jmp", "je", "jne", "jg", "jge", "jl", "jle",
    "call", "ret", "push", "pop",
    "input", "print", "println", "rand",
    "break", "halt"
]);

const registers = new Set([
    "ax", "bx", "cx", "dx", "bp", "sp"
]);

// Stream parser for toy assembly
export const toyAsmForCodemirror = StreamLanguage.define({
    name: "toyasm",

    token(stream) {
        // Skip whitespace but track if we were at line start before whitespace
        const atLineStart = /^\s*$/.test(stream.string.slice(0, stream.pos));
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
export function completeAssembly(context: CompletionContext) {
    const line = context.state.doc.lineAt(context.pos);
    const prefix = line.text.slice(0, context.pos - line.from);
    // Do not complete in strings or comments, including escaped quotation marks.
    if (/^(?:[^";；]|"(?:[^"\\]|\\.)*")*[;；]/.test(prefix) ||
        /"(?:[^"\\]|\\.)*$/.test(prefix.replace(/"(?:[^"\\]|\\.)*"/g, ''))) return null;
    const word = context.matchBefore(/[a-z_][a-z0-9_]*/i);
    if (!word && !context.explicit) return null;
    const before = prefix.slice(0, word ? word.from - line.from : prefix.length);
    const instructionPosition = /^\s*(?:[a-z_][a-z0-9_]*\s*[:：]\s*)?$/i.test(before);
    const labels = [...context.state.doc.toString().matchAll(/^\s*([a-z_][a-z0-9_]*)\s*[:：]/gim)].map(match => match[1]);
    const options = instructionPosition
        ? Object.entries(instructionHelp).map(([label, info]) => ({label, type: 'keyword', info}))
        : /\b(?:j(?:mp|e|ne|g|ge|l|le)|call)\s+$/i.test(before)
            ? [...new Set(labels)].map(label => ({label, type: 'constant'}))
            : ['ax', 'bx', 'cx', 'dx', 'bp', 'sp'].map(label => ({label, type: 'variable'}));
    return {from: word?.from ?? context.pos, options, validFor: /^[a-z_][a-z0-9_]*$/i};
}

export const toyAsm = new LanguageSupport(toyAsmForCodemirror, [
    toyAsmForCodemirror.data.of({autocomplete: completeAssembly})
]);
