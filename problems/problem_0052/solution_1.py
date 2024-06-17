import pytest


class Solution:
    def totalNQueens(self, n: int) -> int:
        def dfs(c, rows):
            if c == n:
                return 1

            res = 0
            for r in range(n):
                if all(r != x and abs(r - x) != abs(c - y) for y, x in enumerate(rows)):
                    res += dfs(c + 1, rows + [r])

            return res

        return dfs(0, [])


tests = [
    (
        (4,),
        2,
    ),
    (
        (1,),
        1,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().totalNQueens(*inputs)
    assert output == expected
