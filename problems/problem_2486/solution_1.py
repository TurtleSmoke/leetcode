import pytest


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        for j in range(len(s)):
            if s[j] == t[i]:
                i += 1
                if i >= len(t):
                    return 0

        return len(t) - i


tests = [
    (
        ("coaching", "coding"),
        4,
    ),
    (
        ("abcde", "a"),
        0,
    ),
    (
        ("z", "abcde"),
        5,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().appendCharacters(*inputs)
    assert output == expected
