from typing import List
import pytest


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, word, used):
            if word == "":
                return True
            if (i, j) in used:
                return False
            used.add((i, j))
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and (board[i][j] == word[0]):
                return (
                    dfs(i + 1, j, word[1:], used.copy())
                    or dfs(i - 1, j, word[1:], used.copy())
                    or dfs(i, j + 1, word[1:], used.copy())
                    or dfs(i, j - 1, word[1:], used.copy())
                )
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, word, set()):
                    return True
        return False


tests = [
    (
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"),
        True,
    ),
    (
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"),
        True,
    ),
    (
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"),
        False,
    ),
    (
        ([["a", "b"], ["c", "d"]], "cdba"),
        True,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().exist(*inputs)
    assert output == expected
