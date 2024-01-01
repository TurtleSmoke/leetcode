from typing import List

import pytest


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] <= len(nums) and (nums[nums[i] - 1] != nums[i]):
                tmp = nums[i]
                nums[i] = nums[tmp - 1]
                nums[tmp - 1] = tmp

        for i, v in enumerate(nums):
            if i + 1 != v:
                return i + 1

        return len(nums) + 1


tests = [
    (
        ([1, 2, 0],),
        3,
    ),
    (
        ([3, 4, -1, 1],),
        2,
    ),
    (
        ([7, 8, 9, 11, 12],),
        1,
    ),
    (
        ([2, 2, 2],),
        1,
    ),
    (
        ([1],),
        2,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().firstMissingPositive(*inputs)
    assert output == expected
