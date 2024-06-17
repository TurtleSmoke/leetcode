import pytest


class Solution:
    def scoreOfString(self, s: str) -> int:
        score = list(map(ord, s))
        return sum(abs(s2 - s1) for s1, s2 in zip(score[:-1], score[1:]))


tests = [
    (
        ("hello",),
        13,
    ),
    (
        ("zaz",),
        50,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().scoreOfString(*inputs)
    assert output == expected
