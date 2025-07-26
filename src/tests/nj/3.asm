    mov ax,0
    mov bx,1
repeat:
    add ax,bx
    add bx,1
    cmp bx,10000
    jle repeat
    println ax