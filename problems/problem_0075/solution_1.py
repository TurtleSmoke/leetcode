from collections import Counter
from typing import List

import pytest


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        current = 0
        for i in range(len(nums)):
            while count[current] <= 0:
                current += 1

            nums[i] = current
            count[current] -= 1


tests = [
    (
        ([2, 0, 2, 1, 1, 0],),
        [0, 0, 1, 1, 2, 2],
    ),
    (
        ([2, 0, 1],),
        [0, 1, 2],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    input = inputs[0]
    Solution().sortColors(input)
    assert input == expected
