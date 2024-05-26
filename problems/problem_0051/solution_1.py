from typing import List

import pytest


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(i, queens):
            if n == i:
                return [queens]

            res = []
            for j in range(n):
                if all(j != qj and abs(i - qi) != abs(j - qj) for qi, qj in queens):
                    res += dfs(i + 1, queens | {(i, j)})

            return res

        boards = dfs(0, set())
        return [["".join("Q" if (i, j) in queens else "." for j in range(n)) for i in range(n)] for queens in boards]


tests = [
    (
        (4,),
        [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]],
    ),
    (
        (3,),
        [],
    ),
    (
        (1,),
        [["Q"]],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().solveNQueens(*inputs)
    assert output == expected
