import pytest
from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        return sum(all(c in allowed for c in word) for word in words)


tests = [
    (
        ("ab", ["ad", "bd", "aaab", "baa", "badab"]),
        2,
    ),
    (
        ("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"]),
        7,
    ),
    (
        ("cad", ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]),
        4,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().countConsistentStrings(*inputs)
    assert output == expected
