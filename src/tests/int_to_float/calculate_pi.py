#!/usr/bin/env python3

from floatlib import BigFloat


def calculate_pi(n: int):
    i = BigFloat(1)
    r = BigFloat(1)
    epsilon = BigFloat(1)
    for j in range(n):
        epsilon /= 10
    x = r * 3
    pi = x
    while x > epsilon:
        x = x * i / ((i + 1) * 4)
        pi = pi + x / (i + 2)
        i = i + 2
        print(pi, x)


if __name__ == "__main__":
    calculate_pi(100)
