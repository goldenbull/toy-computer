#!/usr/bin/env python3
"""
Calculate PI using the continued fraction formula:
π = 2 + 1/3 × (2 + 2/5 × (2 + 3/7 × (2 + ... (2 + k/(2k+1) × (2 + ...))...)))

This formula is evaluated from the innermost term outward.
"""

from floatlib import BigFloat


def calculate_pi(iterations=1000, debug=False):
    """
    Calculate PI using continued fraction formula.

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


def main():
    # Test with different iteration counts
    test_cases = [10, 50, 100, 500, 1000, 2000]
    for iterations in test_cases:
        pi = calculate_pi(iterations)
        print(f"PI with {iterations:5d} iterations: {pi}")


if __name__ == "__main__":
    main()
