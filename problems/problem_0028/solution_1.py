import pytest


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i

        return -1


tests = [
    (
        ("sadbutsad", "sad"),
        0,
    ),
    (
        ("leetcode", "leeto"),
        -1,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().strStr(*inputs)
    assert output == expected
