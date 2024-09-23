import functools
from typing import List

import pytest


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        @functools.cache
        def dfs(s):
            if not s:
                return 0

            res = float("inf")
            for i in range(len(s)):
                substr = s[: i + 1]
                if substr in dictionary:
                    res = min(res, dfs(s[i + 1 :]))
                else:
                    res = min(res, len(substr) + dfs(s[i + 1 :]))
            return res

        dictionary = set(dictionary)
        return dfs(s)


tests = [
    (
        ("leetscode", ["leet", "code", "leetcode"]),
        1,
    ),
    (
        ("sayhelloworld", ["hello", "world"]),
        3,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().minExtraChar(*inputs)
    assert output == expected
