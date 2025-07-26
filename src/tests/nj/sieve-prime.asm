    primes: memory[0-999]

    primes[0] = 2
    cnt = 1
    n = 3

loop1:
    i = 0
loop2:
    if n % primes[i] == 0:
        goto try_next_n
    i = i+1
    if i==cnt:
        jmp n_is_prime
    goto loop2


n_is_prime:
    primes[cnt] = n
    cnt = cnt+1
    if cnt==1000
        goto finish
    goto try_next_n

try_next_n:
    n = n+1
    goto loop1

finish:
    i=0
print_loop:
    print primes[i]
    i=i+1
    if i==1000:
        halt
    goto print_loop