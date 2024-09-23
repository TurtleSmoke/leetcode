import pytest


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        s_reversed = s[::-1]
        for i in range(len(s_reversed)):
            if s.startswith(s_reversed[i:]):
                return s_reversed[:i] + s

        return s_reversed + s


tests = [
    (
        ("aacecaaa",),
        "aaacecaaa",
    ),
    (
        ("abcd",),
        "dcbabcd",
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().shortestPalindrome(*inputs)
    assert output == expected
