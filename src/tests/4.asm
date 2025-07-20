    jmp main

f1:
    dump 512, 32
    mov ax, [sp-2] // 参数
    add ax, 1
    cmp ax, 10
    jg stop_recursive

    print "working on "
    print ax
    print " sp="
    println sp

    push ax
    call f1
    pop
stop_recursive:
    ret

main:
    push 0
    call f1
    pop
