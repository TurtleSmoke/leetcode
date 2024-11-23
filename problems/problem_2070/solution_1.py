import bisect
from typing import List

import pytest


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items = sorted(items + [[0, 0]], key=lambda x: x[0])
        for i in range(len(items) - 1):
            items[i + 1][1] = max(items[i][1], items[i + 1][1])
        return [items[bisect.bisect(items, [q + 1]) - 1][1] for q in queries]


tests = [
    (
        ([[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]], [1, 2, 3, 4, 5, 6]),
        [2, 4, 5, 5, 6, 6],
    ),
    (
        ([[1, 2], [1, 2], [1, 3], [1, 4]], [1]),
        [4],
    ),
    (
        ([[10, 1000]], [5]),
        [0],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().maximumBeauty(*inputs)
    assert output == expected
