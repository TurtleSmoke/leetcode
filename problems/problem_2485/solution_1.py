from math import sqrt
import pytest


class Solution:
    def pivotInteger(self, n: int) -> int:
        summ = n * (n + 1) / 2
        x = int(sqrt(summ))
        return x if x * x == summ else -1


tests = [
    (
        (8,),
        6,
    ),
    (
        (1,),
        1,
    ),
    (
        (4,),
        -1,
    ),
    (
        (15,),
        -1,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().pivotInteger(*inputs)
    assert output == expected
