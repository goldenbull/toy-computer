    jmp main

fib:
    // enter fib(), setup stack
    push bp
    mov bp, sp
    add sp, 2 // reserve space for a and b

    // now the stack layout:
    // [bp-4] n
    // [bp-3] ret
    // [bp-2] return ip
    // [bp-1] original bp
    // [bp+0] a
    // [bp+1] b
    // sp = bp+2

    // if(n<=2)
    mov ax, [bp-4]
    cmp ax, 2
	jg	fib_recursive

    // return 1;
	mov	[bp-3], 1
	jmp	fib_return

fib_recursive:

    // a = fib(n-1)
    mov ax, [bp-4]
    sub ax, 1       // get n-1
    push ax         // push parameter
    add sp, 1       // reserve space for return value
    call fib
    pop dx          // get return value
    sub sp, 1       // discard parameter
    mov [bp], dx    // return value --> a

    // b = fib(n-2)
    mov ax, [bp-4]
    sub ax, 2
    push ax
    add sp, 1
    call fib
    pop dx
    sub sp, 1
    mov [bp+1], dx

    // return a+b
    mov ax, [bp]
    add ax, [bp+1]
    mov [bp-3], ax

fib_return:
    // debug output
    print [bp-3]
    print " "

    // restore stack pointers before exit fib()
	mov	sp, bp
	pop	bp
	ret

main:
    // call fib(20)
    push 20
    add sp, 1
    call fib
    pop dx
    sub sp, 1
    println
    print "result = "
    println dx
