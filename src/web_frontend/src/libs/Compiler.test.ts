import {test} from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync, readdirSync} from 'node:fs';
import {Compiler} from './Compiler';

const compiler = new Compiler();
test('reserved words cannot be labels; highlight the name rather than the colon', () => {
    for (const source of ['jmp:', '  JMP： halt', '\tax: mov bx, 1', 'println:']) {
        const result = compiler.compile(source);
        const name = source.trim().split(/[:：]/)[0];
        assert.equal(result.success, false);
        assert.equal(result.errors.length, 1);
        assert.match(result.firstError!.message, new RegExp(`关键字 ${name} 不能用作标签`));
        assert.equal(result.firstError!.column, source.indexOf(name));
        assert.equal(result.firstError!.length, name.length);
    }
    assert.equal(compiler.compile('jmp_loop: halt\njmp jmp_loop\nprint "jmp:" ; ax:').success, true);
    assert.equal(compiler.compile('; jmp:').success, true);
});
test('all shipped demo programs compile', () => {
    const dir = new URL('../../static/', import.meta.url);
    for (const file of readdirSync(dir).filter(file => file.endsWith('.asm'))) {
        const result = compiler.compile(readFileSync(new URL(file, dir), 'utf8'));
        assert.equal(result.success, true, `${file}: ${result.firstError}`);
    }
});
test('collects independent errors and never returns executable partial code', () => {
    const result = compiler.compile('mov ax 1\ninput 2\njmp missing\ntrailing:');
    assert.deepEqual(result.errors.map(error => error.lineNum), [0, 1, 2, 3]);
    assert.deepEqual(result.operations, []);
    assert.equal(result.firstError, result.errors[0]);
    assert.match(result.errors[0].message, /逗号/);
    assert.match(result.errors[1].message, /用法/);
    assert.match(result.errors[2].message, /没有定义标签/);
});
test('prototype property names are ordinary labels, not inherited definitions', () => {
    assert.equal(compiler.compile('constructor: halt\njmp constructor\n__proto__: halt\ncall __proto__').success, true);
    assert.equal(compiler.compile('jmp constructor').success, false);
});
test('forward labels, full-width punctuation, CRLF and uppercase instructions', () => {
    const result = compiler.compile('JMP End\r\nMOV AX，+1；说明\r\nEnd：HALT');
    assert.equal(result.success, true);
    assert.equal(result.operations[0].targetAddr, 2);
    assert.equal(result.operations[2].sourceLine, 2);
});
test('duplicate labels refer to the original definition and accurate column', () => {
    const result = compiler.compile('same: halt\n  same: halt\n same: halt');
    assert.equal(result.errors.length, 2);
    assert.equal(result.errors[0].column, 2);
    for (const error of result.errors) assert.match(error.message, /首次出现在第 1 行/);
});
test('numeric safety includes literals and memory offsets, but not strings or comments', () => {
    for (const code of ['mov ax, 9007199254740992', 'mov ax, [bp-9007199254740992]']) {
        assert.match(compiler.compile(code).firstError!.message, /安全范围/);
    }
    assert.equal(compiler.compile('mov ax, -9007199254740991\nprint "9007199254740992" ; 999999999999999999').success, true);
});
test('malformed input has bounded locations and useful diagnostics', () => {
    for (const code of ['mov ax,', 'mov ax, [bp+]', 'print "abc', 'mov ip, 1', 'mov [ax], [bx]', 'halt 1', '???', 'constructor']) {
        const result = compiler.compile(code);
        assert.equal(result.success, false, code);
        assert.ok(result.firstError!.column >= 0 && result.firstError!.column <= code.length);
        assert.match(result.firstError!.toString(), /第 1 行，第/);
        assert.doesNotMatch(result.firstError!.message, /function Object/);
    }
});
