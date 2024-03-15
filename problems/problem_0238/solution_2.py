from typing import List

import pytest


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]

        suffix_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix_prod
            suffix_prod *= nums[i]

        return res


tests = [
    (
        ([1, 2, 3, 4],),
        [24, 12, 8, 6],
    ),
    (
        ([-1, 1, 0, -3, 3],),
        [0, 0, 9, 0, 0],
    ),
    (
        ([0, 2, 3, 4],),
        [24, 0, 0, 0],
    ),
    (
        ([0, 0, 3, 4],),
        [0, 0, 0, 0],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().productExceptSelf(*inputs)
    assert output == expected
