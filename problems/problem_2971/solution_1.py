import pytest
from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)
        cur = sum(nums)
        for i in range(len(nums) - 1, -1, -1):
            if cur > nums[i] * 2:
                return cur
            cur -= nums[i]

        return -1


tests = [
    (
        ([5, 5, 5],),
        15,
    ),
    (
        ([1, 12, 1, 2, 5, 50, 3],),
        12,
    ),
    (
        ([5, 5, 50],),
        -1,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().largestPerimeter(*inputs)
    assert output == expected
