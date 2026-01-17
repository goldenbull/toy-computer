import {Compiler} from './Compiler';

const compiler = new Compiler();

const source = `
; test program
mov ax, 10 ;:err1
  loop:
  loop:
    add ax, 1
    cmp ax, 20
    jl loop
halt
`;

const result = compiler.compile(source);
console.log('Success:', result.success);
console.log('Operations:', JSON.stringify(result.operations, null, 2));
console.log('Labels:', result.labels);
console.log('Errors:', result.firstError?.toString());
