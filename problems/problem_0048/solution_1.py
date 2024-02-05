import pytest
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for row in range(len(matrix)):
            for col in range(row, len(matrix)):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        for row in range(len(matrix)):
            for col in range(len(matrix) // 2):
                matrix[row][col], matrix[row][len(matrix) - 1 - col] = (
                    matrix[row][len(matrix) - 1 - col],
                    matrix[row][col],
                )


tests = [
    (
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]],),
        [[7, 4, 1], [8, 5, 2], [9, 6, 3]],
    ),
    (
        ([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],),
        [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    input = inputs[0]
    Solution().rotate(input)
    assert input == expected
