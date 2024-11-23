from functools import reduce
from typing import List

import pytest


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        dp = reduce(lambda x, y: x ^ y, nums)
        res = []
        for i in range(len(nums) - 1, -1, -1):
            res.append(dp ^ (2**maximumBit - 1))
            dp ^= nums[i]

        return res


tests = [
    (
        ([0, 1, 1, 3], 2),
        [0, 3, 2, 3],
    ),
    (
        ([2, 3, 4, 7], 3),
        [5, 2, 6, 5],
    ),
    (
        ([0, 1, 2, 2, 5, 7], 3),
        [4, 3, 6, 4, 6, 7],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().getMaximumXor(*inputs)
    assert output == expected
