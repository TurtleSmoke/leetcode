import pytest
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        return sum(expected[i] != heights[i] for i in range(len(heights)))


tests = [
    (
        ([1, 1, 4, 2, 1, 3],),
        3,
    ),
    (
        ([5, 1, 2, 3, 4],),
        5,
    ),
    (
        ([1, 2, 3, 4, 5],),
        0,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().heightChecker(*inputs)
    assert output == expected
