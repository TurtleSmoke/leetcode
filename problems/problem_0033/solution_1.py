import pytest
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (right + left) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


tests = [
    (
        ([4, 5, 6, 7, 0, 1, 2], 0),
        4,
    ),
    (
        ([4, 5, 6, 7, 0, 1, 2], 3),
        -1,
    ),
    (
        ([1], 0),
        -1,
    ),
    (
        ([2, 4, 5, 6, 7, 0, 1], 2),
        0,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().search(*inputs)
    assert output == expected
