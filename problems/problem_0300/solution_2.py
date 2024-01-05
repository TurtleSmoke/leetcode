import bisect
from typing import List

import pytest


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [nums[0]]
        for x in nums[1:]:
            if res[-1] < x:
                res.append(x)
            else:
                res[bisect.bisect_left(res, x)] = x

        return len(res)


tests = [
    (
        ([10, 9, 2, 5, 3, 7, 101, 18],),
        4,
    ),
    (
        ([0, 1, 0, 3, 2, 3],),
        4,
    ),
    (
        ([7, 7, 7, 7, 7, 7, 7],),
        1,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().lengthOfLIS(*inputs)
    assert output == expected
