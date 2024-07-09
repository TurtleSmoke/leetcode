from typing import List
import pytest


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return 0
        nums = sorted(nums)
        return min((nums[i - 4] - nums[i] for i in range(4)))


tests = [
    (
        ([5, 3, 2, 4],),
        0,
    ),
    (
        ([1, 5, 0, 10, 14],),
        1,
    ),
    (
        ([3, 100, 20],),
        0,
    ),
    (
        ([53, 60, 100, 85, 16, 68, 64, 31, 37, 78],),
        47,
    ),
    (
        ([6, 6, 0, 1, 1, 4, 6],),
        2,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().minDifference(*inputs)
    assert output == expected
