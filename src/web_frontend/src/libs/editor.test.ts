import {test} from 'node:test';
import assert from 'node:assert/strict';
import {EditorState} from '@codemirror/state';
import {CompletionContext} from '@codemirror/autocomplete';
import {completeAssembly} from './toyAsmForCodemirror';
function complete(doc: string) {
    return completeAssembly(new CompletionContext(EditorState.create({doc}), doc.length, true));
}
test('context-aware instruction, register and forward label completion', () => {
    assert.ok(complete('mo')?.options.some(option => option.label === 'mov'));
    assert.ok(complete('loop: mo')?.options.some(option => option.label === 'mov'));
    assert.ok(complete('mov a')?.options.some(option => option.label === 'ax'));
    assert.deepEqual(complete('loop: halt\njmp lo')?.options.map(option => option.label), ['loop']);
});
test('no completions inside strings and comments', () => {
    for (const doc of ['; mov', '；mov', 'print "mo', 'print "a\\"mo', 'print "hello" ; mo']) {
        assert.equal(complete(doc), null, doc);
    }
    assert.ok(complete('print "hello"'));
});
