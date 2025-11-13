; 观察函数调用时使用栈的逻辑
; call 和 ret 指令只涉及 ip 寄存器的进出栈
; 参数、返回值、函数内的临时变量（即C语言的局部变量）的使用，需要遵循一定的规范
; 此处以一个简单的两层函数调用为例，通过step模式观察栈的变化情况
; f1(x,y) = f2(x,y) + f3(x,y)
; f2(x,y) = x+y+1
; f3(x,y) = x*y*2
; 按照C语言的约定，参数按照从后往前的顺序，即先y后x的顺序入栈
; 出于演示目的，代码中会轮流使用不同的寄存器进行计算

_start:
    ; 输入x，存入内存
    println "input x"
    input ax
    mov dx, 0
    mov [dx], ax

    ; 输入y，存入内存
    println "input y"
    input ax
    mov [dx+1], ax

    ; 参数入栈
    mov ax, [dx+1]
    push ax
    mov ax, [dx]
    push ax

    ; 为返回值预留位置
    sub sp, 1

    ; 调用函数
    call f1

    ; 获得返回值
    pop dx
    print "f1(x,y)="
    println dx

    halt ; 停机，否则后续指令会被继续执行

f1:
    ; 栈的使用规范，用bp寄存器寻址
    push bp
    mov bp, sp

    ; 预留一个内存单元给临时变量
    sub sp, 1

    ; 调用f2
    mov ax, [bp+5] ; 获取参数y并入栈
    push ax
    mov ax, [bp+4] ; 获取参数x并入栈
    push ax
    sub sp, 1      ; 为f2的返回值预留空间
    call f2
    pop cx         ; 获得函数结果
    add sp, 2      ; 释放两个参数占据的栈空间
    mov [bp], cx   ; 存入预留的内存空间

    ; 调用f3
    mov ax, [bp+5] ; 获取参数y并入栈
    push ax
    mov ax, [bp+4] ; 获取参数x并入栈
    push ax
    sub sp, 1      ; 为f3的返回值预留空间
    call f3
    pop cx         ; 获得函数结果
    add sp, 2      ; 释放两个参数占据的栈空间
    add cx, [bp]   ; f1 = f2 + f3
    mov [bp+3], cx ; 设置f1的函数返回值

    ; 准备返回，恢复进入函数之前的bp寄存器
	mov	sp, bp
    pop bp
    ret

f2:
    push bp
    mov bp, sp

    mov cx, [bp+5] ; 获取参数y
    mov dx, [bp+4] ; 获取参数x
    add cx, dx     ; x + y + 1
    add cx, 1
    mov [bp+3], cx ; 设置f2的函数返回值

	mov	sp, bp
    pop  bp
    ret

f3:
    push bp
    mov bp, sp

    mov ax, [bp+5] ; 获取参数y
    mov dx, [bp+4] ; 获取参数x
    mul dx         ; x * y * 2
    mul 2
    mov [bp+3], ax ; 设置f2的函数返回值

	mov	sp, bp
    pop  bp
    ret
