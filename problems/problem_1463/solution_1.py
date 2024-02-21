import itertools
from typing import List
from functools import cache

import pytest


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @cache
        def dp(row, p1, p2):
            if row == m:
                return 0

            res = max(
                dp(row + 1, np1, np2)
                for np1, np2 in itertools.product(range(p1 - 1, p1 + 2), range(p2 - 1, p2 + 2))
                if 0 <= np1 <= np2 < n
            )
            return res + (grid[row][p1] if p1 == p2 else grid[row][p1] + grid[row][p2])

        return dp(0, 0, n - 1)


tests = [
    (
        ([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]],),
        24,
    ),
    (
        (
            [
                [1, 0, 0, 0, 0, 0, 1],
                [2, 0, 0, 0, 0, 3, 0],
                [2, 0, 9, 0, 0, 0, 0],
                [0, 3, 0, 5, 4, 0, 0],
                [1, 0, 2, 3, 0, 0, 6],
            ],
        ),
        28,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().cherryPickup(*inputs)
    assert output == expected
