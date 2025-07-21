#include <stdio.h>

int fib(int n)
{
    if(n <= 2)
        return 1;

    int a = fib(n - 1);
    int b = fib(n - 2);

    printf("%d ", a+b);

    return a + b;
}

int main()
{
    int x = fib(20);
    printf("%d\n", x);
    return 0;
}