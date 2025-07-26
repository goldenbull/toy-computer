    input n;

    if(n<=1)
        goto not_prime;

    if(n==2||n==3)
        goto is_prime;

    if(n%2!=0)
        goto go_on1

    a=2
    b=n/2
    goto not_prime2

go_on1:

    m=3
loop1:
    if(n%m!=0)
        goto go_on2

    a=m
    b=n/m
    goto not_prime2

go_on2:
    m=m+2
    if(m*m>n)
        goto is_prime
    goto loop1


not_prime:
    print(n, " is not a prime")
    goto finish

is_prime:
    print(n, " is a prime")
    goto finish

not_prime2:
    print(n, " is not a prime")
    print(n,"=",a,"*",b)

finish:
    println()