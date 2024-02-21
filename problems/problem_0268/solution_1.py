import pytest
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)


tests = [
    (
        ([3, 0, 1],),
        2,
    ),
    (
        ([0, 1],),
        2,
    ),
    (
        ([9, 6, 4, 2, 3, 5, 7, 0, 1],),
        8,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().missingNumber(*inputs)
    assert output == expected
