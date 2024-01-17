from functools import cache

import pytest


class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dfs(n):
            if n == 0:
                return 1
            elif n > 1:
                return dfs(n - 1) + dfs(n - 2)
            elif n > 0:
                return dfs(n - 1)

        return dfs(n)


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
