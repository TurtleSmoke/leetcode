import pytest
from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        res = 0
        mini = 0
        for n in sorted(nums):
            res += max(mini - n, 0)
            mini = max(mini + 1, n + 1)
        return res


tests = [
    (
        ([1, 2, 2],),
        1,
    ),
    (
        ([3, 2, 1, 2, 1, 7],),
        6,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().minIncrementForUnique(*inputs)
    assert output == expected
