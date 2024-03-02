import pytest
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0 for _ in nums]
        l, r = 0, len(nums) - 1
        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])
            if left > right:
                res[r - l] = left**2
                l += 1
            else:
                res[r - l] = right**2
                r -= 1
        return res


tests = [
    (
        ([-4, -1, 0, 3, 10],),
        [0, 1, 9, 16, 100],
    ),
    (
        ([-7, -3, 2, 3, 11],),
        [4, 9, 9, 49, 121],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().sortedSquares(*inputs)
    assert output == expected
