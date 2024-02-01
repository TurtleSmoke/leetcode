import pytest
from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums = sorted(nums)
        if any(abs(nums[i] - nums[i + 2]) > k for i in range(0, len(nums), 3)):
            return []
        return [nums[i : i + 3] for i in range(0, len(nums), 3)]


tests = [
    (
        ([1, 3, 4, 8, 7, 9, 3, 5, 1], 2),
        [[1, 1, 3], [3, 4, 5], [7, 8, 9]],
    ),
    (
        ([1, 3, 3, 2, 7, 3], 3),
        [],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().divideArray(*inputs)
    assert output == expected
