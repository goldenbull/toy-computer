    jmp main

fib:
    push bp
    mov bp, sp

    add sp,3
    // [bp+0] n
    // [bp+1] a
    // [bp+2] b

    mov [bp], ax
    cmp ax,2
    jle return1

    mov ax,[bp]
    sub ax,1
    call fib
    mov [bp+1], ax

    mov ax,[bp]
    sub ax,2
    call fib
    mov [bp+2], ax

    print [bp]
    print " "
    print [bp+1]
    print " "
    println [bp+2]

    mov ax, [bp+1]
    add ax, [bp+2]
    jmp fib_ret

return1:
    mov ax,1

fib_ret:
    mov [bp],12345
    mov [bp+1],23456
    mov [bp+2],34567
    mov sp,bp
    pop bp
    ret

main:

    mov ax,6
    call fib
    print ax
