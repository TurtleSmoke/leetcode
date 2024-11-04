import pytest


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            if s[i:] + s[:i] == goal:
                return True

        return False


tests = [
    (
        ("abcde", "cdeab"),
        True,
    ),
    (
        ("abcde", "abced"),
        False,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().rotateString(*inputs)
    assert output == expected
