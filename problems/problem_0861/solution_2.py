from typing import List

import pytest


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = (1 << n - 1) * m
        for j in range(1, n):
            cur = sum(grid[i][j] == grid[i][0] for i in range(m))
            res += max(cur, m - cur) * (1 << n - j - 1)
        return res


tests = [
    (
        ([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]],),
        39,
    ),
    (
        ([[0]],),
        1,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().matrixScore(*inputs)
    assert output == expected
