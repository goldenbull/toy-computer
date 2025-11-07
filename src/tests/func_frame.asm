; show function call/ret stack frame

    push 100         ; 第一个参数
    push 200         ; 第二个参数
    sub sp, 1       ; 为返回值预留位置
    call _f1        ; ip 自动入栈，并跳转到 _f1 位置
    mov ax, [sp+1]  ; 获得返回值，存入ax中
    add sp, 3       ; 函数调用完毕，参数和返回值不能再继续占据内存

    print ax

    halt


_f1:
    ; 创建新的frame
    push bp
    mov bp, sp

    ; 参数的访问
    mov ax, [bp+4] ; 第一个参数
    mov bx, [bp+5] ; 第二个参数

    ; 开始函数计算，其实可以不用临时变量，此处只为演示临时变量的用法
    mov [bp], ax
    mov [bp-1], bx
    mov ax, 0
    add ax, [bp]
    add ax, [bp-1]
    add ax, 1

    ; 返回值
    mov [bp+3], ax

    ; 退回之前的frame
    mov sp, bp
    pop bp

    ; ip出栈，函数返回
    ret