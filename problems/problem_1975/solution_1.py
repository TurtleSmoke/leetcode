import pytest
from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        parity = True
        mini = abs(matrix[0][0])
        res = 0
        for row in matrix:
            for v in row:
                if v < 0:
                    parity = not parity
                mini = min(mini, abs(v))
                res += abs(v)
        return res if parity else res - 2 * mini


tests = [
    (
        ([[1, -1], [-1, 1]],),
        4,
    ),
    (
        ([[1, 2, 3], [-1, -2, -3], [1, 2, 3]],),
        16,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().maxMatrixSum(*inputs)
    assert output == expected
