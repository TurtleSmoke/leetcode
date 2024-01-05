import pytest
from typing import List
from collections import Counter


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        occ = list(Counter(nums).values())
        if 1 in occ:
            return -1

        return sum(((o + 2) // 3 for o in occ))


tests = [
    (
        ([2, 3, 3, 2, 2, 4, 2, 3, 4],),
        4,
    ),
    (
        ([2, 1, 2, 2, 3, 3],),
        -1,
    ),
    (
        ([14, 12, 14, 14, 12, 14, 14, 12, 12, 12, 12, 14, 14, 12, 14, 14, 14, 12, 12],),
        7,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().minOperations(*inputs)
    assert output == expected
