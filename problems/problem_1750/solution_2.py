import pytest


class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1
        while l < r and s[l] == s[r]:
            c = s[l]
            while l <= r and s[l] == c:
                l += 1
            while l < r and s[r] == c:
                r -= 1

        return r - l + 1


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
