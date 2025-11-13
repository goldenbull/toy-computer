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

    ; quicksort(0, N - 1);
    mov ax, [bp]
    sub ax, 1
    push ax
    push 0
    call quicksort
    add sp, 2

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

; ------- void quicksort(low, high) ----------
quicksort:
    push bp
    mov bp, sp

    sub sp, 1   ; 为pivotIndex预留空间
    ; [bp+4] high
    ; [bp+3] low
    ; [bp+2] ret ip
    ; [bp+1] saved bp
    ; [bp+0] pivotIndex
    ; []    <-- sp

    ; if (low >= high)
    ;     return;
    mov ax, [bp+3]
    cmp ax, [bp+4]
    jge quicksort_ret

    ; int pivotIndex = partition(low, high);
    mov ax, [bp+4]
    push ax
    mov ax, [bp+3]
    push ax
    push 0
    call partition
    pop ax
    mov [bp], ax
    add sp, 2

    ; quicksort(low, pivotIndex - 1);
    mov ax, [bp]
    sub ax, 1
    push ax
    mov ax, [bp+3]
    push ax
    call quicksort
    add sp, 2

    ; quicksort(pivotIndex + 1, high);
    mov ax, [bp+4]
    push ax
    mov ax, [bp]
    add ax, 1
    push ax
    call quicksort
    add sp, 2

quicksort_ret:
    ; return
    mov sp, bp
    pop bp
    ret

; ---------- int partition(low, high) ---------
partition:
    push bp
    mov bp, sp

    sub sp, 4
    ; [bp+5] high
    ; [bp+4] low
    ; [bp+3] return value
    ; [bp+2] ret ip
    ; [bp+1] saved bp
    ; [bp+0] pivot
    ; [bp-1] tmp
    ; [bp-2] i
    ; [bp-3] j
    ; []    <-- sp

    ; int pivot = data[high];
    mov ax, [bp+5]
    mov bx, [ax]
    mov [bp], bx

    ; int i = low - 1;
    mov ax, [bp+4]
    sub ax, 1
    mov [bp-2], ax

    ; int j = low;
    mov ax, [bp+4]
    mov [bp-3], ax

_swap_loop:
    ; if (j >= high)
    ;   goto swap_loop_finish;
    mov ax, [bp-3]
    cmp ax, [bp+5]
    jge _swap_loop_finish

    ; if (data[j] > pivot)
    ;   goto swap_loop_next;
    mov cx, [bp-3]
    mov ax, [cx]
    cmp ax, [bp]
    jg _swap_loop_next

    ;        i++;
    mov ax, [bp-2]
    add ax, 1
    mov [bp-2], ax

    ;        tmp = data[i];
    mov bx, [ax]
    mov [bp-1], bx

    ;        data[i] = data[j];
    mov ax, [bp-3]
    mov bx, [ax]
    mov ax, [bp-2]
    mov [ax], bx

    ;        data[j] = tmp;
    mov bx, [bp-1]
    mov ax, [bp-3]
    mov [ax], bx

_swap_loop_next:
    ; j++
    mov ax, [bp-3]
    add ax, 1
    mov [bp-3], ax
    jmp _swap_loop

_swap_loop_finish:

    ; tmp = data[i + 1];
    mov ax, [bp-2]
    mov bx, [ax+1]
    mov [bp-1], bx

    ; data[i + 1] = data[high];
    mov ax, [bp+5]
    mov bx, [ax]
    mov ax, [bp-2]
    mov [ax+1], bx

    ; data[high] = tmp;
    mov bx, [bp-1]
    mov ax, [bp+5]
    mov [ax], bx

    ; return i + 1;
    mov ax, [bp-2]
    add ax, 1
    mov [bp+3], ax

    mov sp, bp
    pop bp
    ret

