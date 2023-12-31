import pytest
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        remove_dot = lambda x: [c for c in x if c != "."]
        is_valid = lambda x: len(x) == len(set(x))

        for i in range(9):
            if not is_valid(remove_dot(board[i])):
                return False
            if not is_valid(remove_dot([board[j][i] for j in range(9)])):
                return False

        for i in range(3):
            for j in range(3):
                if not is_valid(remove_dot([board[i * 3 + k][j * 3 + l] for k in range(3) for l in range(3)])):
                    return False

        return True


tests = [
    (
        (
            [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ],
        ),
        True,
    ),
    (
        (
            [
                ["8", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ],
        ),
        False,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().isValidSudoku(*inputs)
    assert output == expected
