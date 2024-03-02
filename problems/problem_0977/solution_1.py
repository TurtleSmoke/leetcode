import pytest
from typing import List
import bisect


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([n**2 for n in nums])


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
