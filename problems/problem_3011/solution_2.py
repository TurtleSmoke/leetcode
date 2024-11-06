from typing import List

import pytest


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        prev_max, cur_min, cur_max, prev_one = 0, 0, 0, 0
        for v in nums:
            cur_one = v.bit_count()
            if cur_one == prev_one:
                cur_min, cur_max = min(cur_min, v), max(cur_max, v)
            elif cur_min < prev_max:
                return False
            else:
                prev_max, cur_min, cur_max, prev_one = cur_max, v, v, cur_one

        return cur_min >= prev_max


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
