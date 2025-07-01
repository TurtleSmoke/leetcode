import pytest


class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = 1
        for i in range(1, len(word)):
            if word[i - 1] == word[i]:
                res += 1
        return res


tests = [
    (
        ("abbcccc",),
        5,
    ),
    (
        ("abcd",),
        1,
    ),
    (
        ("aaaa",),
        4,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().possibleStringCount(*inputs)
    assert output == expected
