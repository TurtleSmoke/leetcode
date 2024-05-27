import pytest
from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] >= len(nums):
            return len(nums)

        for i in range(1, len(nums)):
            if nums[i - 1] < len(nums) - i <= nums[i]:
                return len(nums) - i

        return -1


tests = [
    (
        ([3, 5],),
        2,
    ),
    (
        ([0, 0],),
        -1,
    ),
    (
        ([0, 4, 3, 0, 4],),
        3,
    ),
    (
        ([3, 6, 7, 7, 0],),
        -1,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().specialArray(*inputs)
    assert output == expected
