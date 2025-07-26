    //primes: memory[0-999]
    //i: [1000]
    //cnt:[1001]
    //n: [1002]
    
    //primes[0] = 2
    mov bp,0
    mov [bp],2

    //cnt = 1
    mov ax,1
    mov [bp+1001],ax

    //n = 3
    mov [bp+1002],3


loop1:
    //i = 0
    mov [bp+1000],0


loop2:
    //if n % primes[i] == 0:
    mov bx, [bp+1000]
    mov cx, [bx]
    mov ax,[bp+1002]
    div cx
    cmp dx,0
    je try_next_n
        //goto try_next_n
    
    //i = i+1
    mov bx,[bp+1000]
    add bx,1
    mov [bp+1000],bx

    //if i==cnt:
    //    jmp n_is_prime
    mov bx,[bp+1000]
    mov ax,[bp+1001]
    cmp ax,bx
    je n_is_prime


    //goto loop2
    jmp loop2


n_is_prime:
    //primes[cnt] = n
    mov ax,[bp+1002]
    mov bx,[bp+1001]
    mov [bx],ax

    //cnt = cnt+1
    mov bx,[bp+1001]
    add bx,1
    mov [bp+1001],bx

    //if cnt==1000
    //    goto finish
    mov bx,[bp+1001]
    cmp bx,1000
    je finish

    //goto try_next_n
    jmp try_next_n

try_next_n:
    //n = n+1
    mov bx,[bp+1002]
    add bx,1
    mov [bp+1002],bx

    //goto loop1
    jmp loop1

finish:
    //i=0
    mov [bp+1000],0

print_loop:
    //print primes[i]
    mov bx,[bp+1000]
    mov ax,[bx]
    print bx
    print ":"
    print ax
    println

    //i=i+1
    mov bx,[bp+1000]
    add bx,1
    mov [bp+1000],bx

    //if i==1000:
    mov bx,[bp+1000]
    cmp bx,1000
    je main_finish

        //halt
    //goto print_loop
    jmp print_loop
main_finish:
    halt