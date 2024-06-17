import pytest
from collections import Counter
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = Counter(words[0])
        for word in words[1:]:
            res &= Counter(word)
        return list(res.elements())


tests = [
    (
        (["bella", "label", "roller"],),
        ["e", "l", "l"],
    ),
    (
        (["cool", "lock", "cook"],),
        ["c", "o"],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().commonChars(*inputs)
    assert sorted(output) == sorted(expected)
