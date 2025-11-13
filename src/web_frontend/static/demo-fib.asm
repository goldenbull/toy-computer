; 斐波那契数列的计算本身是很简单的过程，使用一个简单循环即可
; 但同时，斐波那契数列的计算过程可以很好的展示递归函数的思想
; 在数学上，斐波那契数列就是通过递归的形式定义的：
;   f(n) = f(n-1) + f(n-2), f(1)=f(2)=1
; 这个定义方式很鲜明的展示了递归函数的两个核心点
;   1. 自身调用自身，即递归调用（recursive）
;   2. 递归不是一个无限过程，有终止条件，即n=1或n=2
; 实际上，fib函数的C语言实现是非常简单而清晰的：
; int fib(n)
; {
;   if (n<=2)
;     return 1;
;   a = f(n-1);
;   b = f(n-2);
;   return a+b;
; }
;
; 以下将这个C的递归函数逐行翻译成汇编代码，重点在于观察栈的使用情况


    jmp _start    ; 我们把函数实现写在前面，把主程序放到后面

fib:
    push bp
    mov bp, sp

    sub sp, 2 ; 为临时变量a和b预留空间

    ; 栈的布局
    ;   [bp+4] n
    ;   [bp+3] ret
    ;   [bp+2] return ip
    ;   [bp+1] original bp
    ;   [bp+0] a
    ;   [bp-1] b
    ;   []     <-- sp

    ;
    ; if (n<=2)
    ;
    mov ax, [bp+4]
    cmp ax, 2
    jg fib_recursive

    ;
    ;   return 1;
    ;
    mov [bp+3], 1
    jmp fib_return

fib_recursive:

    ;
    ; a = fib(n-1)
    ;
    mov ax, [bp+4]
    sub ax, 1       ; get n-1
    push ax         ; push parameter
    sub sp, 1       ; reserve space for return value
    call fib
    pop dx          ; get return value
    add sp, 1       ; discard parameter
    mov [bp], dx    ; return value --> a

    ;
    ; b = fib(n-2)
    ;
    mov ax, [bp+4]
    sub ax, 2
    push ax
    sub sp, 1
    call fib
    pop dx
    add sp, 1
    mov [bp-1], dx

    ;
    ; return a+b
    ;
    mov ax, [bp]
    add ax, [bp-1]
    mov [bp+3], ax

fib_return:
    ; 输出中间的计算过程
    print [bp+3]
    print " "

    ; 恢复之前的栈指针，返回
    mov sp, bp
    pop bp
    ret

_start:
    ; call fib(20)
    mov ax, 20

    push ax
    sub sp, 1
    call fib
    pop dx
    pop ax

    println
    print "fib("
    print ax
    print ")="
    println dx
