import pytest


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        for i, c in enumerate(s, 1):
            dp[i] = dp[i - 1] ^ ((1 << "aeiou".find(c)) if c in "aeiou" else 0)
        first = {}
        res = 0
        for i, x in enumerate(dp):
            if x not in first:
                first[x] = i
            res = max(res, i - first[x])

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
