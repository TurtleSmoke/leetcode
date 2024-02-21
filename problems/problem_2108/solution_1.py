import pytest
from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word

        return ""


tests = [
    (
        (["abc", "car", "ada", "racecar", "cool"],),
        "ada",
    ),
    (
        (["notapalindrome", "racecar"],),
        "racecar",
    ),
    (
        (["def", "ghi"],),
        "",
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().firstPalindrome(*inputs)
    assert output == expected
