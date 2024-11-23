from typing import List

import pytest


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        total = 0
        min_length = float("inf")
        while right < len(nums):
            total += nums[right]
            while total >= k:
                min_length = min(min_length, right - left + 1)
                total -= nums[left]
                left += 1
            right += 1
        return min_length if min_length != float("inf") else 0


tests = [
    (
        ([1, 2, 3], 2),
        1,
    ),
    (
        ([2, 1, 8], 10),
        3,
    ),
    (
        ([1, 2], 0),
        1,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().minimumSubarrayLength(*inputs)
    assert output == expected
