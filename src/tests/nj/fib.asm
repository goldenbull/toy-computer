    mov cx,0
    mov [cx],1

    add cx,1
    mov [cx],1

repeat:
    add cx,1
    mov ax,[cx-2]
    add ax,[cx-1]
    mov [cx],ax
    print [cx]
    print " "

    cmp cx,100
    jl repeat