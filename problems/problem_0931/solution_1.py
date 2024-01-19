from typing import List

import pytest


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for i in range(1, len(matrix)):
            matrix[i][0] += min(matrix[i - 1][0], matrix[i - 1][1])
            for j in range(1, len(matrix[i]) - 1):
                matrix[i][j] += min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i - 1][j + 1])
            matrix[i][-1] += min(matrix[i - 1][-1], matrix[i - 1][-2])

        return min(matrix[-1])


tests = [
    (
        ([[2, 1, 3], [6, 5, 4], [7, 8, 9]],),
        13,
    ),
    (
        ([[-19, 57], [-40, -5]],),
        -59,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().minFallingPathSum(*inputs)
    assert output == expected
