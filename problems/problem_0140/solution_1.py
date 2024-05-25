import pytest
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def dfs(s):
            if not s:
                return []

            res = []
            for word in wordDict:
                if not s.startswith(word):
                    continue

                if len(word) == len(s):
                    res.append(word)
                else:
                    sub_res = dfs(s[len(word) :])
                    for sr in sub_res:
                        res.append(word + " " + sr)
            return res

        return dfs(s)


tests = [
    (
        ("catsanddog", ["cat", "cats", "and", "sand", "dog"]),
        ["cats and dog", "cat sand dog"],
    ),
    (
        ("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]),
        ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"],
    ),
    (
        ("catsandog", ["cats", "dog", "sand", "and", "cat"]),
        [],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().wordBreak(*inputs)
    assert sorted(output) == sorted(expected)
