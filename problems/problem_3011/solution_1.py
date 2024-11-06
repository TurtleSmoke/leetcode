import pytest
from typing import List


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        one_nums = [bin(num).count("1") for num in nums]
        sub_nums = []
        i = 0
        for j in range(1, len(nums)):
            if one_nums[i] != one_nums[j]:
                sub_nums.append(sorted(nums[i:j]))
                i = j
        sub_nums.append(sorted(nums[i:]))
        return sorted(nums) == sum(sub_nums, [])


tests = [
    (
        ([8, 4, 2, 30, 15],),
        True,
    ),
    (
        ([1, 2, 3, 4, 5],),
        True,
    ),
    (
        ([3, 16, 8, 4, 2],),
        False,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().canSortArray(*inputs)
    assert output == expected
