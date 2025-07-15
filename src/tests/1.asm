    dump
    println "hello \t world\n==new line=="
    pause
    jmp _main

f1: nop
    //dump dx, 10
    //pause
    push bp
    mov bp, sp

    mov cx, [bp-3]
    print cx

    dump dx, 10
    pause

    pop bp
    ret


_main:
    mov ax, 0
    mov dx, sp
loop1:
    add ax, 1
    cmp ax, 10
    jg _finish

    // do work here
    //dump dx, 10
    //pause
    push ax
    //dump dx, 10
    //pause
    call f1
    pop ax

    jmp loop1
_finish:
    nop