from typing import List

import pytest


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = nums[0]
        occ = 1
        for x in nums:
            if occ == 0:
                occ = 1
                res = x
            elif res == x:
                occ += 1
            else:
                occ -= 1

        return res


tests = [
    (
        ([3, 2, 3],),
        3,
    ),
    (
        ([2, 2, 1, 1, 1, 2, 2],),
        2,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().majorityElement(*inputs)
    assert output == expected
