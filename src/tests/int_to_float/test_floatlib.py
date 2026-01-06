#!/usr/bin/env python3
"""Test suite for BigFloat class"""

from floatlib import BigFloat


def test_basic_init():
    """Test basic initialization"""
    print("=== Test: Basic Initialization ===")

    a = BigFloat(12345)
    print(f"BigFloat(12345) = {a}")
    print(f"  values: {a.values}")
    print(f"  sign: {a.sign}")

    b = BigFloat(-6789)
    print(f"BigFloat(-6789) = {b}")
    print(f"  values: {b.values}")
    print(f"  sign: {b.sign}")
    print()


def test_addition():
    """Test addition operations"""
    print("=== Test: Addition ===")

    a = BigFloat(12345)
    b = BigFloat(6789)
    c = a.add(b)
    print(f"{a} + {b}")
    print(f"  = {c}")
    print(f"  Expected: ~19134")
    print(f"  to_float(): {c.to_float()}")

    # Test with negative numbers
    a = BigFloat(1000)
    b = BigFloat(-300)
    c = a.add(b)
    print(f"\n{a} + {b}")
    print(f"  = {c}")
    print(f"  Expected: ~700")
    print(f"  to_float(): {c.to_float()}")

    # Test negative + negative
    a = BigFloat(-500)
    b = BigFloat(-200)
    c = a.add(b)
    print(f"\n{a} + {b}")
    print(f"  = {c}")
    print(f"  Expected: ~-700")
    print(f"  to_float(): {c.to_float()}")
    print()


def test_subtraction():
    """Test subtraction operations"""
    print("=== Test: Subtraction ===")

    a = BigFloat(10000)
    b = BigFloat(3000)
    c = a.subtract(b)
    print(f"{a} - {b}")
    print(f"  = {c}")
    print(f"  Expected: ~7000")
    print(f"  to_float(): {c.to_float()}")

    # Test that results in negative
    a = BigFloat(1000)
    b = BigFloat(5000)
    c = a.subtract(b)
    print(f"\n{a} - {b}")
    print(f"  = {c}")
    print(f"  Expected: ~-4000")
    print(f"  to_float(): {c.to_float()}")
    print()


def test_multiplication():
    """Test multiplication operations"""
    print("=== Test: Multiplication ===")

    a = BigFloat(123)
    b = BigFloat(456)
    c = a.multiply(b)
    print(f"{a} * {b}")
    print(f"  = {c}")
    print(f"  Expected: ~56088")
    print(f"  to_float(): {c.to_float()}")

    # Test with negative
    a = BigFloat(-100)
    b = BigFloat(50)
    c = a.multiply(b)
    print(f"\n{a} * {b}")
    print(f"  = {c}")
    print(f"  Expected: ~-5000")
    print(f"  to_float(): {c.to_float()}")

    # Test larger numbers
    a = BigFloat(999999)
    b = BigFloat(1000000)
    c = a.multiply(b)
    print(f"\n{a} * {b}")
    print(f"  = {c}")
    print(f"  Expected: ~999999000000")
    print(f"  to_float(): {c.to_float()}")
    print()


def test_division():
    """Test division operations"""
    print("=== Test: Division ===")

    a = BigFloat(10000)
    b = BigFloat(100)
    c = a.divide(b)
    print(f"{a} / {b}")
    print(f"  = {c}")
    print(f"  Expected: ~100")
    print(f"  to_float(): {c.to_float()}")

    # Test with remainder
    a = BigFloat(10000)
    b = BigFloat(300)
    c = a.divide(b)
    print(f"\n{a} / {b}")
    print(f"  = {c}")
    print(f"  Expected: ~33")
    print(f"  to_float(): {c.to_float()}")
    print()


def test_normalization():
    """Test normalization with carries"""
    print("=== Test: Normalization (Carries) ===")

    # Create a BigFloat and manually set values to test normalization
    a = BigFloat(0)
    a.values[0] = 0
    a.values[1] = 2000000  # Exceeds BASE (1000000)
    a.values[2] = 500000
    print(f"Before normalize: {a.values}")
    a.normalize()
    print(f"After normalize:  {a.values}")
    print(f"String form: {a}")
    print()


def test_large_numbers():
    """Test with very large numbers"""
    print("=== Test: Large Numbers ===")

    a = BigFloat(999999999)
    b = BigFloat(888888888)
    c = a.add(b)
    print(f"Large addition:")
    print(f"  {a.to_float()} + {b.to_float()}")
    print(f"  = {c.to_float()}")
    print(f"  String: {c}")
    print()


def test_zero():
    """Test operations with zero"""
    print("=== Test: Zero Operations ===")

    zero = BigFloat(0)
    a = BigFloat(12345)

    c = a.add(zero)
    print(f"{a.to_float()} + 0 = {c.to_float()}")

    c = a.multiply(zero)
    print(f"{a.to_float()} * 0 = {c.to_float()}")

    c = zero.add(a)
    print(f"0 + {a.to_float()} = {c.to_float()}")
    print()


def test_chained_operations():
    """Test chaining multiple operations"""
    print("=== Test: Chained Operations ===")

    a = BigFloat(100)
    b = BigFloat(50)
    c = BigFloat(25)

    # (a + b) * c
    result = a.add(b).multiply(c)
    print(f"(100 + 50) * 25 = {result.to_float()}")
    print(f"  Expected: 3750")

    # a * b + c
    result = a.multiply(b).add(c)
    print(f"100 * 50 + 25 = {result.to_float()}")
    print(f"  Expected: 5025")
    print()


def run_all_tests():
    """Run all test functions"""
    print("=" * 60)
    print("BigFloat Test Suite")
    print(f"BASE = {BigFloat.BASE} (10^6)")
    print(f"PRECISION = {BigFloat.PRECISION} elements")
    print("=" * 60)
    print()

    test_basic_init()
    test_addition()
    test_subtraction()
    test_multiplication()
    test_division()
    test_normalization()
    test_large_numbers()
    test_zero()
    test_chained_operations()

    print("=" * 60)
    print("All tests completed!")
    print("=" * 60)


if __name__ == "__main__":
    run_all_tests()

    # calc PI
    a = BigFloat(100)
    b = BigFloat(37)
    for i in range(100):
        a = a.multiply(b)
        print(a)
