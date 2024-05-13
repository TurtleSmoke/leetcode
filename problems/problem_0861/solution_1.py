from typing import List

import numpy as np
import pytest


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        grid = np.asarray(grid)
        if 0 in grid.shape:
            return 0

        for i in range(len(grid)):
            if grid[i][0] == 0:
                grid[i] = 1 - grid[i]

        for j in range(1, len(grid[0])):
            if sum(grid[:, j]) < len(grid) / 2:
                grid[:, j] = 1 - grid[:, j]

        return int(np.sum([int("".join(map(str, row)), 2) for row in grid]))


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
