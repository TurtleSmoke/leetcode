import pytest


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        dp = [[float("inf")] * (k + 1) for _ in range(len(s) + 1)]
        dp[0][0] = 0

        for j in range(k + 1):
            for i in range(1, len(s) + 1):
                occ, removed = 0, 0
                for l in range(i, 0, -1):
                    if s[l - 1] == s[i - 1]:
                        occ += 1

                    removed = j + l - i + occ - 1
                    if removed >= 0:
                        dp[i][j] = min(
                            dp[i][j], dp[l - 1][removed] + 1 + int(occ >= 100) + int(occ >= 10) + int(occ >= 2)
                        )

                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])

        return int(dp[-1][-1])


tests = [
    (
        ("aaab", 1),
        2,
    ),
    (
        ("aaabcccd", 2),
        4,
    ),
    (
        ("aabbaa", 2),
        2,
    ),
    (
        ("aaaaaaaaaaa", 0),
        3,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().getLengthOfOptimalCompression(*inputs)
    assert output == expected
