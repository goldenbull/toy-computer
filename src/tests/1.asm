start:
rand ax
print ax
mov ax, 100
rand [ax]
print [ax]
print [bx-22]
add ax, [bx]
mov ax, 100
div 24
dump
mov ax, 100
mov cx, 0
mov [cx+1], 0
div [cx+1]
dump
pause
mov ax, 900
mov bx, [ax+100]
dump ax, 100
start2: mov ax, +123
mov ax, -123
mov ax, 0
mov ax, -0
mov cx, [ax]
dump ax, 0
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
//pause
pop ax