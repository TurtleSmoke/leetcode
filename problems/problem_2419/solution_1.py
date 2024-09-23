from typing import List

import pytest


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maximum = max(nums)

        res = 0
        max_window = 0
        for i in range(len(nums)):
            if nums[i] == maximum:
                max_window += 1
            else:
                res = max(res, max_window)
                max_window = 0

        return max(res, max_window)


tests = [
    (
        ([1, 2, 3, 3, 2, 2],),
        2,
    ),
    (
        ([1, 2, 3, 4],),
        1,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().longestSubarray(*inputs)
    assert output == expected
