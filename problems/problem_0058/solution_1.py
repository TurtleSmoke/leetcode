import pytest


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


tests = [
    (
        ("Hello World",),
        5,
    ),
    (
        ("   fly me   to   the moon  ",),
        4,
    ),
    (
        ("luffy is still joyboy",),
        6,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().lengthOfLastWord(*inputs)
    assert output == expected
