import pytest
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


tests = [
    (
        ([10, 9, 2, 5, 3, 7, 101, 18],),
        4,
    ),
    (
        ([0, 1, 0, 3, 2, 3],),
        4,
    ),
    (
        ([7, 7, 7, 7, 7, 7, 7],),
        1,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().lengthOfLIS(*inputs)
    assert output == expected
