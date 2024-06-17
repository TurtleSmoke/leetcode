import pytest


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        it = iter(s)
        for i, c in enumerate(t):
            if c not in it:
                return len(t) - i

        return 0


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
