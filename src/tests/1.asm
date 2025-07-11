jmp _main
_main:
mov ax, 0
loop1:
add ax, 1
cmp ax, 10
// cmd
 jg _finish
 print ax
jmp loop1
_finish:
dump