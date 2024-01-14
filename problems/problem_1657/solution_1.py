from collections import Counter

import pytest


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1, c2 = map(Counter, (word1, word2))
        return c1.keys() == c2.keys() and sorted(c1.values()) == sorted(c2.values())



tests = [
    (
        ("abc", "bca"),
        True,
    ),
    (
        ("a", "aa"),
        False,
    ),
    (
        ("cabbba", "abbccc"),
        True,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().closeStrings(*inputs)
    assert output == expected
