import pytest


class Solution:
    def climbStairs(self, n: int) -> int:
        current, prev = 1, 1
        for _ in range(n - 1):
            current, prev = current + prev, current

        return current


tests = [
    (
        (2,),
        2,
    ),
    (
        (3,),
        3,
    ),
    (
        (4,),
        5,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().climbStairs(*inputs)
    assert output == expected
