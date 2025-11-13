_main:
    mov ax, 0
    mov [bp], ax        ; n保存在[bp]中，从0开始
_main_loop1:
    mov ax, [bp]
    push ax             ; 检查当前的n是不是质数
    call _f_is_prime
    add sp, 1           ; 释放参数的栈空间
    cmp ax, 1           ; 返回值为1表示是质数
    jne _next
    print [bp]          ; 输出质数
    print " "
_next:
    mov ax, [bp]        ; n <= n+1
    add ax, 1
    mov [bp], ax
    cmp ax, 1000        ; n到1000为止
    je _finish
    jmp _main_loop1
_finish:
    println
    print "bye!"
    println
    halt

_f_is_prime:
    push bp
    mov bp, sp

    ; 参数在[bp+3]中
    ; 质数判断的笨办法是从2一直整除到n-1
    ; 此处使用一个简单的加速算法，只判断奇数，除数也只需要尝试奇数，且到n的平方根截止

    ; 依次处理特殊情况： <2, ==2, ==3, 整除2
    mov ax, [bp+3]
    cmp ax, 2
    jl _not_prime       ; <2 不是质数
    je _is_prime        ; ==2 是质数
    cmp ax, 3
    je _is_prime        ; ==3 是质数
    div 2
    cmp dx, 0
    je _not_prime       ; >2 且能整除2，不是质数

    ; 除数从3开始，逐个尝试，直到能整除，或者商小于等于除数为止
    mov cx, 3
_f_is_prime_loop1:
    mov ax, [bp+3]
    div cx
    cmp dx, 0
    je _not_prime       ; 余数为0，能整除，不是质数
    cmp ax, cx
    jle _is_prime       ; 商小于等于除数仍然没有能整除，是质数
    add cx, 2           ; 除数+2，继续尝试
    jmp _f_is_prime_loop1

_not_prime:
    mov ax, 0           ; 使用ax保存返回值
    jmp _f_is_prime_ret

_is_prime:
    mov ax, 1
    jmp _f_is_prime_ret

_f_is_prime_ret:
	mov	sp, bp
    pop bp
    ret
