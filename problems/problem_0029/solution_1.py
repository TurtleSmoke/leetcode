import pytest
import numpy as np


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Ensure that the input is a 32-bit integer
        # It makes the code a bit tricky because abs(MIN_INT) == MIN_INT
        min_int, dividend, divisor = np.int32(-(2**31)), np.int32(dividend), np.int32(divisor)

        if divisor == min_int:
            return 1 if dividend == min_int else 0

        if dividend == -(2**31) and divisor == -1:
            return 2**31 - 1

        output_sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        a, b, res = abs(dividend), abs(divisor), 0
        # Corner case for MIN_INT
        if 0 > dividend == a:
            a = abs(a + b)
            res += 1

        for x in range(31, -1, -1):
            if (a >> x) - b >= 0:
                res += 1 << x
                a -= b << x

        return output_sign * res


tests = [
    (
        (10, 3),
        3,
    ),
    (
        (-10, -3),
        3,
    ),
    (
        (7, -3),
        -2,
    ),
    (
        (-2147483648, -1),
        2147483647,
    ),
    (
        (-2147483648, -3),
        715827882,
    ),
    (
        (0, 1),
        0,
    ),
    (
        (-1010369383, -2147483648),
        0,
    ),
    (
        (-2147483648, -2147483648),
        1,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().divide(*inputs)
    assert output == expected
