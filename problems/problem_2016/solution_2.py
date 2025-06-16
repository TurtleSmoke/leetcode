import pytest
from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        left = 0
        res = -1
        for right in range(1, len(nums)):
            if nums[right] > nums[left]:
                res = max(res, nums[right] - nums[left])
            else:
                left = right
            right += 1

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
