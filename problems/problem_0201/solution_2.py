import pytest
from functools import reduce


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while right > left:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift


tests = [
    (
        (5, 7),
        4,
    ),
    (
        (0, 0),
        0,
    ),
    (
        (1, 2147483647),
        0,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().rangeBitwiseAnd(*inputs)
    assert output == expected
