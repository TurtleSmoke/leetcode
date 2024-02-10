from typing import List

import pytest


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        dp = [[]]
        for n in sorted(nums):
            dp.append(max((s + [n] for s in dp if not s or n % s[-1] == 0), key=len))
        return max(dp, key=len)


tests = [
    (
        ([1, 2, 3],),
        [1, 2],
    ),
    (
        ([1, 2, 4, 8],),
        [1, 2, 4, 8],
    ),
    (
        ([5, 9, 18, 54, 108, 540, 90, 180, 360, 720],),
        [9, 18, 90, 180, 360, 720],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().largestDivisibleSubset(*inputs)
    assert sorted(output) == expected
