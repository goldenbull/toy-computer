addr1:
    // comment here
    mov ax, 0
    push ax
    jmp main
addr2:
addr3:
    dump 512, 20
    ret

main:
    // comment
    // more comment
main2:
    // comment
    call addr2
    call addr3


