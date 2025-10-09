import pytest
from typing import List


class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        dp = [0] * (len(skill) + 1)
        for m in mana:
            for i, s in enumerate(skill):
                dp[i + 1] = max(dp[i + 1], dp[i]) + m * s
            for i in range(len(skill) - 1, -1, -1):
                dp[i] = dp[i + 1] - m * skill[i]
        return dp[-1]


tests = [
    (
        ([1, 5, 2, 4], [5, 1, 4, 2]),
        110,
    ),
    (
        ([1, 1, 1], [1, 1, 1]),
        5,
    ),
    (
        ([1, 2, 3, 4], [1, 2]),
        21,
    ),
    (
        ([3, 5, 3, 9], [1, 10, 7, 3]),
        293,
    ),
]


@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().minTime(*inputs)
    assert output == expected
