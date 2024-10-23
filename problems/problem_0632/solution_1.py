import pytest
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        return []


tests = [
    (
        ([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]],),
        [20, 24],
    ),
    (
        ([[1, 2, 3], [1, 2, 3], [1, 2, 3]],),
        [1, 1],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().smallestRange(*inputs)
    assert output == expected
