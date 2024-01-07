from typing import List
from collections import defaultdict

import pytest


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        res = 0

        for i in range(1, len(nums)):
            for j in range(i):
                delta = nums[i] - nums[j]
                res += dp[(j, delta)]
                dp[(i, delta)] += dp[(j, delta)] + 1

        return res


tests = [
    (
        ([2, 4, 6, 8, 10],),
        7,
    ),
    (
        ([7, 7, 7, 7],),
        5,
    ),
    (
        ([7, 7, 7, 7, 7],),
        16,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().numberOfArithmeticSlices(*inputs)
    assert output == expected
