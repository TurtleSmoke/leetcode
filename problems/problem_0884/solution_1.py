import pytest
from collections import Counter
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        cache = Counter(s1.split() + s2.split())
        return [k for k, v in cache.items() if v == 1]


tests = [
    (
        ("this apple is sweet", "this apple is sour"),
        ["sweet", "sour"],
    ),
    (
        ("apple apple", "banana"),
        ["banana"],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().uncommonFromSentences(*inputs)
    assert sorted(output) == sorted(expected)
