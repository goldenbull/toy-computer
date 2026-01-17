#!/usr/bin/env python3


from floatlib import BigFloat


def calculate_pi(iterations=1000, debug=False):
    """
    Calculate PI using the continued fraction formula:
    π = 2 + 1/3 × (2 + 2/5 × (2 + 3/7 × (2 + ... (2 + k/(2k+1) × (2 + ...))...)))

    This formula is evaluated from the innermost term outward.

    Args:
        iterations: Number of terms to compute (more = higher precision)
        debug: Print debug information

    Returns:
        BigFloat: Computed value of PI
    """

    # Start with 2 (the innermost constant)
    ret = BigFloat(2)

    # Work backwards from k = iterations down to k = 1
    # At each step: ret = 2 + k/(2k+1) × ret
    for k in range(iterations, 0, -1):
        # Calculate k/(2k+1)
        a = BigFloat(k)
        b = BigFloat(2 * k + 1)
        c = a.divide(b)

        # Multiply by current result
        d = c.multiply(ret)

        # Add 2
        ret = BigFloat(2).add(d)

    return ret


def main1():
    # Test with different iteration counts
    test_cases = [10, 50, 100, 500, 1000, 2000]
    for iterations in test_cases:
        pi = calculate_pi(iterations)
        print(f"PI with {iterations:5d} iterations: {pi}")
    pi100 = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
    print(" real PI with 100 digits:", pi100)


def main2():
    """
    let i = 1n;
    let x = 3n * (10n ** 10000n);
    let pi = x;
    while (x > 0) {
            x = x * i / ((i + 1n) * 4n);
            pi += x / (i + 2n);
            i += 2n;
    }
    console.log(pi / (10n ** 20n));
    """
    i = BigFloat(1)
    r = BigFloat(10)
    for j in range(120):
        r = r * 10
    x = r * 3
    pi = x
    # while x > 0:
    for j in range(200):
        x = x * i / ((i + 1) * 4)
        pi = pi + x / (i + 2)
        i = i + 2
        print(pi, x)


def main3():
    i = BigFloat(1)
    r = BigFloat(1)
    epsilon = BigFloat(1)
    for j in range(120):
        epsilon /= 10
    x = r * 3
    pi = x
    while x > epsilon:
        x = x * i / ((i + 1) * 4)
        pi = pi + x / (i + 2)
        i = i + 2
        print(pi, x)


if __name__ == "__main__":
    # main1()
    # main2()
    main3()
