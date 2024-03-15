import functools
from typing import List
import pytest


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_occ = nums.count(0)
        if zero_occ > 1:
            return [0] * len(nums)

        prod = functools.reduce(lambda x, y: x * (y if y != 0 else 1), nums, 1)
        return [prod // n if zero_occ == 0 else 0 if n != 0 else prod for n in nums]


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
