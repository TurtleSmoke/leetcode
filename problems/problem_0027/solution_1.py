from typing import List

import pytest


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        begin, end = 0, len(nums) - 1
        while begin <= end:
            if nums[begin] == val:
                nums[begin], nums[end] = nums[end], nums[begin]
                end -= 1
            else:
                begin += 1
        return begin


tests = [
    (
        ([3, 2, 2, 3], 3),
        [2, 2],
    ),
    (
        ([0, 1, 2, 2, 3, 0, 4, 2], 2),
        [0, 1, 4, 0, 3],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().removeElement(*inputs)
    assert output == len(expected)
    assert set(inputs[0][:output]) == set(expected)
