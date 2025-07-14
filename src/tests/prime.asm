    jmp _main

_f_is_prime:
    push bp
    mov bp, sp
    pusha

    // check if ax is prime
    mov ax, [bp-3]

    // check <2, ==2
    cmp ax, 2
    jl _not_prime
    je _is_prime
    div 2
    cmp dx, 0
    je _not_prime

    // check 3 to ax-1
    mov cx, 3
_f_is_prime_loop1:
    mov ax, [bp-3]
    cmp cx, ax
    jge _is_prime
    div cx
    cmp dx, 0
    je _not_prime
    add cx, 1
    jmp _f_is_prime_loop1
_not_prime:
    popa
    pop bp
    mov ax, 0
    ret
_is_prime:
    popa
    pop bp
    mov ax, 1
    ret

_main:
    mov ax, -10
_main_loop1:
    push ax
    call _f_is_prime
    mov bx, ax
    pop ax
    cmp bx, 1
    jne _skip
    print ax
_skip:
    add ax, 1
    cmp ax, 100
    je _finish
    jmp _main_loop1
_finish:
    nop
