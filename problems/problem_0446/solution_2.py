from typing import List
from collections import defaultdict

import pytest


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        nums_to_idx = defaultdict(list)
        for i, n in enumerate(nums):
            nums_to_idx[n].append(i)
        dp = [[0] * len(nums) for _ in range(len(nums))]
        res = 0

        for i in range(len(nums)):
            for j in range(i):
                prev = 2 * nums[j] - nums[i]
                if prev in nums_to_idx:
                    for k in nums_to_idx[prev]:
                        if k >= j:
                            break
                        dp[i][j] += dp[j][k] + 1

                res += dp[i][j]

        return res


tests = [
    (
        ([2, 4, 6, 8, 10],),
        7,
    ),
    (
        ([7, 7, 7, 7],),
        5,
    ),
    (
        ([7, 7, 7, 7, 7],),
        16,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().numberOfArithmeticSlices(*inputs)
    assert output == expected
