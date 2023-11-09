from typing import List

import pytest


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        unique_last_index = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[unique_last_index]:
                unique_last_index += 1
                nums[unique_last_index] = nums[i]

        return unique_last_index + 1


tests = [
    (
        ([1, 1, 2],),
        (
            2,
            [1, 2],
        ),
    ),
    (
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4],),
        (
            5,
            [0, 1, 2, 3, 4],
        ),
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    f = getattr(
        Solution(),
        next(method for method in dir(Solution()) if not method.startswith("_")),
    )
    output = f(inputs[0])
    assert output == expected[0]
    assert inputs[0][:output] == expected[1]
