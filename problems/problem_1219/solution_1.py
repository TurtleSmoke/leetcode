from typing import List

import pytest


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(i, j, gold):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] != 0:
                curr_gold, grid[i][j] = grid[i][j], 0
                gold = max(dfs(x, y, gold + curr_gold) for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)))
                grid[i][j] = curr_gold
            return gold

        return max(dfs(i, j, 0) for i in range(len(grid)) for j in range(len(grid[0])))


tests = [
    (
        ([[0, 6, 0], [5, 8, 7], [0, 9, 0]],),
        24,
    ),
    (
        ([[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]],),
        28,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().getMaximumGold(*inputs)
    assert output == expected
