import pytest
from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        res = nums[0]
        comb = 1
        for i in range(1, len(nums)):
            comb = comb * (len(nums) - i) // i
            res = (res + nums[i] * comb) % 10

        return res


tests = [
    (
        ([1, 2, 3, 4, 5],),
        8,
    ),
    (
        ([5],),
        5,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().triangularSum(*inputs)
    assert output == expected
