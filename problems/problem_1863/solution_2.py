import pytest
from functools import reduce
from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x | y, nums) << (len(nums) - 1)


tests = [
    (
        ([1, 3],),
        6,
    ),
    (
        ([5, 1, 6],),
        28,
    ),
    (
        ([3, 4, 5, 6, 7, 8],),
        480,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().subsetXORSum(*inputs)
    assert output == expected
