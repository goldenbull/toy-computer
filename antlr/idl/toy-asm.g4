grammar toy_asm;

program
    : (comment|oneLineCode)+
    ;

comment
    : (Comment)*
    ;

oneLineCode
    : (Addr ':')? oneOp
    ;

oneOp
    : move
    | add
    | sub
    | mul
    | div
    | cmp
    | jump
    | call
    | ret
    | push
    | pop
    | pushf
    | popf
    | pusha
    | popa
    | input
    | print
    | rand
    ;

mem
    : '[' Reg ']'
    | '[' Reg offset ']'
    ;

offset
    : ('+'|'-')INT
    ;

num
    : '+'? INT
    | '-' INT
    ;

move
    : 'mov' Reg ',' num
    | 'mov' Reg ',' Reg
    | 'mov' Reg ',' mem
    | 'mov' mem ',' num
    | 'mov' mem ',' Reg
    ;

add
    : 'add' Reg ',' num
    | 'add' Reg ',' Reg
    | 'add' Reg ',' mem
    ;

sub
    : 'sub' Reg ',' num
    | 'sub' Reg ',' Reg
    | 'sub' Reg ',' mem
    ;

mul
    : 'mul' num
    | 'mul' Reg
    | 'mul' mem
    ;

div
    : 'div' num
    | 'div' Reg
    | 'div' mem
    ;

cmp
    : 'cmp' Reg ',' num
    | 'cmp' Reg ',' Reg
    | 'cmp' Reg ',' mem
    ;

jump
    : 'jmp' Addr
    | 'je' Addr
    | 'jne' Addr
    | 'jg' Addr
    | 'jge' Addr
    | 'jl' Addr
    | 'jle' Addr
    ;

Addr
    : [a-z] ([a-z0-9]|'_')*

call
    : 'call' Addr
    ;

ret
    : 'ret'
    ;

push
    : 'push' num
    | 'push' Reg
    ;

pop
    : 'pop' Reg
    ;

pushf
    : 'pushf'
    ;

popf
    : 'popf'
    ;

pusha
    : 'pusha'
    ;

popa
    : 'popa'
    ;

input
    : 'input' Reg
    | 'input' mem
    ;

print
    ：'print' num
    | 'print' Reg
    | 'print' mem
    ;

rand
    : 'rand' Reg
    | 'rand' mem
    ;

Comment
    : '//' ~[\n]* '\n'
    ;

Reg
    : 'ax' | 'bx' | 'cx' | 'dx' | 'bp' | 'sp'
    ;

INT
    : [0-9]+
    ;

