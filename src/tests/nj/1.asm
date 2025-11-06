
    mov cx,0

loop:
    mov ax,cx
    jmp function_7
back_to_main:
    print cx
    print ":"
    println ax

    add cx,1
    cmp cx,20
    jl loop

    input ax
    jmp function_7
back_to_main2:

    println "bye!"
    halt


function_7:
    div 10
    cmp dx,7
    je _end_with_7
    jne _not_end_with_7

_end_with_7:
    mov ax,1
    jmp _end_func

_not_end_with_7:
    mov ax,0
    jmp _end_func

_end_func:
    jmp back_to_main