import pytest
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Find longest non-increasing suffix: this subarray is its last lexicographic permutation
        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        if i == 0:
            # All elements are non-increasing: this is the last lexicographic permutation
            nums.reverse()
        else:
            # Find the closest successor to replace pivot i
            j = len(nums) - 1
            while nums[j] <= nums[i - 1]:
                j -= 1

            # Swap pivot with its successor
            nums[i - 1], nums[j] = nums[j], nums[i - 1]

            # Reverse the longest non-increasing suffix
            nums[i:] = nums[len(nums) - 1 : i - 1 : -1]


tests = [
    (
        ([1, 2, 3],),
        [1, 3, 2],
    ),
    (
        ([3, 2, 1],),
        [1, 2, 3],
    ),
    (
        ([1, 1, 5],),
        [1, 5, 1],
    ),
    (
        ([1, 3, 2],),
        [2, 1, 3],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    Solution().nextPermutation(*inputs)
    assert inputs[0] == expected
