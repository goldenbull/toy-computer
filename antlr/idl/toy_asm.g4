grammar toy_asm;

options {
    caseInsensitive=true;
}

// Source code is pre-processed before compiling:
// 1. Split into lines
// 2. Skip comments and blank lines
// 3. Extract labels (lines ending with ':')
// 4. Parse each remaining line as a single instruction

line
    : (label|label_and_op|op) EOF
    ;

label
    : Label ':'
    ;

label_and_op
    : label ':' op
    ;

op
    : mov
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
    | halt
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

mov
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

halt
    : 'halt'
    ;


INT : [0-9]+ ;
Label : ([a-z]|'_') ([a-z0-9]|'_')* ;
STR : '"' ( EscapeSequence | ~('\\'|'"') )* '"' ;
fragment EscapeSequence :  '\\' ('b'|'t'|'n'|'f'|'r'|'"'|'\''|'\\') ;
WS : [ \t\r]+ -> skip;
