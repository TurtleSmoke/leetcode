import pytest


class Solution:
    def minimumLength(self, s: str) -> int:
        while len(s) > 1 and s[0] == s[-1]:
            l = next((i for i in range(len(s)) if s[i] != s[0]), len(s))
            r = next((i for i in range(len(s) - 1, -1, -1) if s[i] != s[-1]), -1)
            s = s[l : r + 1]
        return len(s)


tests = [
    (
        ("ca",),
        2,
    ),
    (
        ("cabaabac",),
        0,
    ),
    (
        ("aabccabba",),
        3,
    ),
    (
        ("bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb",),
        1,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().minimumLength(*inputs)
    assert output == expected
