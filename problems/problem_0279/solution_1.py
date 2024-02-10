import pytest


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [float("inf")] * n
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[-1]


tests = [
    (
        (12,),
        3,
    ),
    (
        (13,),
        2,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().numSquares(*inputs)
    assert output == expected
