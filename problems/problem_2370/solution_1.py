import pytest


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 128
        for c in s:
            i = ord(c)
            dp[i] = max(dp[i - k : i + k + 1]) + 1
        return max(dp)


tests = [
    (
        ("acfgbd", 2),
        4,
    ),
    (
        ("abcd", 3),
        4,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().longestIdealString(*inputs)
    assert output == expected
