import pytest


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        first = {0: -1}
        res = idx = 0
        for i, c in enumerate(s):
            idx ^= 1 << ("aeiou".find(c) + 1) >> 1
            first.setdefault(idx, i)
            res = max(res, i - first[idx])
        return res


tests = [
    (
        ("eleetminicoworoep",),
        13,
    ),
    (
        ("leetcodeisgreat",),
        5,
    ),
    (
        ("bcbcbc",),
        6,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().findTheLongestSubstring(*inputs)
    assert output == expected
