import pytest
from typing import List


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        return 0


tests = [
    (
        ([1, 2, 1], 3, [[0, 1], [0, 2]]),
        6,
    ),
    (
        ([2, 3], 7, [[0, 1]]),
        9,
    ),
    (
        ([7, 7, 7, 7, 7, 7], 3, [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]),
        42,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().maximumValueSum(*inputs)
    assert output == expected
