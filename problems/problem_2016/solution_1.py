import pytest
from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = -1
        for i, a in enumerate(nums):
            for b in nums[i:]:
                if b > a:
                    res = max(res, b - a)

        return res


tests = [
    (
        ([7, 1, 5, 4],),
        4,
    ),
    (
        ([9, 4, 3, 2],),
        -1,
    ),
    (
        ([1, 5, 2, 10],),
        9,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().maximumDifference(*inputs)
    assert output == expected
