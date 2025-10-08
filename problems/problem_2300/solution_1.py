import pytest
from bisect import bisect_left
from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        return [len(potions) - bisect_left(potions, (success + a - 1) // a) for a in spells]


tests = [
    (
        ([5, 1, 3], [1, 2, 3, 4, 5], 7),
        [4, 0, 3],
    ),
    (
        ([3, 1, 2], [8, 5, 8], 16),
        [2, 0, 2],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().successfulPairs(*inputs)
    assert output == expected
