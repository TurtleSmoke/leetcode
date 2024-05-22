from functools import cache
from typing import List

import pytest


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        @cache
        def dfs(s):
            if not s:
                return [[]]

            res = []
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    for suf in dfs(s[i:]):
                        res.append([s[:i]] + suf)

            return res

        return dfs(s)


tests = [
    (
        ("aab",),
        [["a", "a", "b"], ["aa", "b"]],
    ),
    (
        ("a",),
        [["a"]],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().partition(*inputs)
    assert sorted(output) == sorted(expected)
