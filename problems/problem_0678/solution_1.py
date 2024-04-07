from functools import cache
import pytest


class Solution:
    def checkValidString(self, s: str) -> bool:
        @cache
        def dfs(i, open):
            if open < 0:
                return False
            if i >= len(s):
                return open == 0

            if s[i] == ")":
                return dfs(i + 1, open - 1)
            if s[i] == "(":
                return dfs(i + 1, open + 1)
            if s[i] == "*":
                return dfs(i + 1, open + 1) or dfs(i + 1, open) or dfs(i + 1, open - 1)

        return dfs(0, 0)


tests = [
    (
        ("()",),
        True,
    ),
    (
        ("(*)",),
        True,
    ),
    (
        ("(*))",),
        True,
    ),
    (
        ("(",),
        False,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().checkValidString(*inputs)
    assert output == expected
