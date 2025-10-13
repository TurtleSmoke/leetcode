import pytest
from typing import List
from collections import Counter


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        counter = [Counter(word) for word in words]
        result = [words[0]]
        for i in range(1, len(words)):
            if counter[i] != counter[i - 1]:
                result.append(words[i])
        return result


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
