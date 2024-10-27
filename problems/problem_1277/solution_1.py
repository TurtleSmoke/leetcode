import pytest
from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i and j and matrix[i][j]:
                    matrix[i][j] += min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1])
                res += matrix[i][j]
        return res


tests = [
    (
        ([[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]],),
        15,
    ),
    (
        ([[1, 0, 1], [1, 1, 0], [1, 1, 0]],),
        7,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().countSquares(*inputs)
    assert output == expected
