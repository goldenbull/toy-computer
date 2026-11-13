import {test} from 'node:test';
import assert from 'node:assert/strict';
import {Compiler} from './Compiler';
import {ComputerStatus, ExecStatus} from './ComputerStatus.svelte';
import {WebExecutor} from './WebExecutor';

// Exercise the execution model without constructing Svelte reactive fields.
function machine(source: string) {
    const result = new Compiler().compile(source);
    assert.equal(result.success, true);
    const status: ComputerStatus = Object.create(ComputerStatus.prototype);
    Object.assign(status, {
        operations: result.operations, registers: {ax: 0, bx: 0, cx: 0, dx: 0, ip: 0, bp: 1023, sp: 1023, flg: 0},
        memory: Array(1024).fill(0), memoryTypes: {}, output: '', execStatus: ExecStatus.Ready,
        inputTarget: null, previousExecStatus: null
    });
    return {status, executor: new WebExecutor(status)};
}
test('division error reports original source line, instruction and reason', () => {
    const {status, executor} = machine('; comment\nmov ax, 4\ndiv 0');
    executor.runOneStep();
    assert.equal(executor.runOneStep(), false);
    assert.equal(status.execStatus, ExecStatus.Halted);
    assert.match(status.output, /源码第 3 行/);
    assert.match(status.output, /div 0/);
    assert.match(status.output, /ax = 4/);
});
test('input memory failure uses the same source-aware runtime diagnostic', () => {
    const {status, executor} = machine('mov bx, 1024\ninput [bx]');
    executor.runOneStep();
    executor.runOneStep();
    assert.throws(() => executor.provideInput('3'), /有效范围/);
    assert.equal(status.execStatus, ExecStatus.Halted);
    assert.match(status.output, /源码第 2 行/);
    assert.match(status.output, /1024/);
});
test('empty stack reports how to repair call/return pairing', () => {
    const {status, executor} = machine('ret');
    assert.equal(executor.runOneStep(), false);
    assert.match(status.output, /call\/ret/);
});
