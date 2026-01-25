; 输入一个数，如果是正整数，则输出从1加到这个数的结果

start:
    println "输入正整数N"
    input ax
    cmp ax, 0
    jle _error  ; 不是正整数时，报错，结束程序

    ; 使用[0]记录N
    mov bp, 0
    mov [bp], ax

    ; cx 做计数器， ax 保存累加结果
    mov cx, 0
    mov ax, 0

_loop:
    ; 开始循环累加
    add cx, 1
    add ax, cx

    ; 判断是否已经加到N了
    cmp cx, [bp]
    jge _finish
    jmp _loop

_finish:
    print "sum from 1 to "
    print [bp]
    print " = "
    println ax

    halt ; 结束程序，如果没有这条指令，后面的两条指令也会被执行

_error:
    println "输入错误"
    halt