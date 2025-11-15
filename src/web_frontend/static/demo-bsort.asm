; 通过重复地遍历待排序的序列，比较相邻的元素，如果它们的排序顺序错误就交换它们的位置。
; 最大的元素会像气泡一样逐渐“浮”到序列的末尾，因此得名。

main:
    ; int N = 100;
    push 100

    ; generate random numbers
    mov cx, 0
_gen_rand_loop:
    rand [cx]
    add cx, 1
    cmp cx, [bp]
    jne _gen_rand_loop

    ; bubble
    ; cx: index
    ; [bp]: N
    ; [bp-1]: swap counter
_bubble_loop_init:
    ; 计数器归零，从头开始循环
    mov [bp-1], 0
    mov cx, 0
_bubble_loop:
    ; cx最大值不能超过N-2
    mov ax, [bp]
    sub ax, 2
    cmp cx, ax
    jg _bubble_loop_end

    ; 检查相邻的数
    mov ax, [cx]
    mov bx, [cx+1]
    cmp ax, bx
    jle _no_swap

    ; 执行交换
    mov [cx], bx
    mov [cx+1], ax
    ; 记录交换次数+1
    mov ax, [bp-1]
    add ax, 1
    mov [bp-1], ax

_no_swap:
    ; 继续检查下一对相邻的数
    add cx, 1
    jmp _bubble_loop

_bubble_loop_end:
    ; 检查本次循环交换了几个数，如果没有交换，说明排序结束了
    mov dx, [bp-1]
    cmp dx, 0
    jne _bubble_loop_init

    ; output result
    mov cx, 0
_print_loop:
    print [cx]
    print " "
    add cx, 1
    cmp cx, [bp]
    jne _print_loop

    println
    println "=== finished ==="
    halt
