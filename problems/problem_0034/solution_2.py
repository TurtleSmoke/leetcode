import pytest
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(x):
            left, right = 0, len(nums)

            while left < right:
                mid = (left + right) // 2
                if nums[mid] < x:
                    left = mid + 1
                else:
                    right = mid

            return left

        left = binary_search(target)
        right = binary_search(target + 1) - 1

        if left <= right:
            return [left, right]

        return [-1, -1]


tests = [
    (
        ([5, 7, 7, 8, 8, 10], 8),
        [3, 4],
    ),
    (
        ([5, 7, 7, 8, 8, 10], 6),
        [-1, -1],
    ),
    (
        ([], 0),
        [-1, -1],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().searchRange(*inputs)
    assert output == expected
