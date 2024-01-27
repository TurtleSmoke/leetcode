from functools import cache

import pytest


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @cache
        def dfs(row, col, remaining_moves):
            if not (0 <= row < m and 0 <= col < n):
                return 1
            if remaining_moves == 0:
                return 0

            return sum(
                dfs(row + dr, col + dc, remaining_moves - 1) for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1))
            ) % (10**9 + 7)

        return dfs(startRow, startColumn, maxMove)


tests = [
    (
        (2, 2, 2, 0, 0),
        6,
    ),
    (
        (1, 3, 3, 0, 1),
        12,
    ),
    (
        (8, 50, 23, 5, 26),
        914783380,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().findPaths(*inputs)
    assert output == expected
