class BigFloat:
    BASE = 10**7  # Each element holds a digit in base 10^7
    PRECISION = 6  # Number of elements in the values array

    def __init__(self, init: int):
        self.sign = 1 if init >= 0 else -1
        self.exponent = 0  # Exponent: number = sign × mantissa × BASE^exponent
        self.values = [abs(init)] + [0] * (self.PRECISION - 1)
        self.normalize()

    def normalize(self):
        """Normalize the representation by handling carries and ensuring each element is in [0, BASE)"""
        # Handle carries from right to left
        for i in range(self.PRECISION - 1, 0, -1):
            if self.values[i] >= self.BASE:
                carry = self.values[i] // self.BASE
                self.values[i] %= self.BASE
                self.values[i - 1] += carry
            elif self.values[i] < 0:
                borrow = (-self.values[i] + self.BASE - 1) // self.BASE
                self.values[i] += borrow * self.BASE
                self.values[i - 1] -= borrow

        # Handle the most significant element overflow
        if self.values[0] >= self.BASE:
            carry = self.values[0] // self.BASE
            # Shift everything right and adjust exponent
            for i in range(self.PRECISION - 1, 0, -1):
                self.values[i] = self.values[i - 1]
            self.values[0] = carry
            self.values[1] = self.values[1] % self.BASE
            self.exponent += 1

        # Handle sign flip
        if self.values[0] < 0:
            self.sign *= -1
            for i in range(self.PRECISION):
                self.values[i] = -self.values[i]
            self.normalize()  # Recurse to handle the flip

        # Normalize mantissa: shift left until values[0] != 0 or all zeros
        while self.values[0] == 0 and any(v != 0 for v in self.values[1:]):
            for i in range(self.PRECISION - 1):
                self.values[i] = self.values[i + 1]
            self.values[self.PRECISION - 1] = 0
            self.exponent -= 1

    def copy(self):
        """Create a deep copy of this BigFloat"""
        result = BigFloat(0)
        result.sign = self.sign
        result.values = self.values.copy()
        result.exponent = self.exponent
        return result

    def add(self, other):
        """Add two BigFloat numbers"""
        result = BigFloat(0)

        # Align exponents - use the larger exponent
        exp_diff = self.exponent - other.exponent

        if exp_diff == 0:
            # Same exponent, direct addition
            if self.sign == other.sign:
                result.sign = self.sign
                for i in range(self.PRECISION):
                    result.values[i] = self.values[i] + other.values[i]
            else:
                for i in range(self.PRECISION):
                    result.values[i] = self.values[i] - other.values[i]
                result.sign = self.sign
            result.exponent = self.exponent
        elif exp_diff > 0:
            # self has larger exponent, shift other right
            result.exponent = self.exponent
            result.sign = self.sign
            # First copy self values
            for i in range(self.PRECISION):
                result.values[i] = self.values[i]
            # Then add other values at shifted positions
            for i in range(self.PRECISION):
                if i + exp_diff < self.PRECISION:
                    if self.sign == other.sign:
                        result.values[i + exp_diff] += other.values[i]
                    else:
                        result.values[i + exp_diff] -= other.values[i]
        else:
            # other has larger exponent, shift self right
            result.exponent = other.exponent
            result.sign = other.sign
            # First copy other values
            for i in range(self.PRECISION):
                result.values[i] = other.values[i]
            # Then add self values at shifted positions
            for i in range(self.PRECISION):
                if i - exp_diff < self.PRECISION:
                    if self.sign == other.sign:
                        result.values[i - exp_diff] += self.values[i]
                    else:
                        result.values[i - exp_diff] -= self.values[i]

        result.normalize()
        return result

    def subtract(self, other):
        """Subtract two BigFloat numbers"""
        # Create a negated copy of other
        neg_other = other.copy()
        neg_other.sign *= -1
        return self.add(neg_other)

    def multiply(self, other):
        """Multiply two BigFloat numbers"""
        result = BigFloat(0)
        result.sign = self.sign * other.sign
        result.exponent = self.exponent + other.exponent  # Exponents add in multiplication

        # Use temporary array with double precision to hold intermediate results
        temp = [0] * (self.PRECISION * 2)

        # Multiply each element
        for i in range(self.PRECISION):
            for j in range(self.PRECISION):
                temp[i + j] += self.values[i] * other.values[j]

        # Normalize the temporary array from right to left
        for i in range(len(temp) - 1, 0, -1):
            if temp[i] >= self.BASE:
                carry = temp[i] // self.BASE
                temp[i] %= self.BASE
                temp[i - 1] += carry

        # Copy the most significant PRECISION elements to result
        # We need to determine the scaling - for now, take elements that preserve precision
        for i in range(self.PRECISION):
            result.values[i] = temp[i]

        result.normalize()
        return result

    def divide(self, other):
        """Divide two BigFloat numbers with proper precision"""
        if all(v == 0 for v in other.values):
            raise ZeroDivisionError("Division by zero")

        result = BigFloat(0)
        result.sign = self.sign * other.sign
        result.exponent = self.exponent - other.exponent  # Exponents subtract in division

        # Long division algorithm for high precision
        # Use the divisor's first element (most significant)
        divisor_val = other.values[0]

        if divisor_val == 0:
            raise ZeroDivisionError("Division by zero")

        # Perform long division
        remainder = 0
        for i in range(self.PRECISION):
            # Bring down the next digit and add previous remainder
            current = remainder * self.BASE + self.values[i]

            # Divide and get quotient and remainder
            result.values[i] = current // divisor_val
            remainder = current % divisor_val

        result.normalize()
        return result

    def __str__(self):
        """String representation in human-readable decimal format"""
        if all(v == 0 for v in self.values):
            return "0.0"

        sign_str = "-" if self.sign < 0 else ""

        # Build the full digit string from the mantissa
        # Each element contributes 6 digits (since BASE = 10^6)
        digits_per_element = 6  # log10(BASE) = log10(10^6) = 6

        # Convert values to a continuous string of digits
        digit_string = ""
        for i, v in enumerate(self.values):
            if i == 0:
                # First element doesn't need leading zeros
                digit_string += str(v)
            else:
                # Subsequent elements need padding to maintain place value
                digit_string += f"{v:0{digits_per_element}d}"

        # Calculate where the decimal point should go
        # exponent tells us how many BASE positions to shift
        # Each BASE position = 6 decimal digits
        decimal_shift = self.exponent * digits_per_element

        # The decimal point starts after the first element's natural length
        natural_decimal_pos = len(str(self.values[0]))
        actual_decimal_pos = natural_decimal_pos + decimal_shift

        # Remove trailing zeros for cleaner output
        digit_string = digit_string.rstrip('0')
        if not digit_string:
            return "0.0"

        # Insert decimal point
        if actual_decimal_pos <= 0:
            # Number is less than 1: 0.00...XXX
            result = "0." + "0" * (-actual_decimal_pos) + digit_string
        elif actual_decimal_pos >= len(digit_string):
            # Number is a large integer: XXX000...
            result = digit_string + "0" * (actual_decimal_pos - len(digit_string)) + ".0"
        else:
            # Normal case: XXX.YYY
            result = digit_string[:actual_decimal_pos] + "." + digit_string[actual_decimal_pos:]

        return sign_str + result

    def __str_debug__(self):
        """Debug string representation showing internal structure"""
        sign_str = "-" if self.sign < 0 else ""
        values_str = ".".join(f"{v:06d}" for v in self.values)
        return f"{sign_str}{values_str} × {self.BASE}^{self.exponent}"

    def __repr__(self):
        return f"BigFloat(sign={self.sign}, values={self.values}, exp={self.exponent})"

    def to_float(self):
        """Convert to Python float (approximate)"""
        result = 0.0
        multiplier = 1.0
        for v in self.values:
            result += v * multiplier
            multiplier /= self.BASE
        result *= (self.BASE ** self.exponent)
        return result * self.sign
