import pytest
from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * (len(arr) + 1)
        for i in range(1, len(arr) + 1):
            max_val = 0
            for j in range(1, k + 1):
                if i - j >= 0:
                    max_val = max(max_val, arr[i - j])
                    dp[i] = max(dp[i], dp[i - j] + max_val * j)

        return dp[-1]


tests = [
    (
        ([1, 15, 7, 9, 2, 5, 10], 3),
        84,
    ),
    (
        ([1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4),
        83,
    ),
    (
        ([1], 1),
        1,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().maxSumAfterPartitioning(*inputs)
    assert output == expected
