grammar toy_asm;

program
    : (Comment|opLabel|op)* (Comment|op) EOF
    ;

opLabel
    : Label ':'
    ;

op
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
    | input
    | print
    | rand
    | dump
    | pause
    | halt
    | nop
    ;

num
    : '+'? INT
    | '-' INT
    ;

reg
    : 'ax' | 'bx' | 'cx' | 'dx' | 'bp' | 'sp'
    ;

offset
    : ('+'|'-') INT
    ;

mem
    : '[' reg offset? ']'
    ;

move
    : 'mov' reg ',' num
    | 'mov' reg ',' reg
    | 'mov' reg ',' mem
    | 'mov' mem ',' num
    | 'mov' mem ',' reg
    ;

add
    : 'add' reg ',' num
    | 'add' reg ',' reg
    | 'add' reg ',' mem
    ;

sub
    : 'sub' reg ',' num
    | 'sub' reg ',' reg
    | 'sub' reg ',' mem
    ;

mul
    : 'mul' num
    | 'mul' reg
    | 'mul' mem
    ;

div
    : 'div' num
    | 'div' reg
    | 'div' mem
    ;

cmp
    : 'cmp' reg ',' num
    | 'cmp' reg ',' reg
    | 'cmp' reg ',' mem
    ;

jump
    : 'jmp' Label
    | 'je' Label
    | 'jne' Label
    | 'jg' Label
    | 'jge' Label
    | 'jl' Label
    | 'jle' Label
    ;

call
    : 'call' Label
    ;

ret
    : 'ret'
    ;

push
    : 'push' num
    | 'push' reg
    | 'pushf'
    ;

pop
    : 'pop'
    | 'pop' reg
    | 'popf'
    ;

input
    : 'input' reg
    | 'input' mem
    ;

str
    : STR
    ;

print
    : 'print' num
    | 'print' reg
    | 'print' mem
    | 'print' str
    | 'println' num
    | 'println' reg
    | 'println' mem
    | 'println' str
    | 'println'
    ;

rand
    : 'rand' reg
    | 'rand' mem
    ;

dump
    : 'dump'
    | 'dump' reg ',' INT
    | 'dump' num ',' INT
    ;

pause
    : 'pause'
    ;

halt
    : 'halt'
    ;

nop
    : 'nop'
    ;

Comment : ';' ~[\n]* '\n' ;
INT : [0-9]+ ;
Label : ([a-z]|'_') ([a-z0-9]|'_')* ;
STR : '"' ( EscapeSequence | ~('\\'|'"') )* '"' ;
fragment EscapeSequence  :  '\\' ('b'|'t'|'n'|'f'|'r'|'"'|'\''|'\\') ;
WS : [ \t\r\n]+ -> skip;
