import pytest
from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        for n in range(len(nums), -1, -1):
            for i in range(1, n):
                nums[i - 1] = (nums[i - 1] + nums[i]) % 10

        return nums[0]


tests = [
    (
        ([1, 2, 3, 4, 5],),
        8,
    ),
    (
        ([5],),
        5,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().triangularSum(*inputs)
    assert output == expected
