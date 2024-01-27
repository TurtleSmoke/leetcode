import pytest


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        if n < 2 or k < 0 or k > n * (n - 1) // 2:
            return 0

        dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
            for j in range(1, min(k, i * (i - 1) // 2) + 1):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
                if j >= i:
                    dp[i][j] -= dp[i - 1][j - i]

        return dp[-1][-1] % 10**9


tests = [
    (
        (3, 0),
        1,
    ),
    (
        (3, 1),
        2,
    ),
    ((5, 5), 22),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().kInversePairs(*inputs)
    assert output == expected
