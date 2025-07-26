    // [0]:n
    // [1]:m
    // [2]:s
    // [3]:t
    // [4]:p
    // [5]:i

     mov ax,1000000
     mov cx,0
     mov [cx+4],ax
     mov ax,1
     mov [cx+5],ax

repeat:
    mov ax,[cx+5]
    mov [cx],ax
    jmp check_is_prime
back_to_main1:
    cmp ax,0
    je main_goon1
    print [cx+5]
    println
main_goon1:
    mov ax,[cx+5]
    add ax,1
    mov [cx+5],ax
    cmp ax,[cx+4]
    jle repeat
    halt

//---------------------------------------
// prime function
//
check_is_prime:
    // input n
    // input ax
    //mov cx,0
    //mov [cx],ax

    //if(n<=1)
    //    goto not_prime;
    mov cx,0
    mov ax,[cx]
    cmp ax,1
    jle not_prime

    //if(n==2||n==3)
    //    goto is_prime;
    mov cx,0
    mov ax,[cx]
    cmp ax,2
    je is_prime
    cmp ax,3
    je is_prime

    //if(n%2!=0)
    //    goto go_on1
    mov cx,0
    mov ax,[cx]
    div 2
    cmp dx,0
    jne go_on1

    //s=2
    //t=n/2
    mov cx,0
    mov [cx+2],2
    mov ax,[cx]
    div 2
    mov [cx+3],ax

    //goto not_prime2
    jmp not_prime2
    
go_on1:

    //m=3
    mov cx,0
    mov [cx+1],3

loop1:
    //if(n%m!=0)
    //    goto go_on2
    mov cx,0
    mov ax,[cx]
    div [cx+1]
    cmp dx,0
    jne go_on2

    // s=m
    mov cx,0
    mov ax,[cx+1]
    mov [cx+2],ax

    // t=n/m
    mov ax,[cx]
    div [cx+1]
    mov [cx+3],ax

    //goto not_prime2
    jmp not_prime2


go_on2:
    //m=m+2
    mov cx,0
    mov ax,[cx+1]
    add ax,2
    mov [cx+1],ax

    //if(m*m>n)
    //    goto is_prime
    mov ax,[cx+1]
    mul [cx+1]
    mov bx,[cx]
    cmp ax, bx
    jg is_prime
    
    //goto loop1
    jmp loop1

not_prime:
    //print(n, " is not a prime")
    mov ax,0
    //goto finish
    jmp finish

is_prime:
    //print(n, " is a prime")
    mov ax,1
    //goto finish
    jmp finish

not_prime2:
    //print(n, " is not a prime")
    mov ax,0
    jmp finish

finish:
    jmp back_to_main1