import pytest
from typing import List
from collections import Counter


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        return all(c % len(words) == 0 for c in Counter("".join(words)).values())


tests = [
    (
        (["abc", "aabc", "bc"],),
        True,
    ),
    (
        (["ab", "a"],),
        False,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().makeEqual(*inputs)
    assert output == expected
