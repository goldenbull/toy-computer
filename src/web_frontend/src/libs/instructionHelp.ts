// Shared by diagnostics and editor completion; matches toy_asm.g4.
export const instructionHelp: Record<string, string> = {
    mov: 'mov 目标, 来源；目标为寄存器或内存，来源为整数、寄存器或内存；不能同时为内存。',
    add: 'add 目标, 加数；目标为寄存器或内存；不能同时为内存。',
    sub: 'sub 目标, 减数；目标为寄存器或内存；不能同时为内存。',
    cmp: 'cmp 左值, 右值；左值为寄存器或内存；不能同时为内存。',
    mul: 'mul 乘数；只接收一个整数、寄存器或内存操作数，结果写入 ax。',
    div: 'div 除数；只接收一个整数、寄存器或内存操作数，商写入 ax，余数写入 dx。',
    ...Object.fromEntries(['jmp', 'je', 'jne', 'jg', 'jge', 'jl', 'jle', 'call'].map(name => [name, `${name} 标签名；目标必须是已定义的标签（区分大小写）。`])),
    ret: 'ret；不接收操作数，从栈中取出返回地址。',
    push: 'push 值；值为整数、寄存器或内存。',
    pop: 'pop [目标]；目标可省略，否则必须为寄存器或内存。',
    input: 'input 目标；目标必须为寄存器或内存。',
    rand: 'rand 目标；目标必须为寄存器或内存。',
    print: 'print 值；值为整数、寄存器、内存或双引号字符串。',
    println: 'println [值]；可省略值，只输出换行。',
    break: 'break；不接收操作数，暂停执行。',
    halt: 'halt；不接收操作数，结束执行。'
};
