import pytest


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        count_vowels = lambda s: sum(c in "aeiouAEIOU" for c in s)
        return count_vowels(s[: len(s) // 2]) == count_vowels(s[len(s) // 2 :])


tests = [
    (
        ("book",),
        True,
    ),
    (
        ("textbook",),
        False,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().halvesAreAlike(*inputs)
    assert output == expected
