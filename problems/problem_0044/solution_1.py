import pytest


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [True] + [False] * len(p)

        for i in range(1, len(p) + 1):
            if p[i - 1] == "*":
                dp[i] = dp[i - 1]
            else:
                break

        for i in range(1, len(s) + 1):
            prev, dp[0] = dp[0], False

            for j in range(1, len(p) + 1):
                if p[j - 1] == "?" or p[j - 1] == s[i - 1]:
                    dp[j], prev = prev, dp[j]
                elif p[j - 1] == "*":
                    dp[j], prev = dp[j] or dp[j - 1], dp[j]
                else:
                    dp[j], prev = False, dp[j]

        return dp[-1]


tests = [
    (
        ("aa", "a"),
        False,
    ),
    (
        ("aa", "*"),
        True,
    ),
    (
        ("cb", "?a"),
        False,
    ),
    (
        ("", "?"),
        False,
    ),
    (
        ("", "*"),
        True,
    ),
    (
        ("ac", "a*c"),
        True,
    ),
    (
        ("abbc", "a*bc"),
        True,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().isMatch(*inputs)
    assert output == expected
