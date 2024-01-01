import pytest
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1

        res = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                res = mid
                break

        if res == -1:
            return [-1, -1]

        first, last = mid, mid

        while first > 0 and nums[first - 1] == nums[mid]:
            first -= 1
        while last < len(nums) - 1 and nums[last + 1] == nums[mid]:
            last += 1

        return [first, last]


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
