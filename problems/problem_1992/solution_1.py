from typing import List

import pytest


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def dfs(i, j):
            if 0 <= i < len(land) and 0 <= j < len(land[0]) and land[i][j] == 1:
                land[i][j] = 0
                r2 = max(i, dfs(i + 1, j)[0])
                c2 = max(j, dfs(i, j + 1)[1])

                return r2, c2

            return -1, -1

        res = []
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] == 1:
                    res.append([i, j, *dfs(i, j)])

        return res


tests = [
    (
        ([[1, 0, 0], [0, 1, 1], [0, 1, 1]],),
        [[0, 0, 0, 0], [1, 1, 2, 2]],
    ),
    (
        ([[1, 1], [1, 1]],),
        [[0, 0, 1, 1]],
    ),
    (
        ([[0]],),
        [],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().findFarmland(*inputs)
    assert output == expected
