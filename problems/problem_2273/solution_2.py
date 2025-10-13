import pytest
from typing import List
from itertools import groupby


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        return [next(g) for _, g in groupby(words, sorted)]


tests = [
    (
        (["abba", "baba", "bbaa", "cd", "cd"],),
        ["abba", "cd"],
    ),
    (
        (["a", "b", "c", "d", "e"],),
        ["a", "b", "c", "d", "e"],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().removeAnagrams(*inputs)
    assert output == expected
