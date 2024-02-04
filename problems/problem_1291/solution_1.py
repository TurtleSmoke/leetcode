import pytest
from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        res = []
        for size in range(len(str(low)), len(str(high)) + 1):
            for i in range(1, 10 - size + 1):
                n = int("".join(digits[i : i + size]))
                if low <= n <= high:
                    res.append(n)

        return res


tests = [
    (
        (100, 300),
        [123, 234],
    ),
    (
        (1000, 13000),
        [1234, 2345, 3456, 4567, 5678, 6789, 12345],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().sequentialDigits(*inputs)
    assert output == expected
