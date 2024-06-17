import pytest
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            s[i], s[-i - 1] = s[-i - 1], s[i]


tests = [
    (
        (["h", "e", "l", "l", "o"],),
        ["o", "l", "l", "e", "h"],
    ),
    (
        (["H", "a", "n", "n", "a", "h"],),
        ["h", "a", "n", "n", "a", "H"],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    input = inputs[0]
    Solution().reverseString(input)
    assert input == expected
