import pytest
from typing import List
import bisect
import functools


@functools.lru_cache()
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        def LIS(nums):
            res = [1] * len(nums)
            dp = [nums[0]]
            for i in range(1, len(nums)):
                idx = bisect.bisect_left(dp, nums[i])
                if idx == len(dp):
                    dp.append(nums[i])
                else:
                    dp[idx] = nums[i]
                res[i] = len(dp)
            return res

        inc = LIS(nums)
        dec = LIS(nums[::-1])[::-1]

        res = 0
        for i in range(len(nums)):
            if inc[i] > 1 and dec[i] > 1:
                res = max(res, inc[i] + dec[i] - 1)
        return len(nums) - res


tests = [
    (
        ([1, 3, 1],),
        0,
    ),
    (
        ([2, 1, 1, 5, 6, 2, 3, 1],),
        3,
    ),
    (
        ([1, 16, 84, 9, 29, 71, 86, 79, 72, 12],),
        2,
    ),
    (
        ([1, 2, 3, 4, 4, 3, 2, 1],),
        1,
    ),
    (
        ([9, 8, 1, 7, 6, 5, 4, 3, 2, 1],),
        2,
    ),
    (
        ([100, 92, 89, 77, 74, 66, 64, 66, 64],),
        6,
    ),
]


@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().minimumMountainRemovals(*inputs)
    assert output == expected
