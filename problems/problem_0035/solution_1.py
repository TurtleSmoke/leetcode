import pytest
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left


tests = [
    (
        ([1, 3, 5, 6], 5),
        2,
    ),
    (
        ([1, 3, 5, 6], 2),
        1,
    ),
    (
        ([1, 3, 5, 6], 7),
        4,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().searchInsert(*inputs)
    assert output == expected
