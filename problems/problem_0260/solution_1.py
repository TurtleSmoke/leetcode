from functools import reduce
from typing import List

import pytest


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = reduce(lambda x, y: x ^ y, nums)
        nz = xor & -xor
        res1 = reduce(lambda x, y: x ^ y, filter(lambda x: x & nz, nums))
        return [res1, res1 ^ xor]


tests = [
    (
        ([1, 2, 1, 3, 2, 5],),
        [3, 5],
    ),
    (
        ([-1, 0],),
        [-1, 0],
    ),
    (
        ([0, 1],),
        [1, 0],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().singleNumber(*inputs)
    assert sorted(output) == sorted(expected)
