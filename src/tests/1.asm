start:   mov ax, 123
start2: mov ax, +123
mov ax, -123
mov ax, 0
mov ax, -0
mov cx, [ax]
mov [bx+66], 0
mov [dx-77], 0
repeat1:
add ax, 456
print ax
mov bx, ax
repeat2: add bx, 1
print bx
jmp repeat2
push ax
mov ax, bp
sub bp, 4
dump bp, 10
pause
pop ax