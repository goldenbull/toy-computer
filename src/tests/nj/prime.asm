    // ax=N
    input ax

    // save to memory
    mov cx,0
    mov [cx],ax

    // check if <=1
    cmp ax,1
    jle fail
    
    // check if ==2 or ==3
    cmp ax,2
    je is_prime
    cmp ax,3
    je is_prime

    // check if %2==0
    div 2
    cmp dx,0
    je fail

    // loop from 3
    mov bx,3
 repeat:
    // N%bx
    mov cx,0
    mov ax,[cx]
    div bx
    // N%bx==0, fail
    cmp dx,0
    je fail
    // bx = bx+2
    add bx,2
    // check if bx*bx>=N
    mov ax,bx
    mul bx
    mov cx,0
    cmp ax,[cx]
    jl repeat
    jmp is_prime

fail:
    mov cx,0
    mov [cx+1],ax
    mov ax,[cx]
    print ax
    print "="
    print bx
    print "*"
    println [cx+1]
    //println " is not prime"
    jmp finish

is_prime:
    mov cx,0
    mov ax,[cx]
    print ax
    println " is prime"

finish:
    println