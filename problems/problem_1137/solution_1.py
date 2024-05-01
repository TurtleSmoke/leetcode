import pytest


class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        for i in range(3, n + 1):
            dp[i % 3] = sum(dp)

        return dp[n % 3]


tests = [
    (
        (4,),
        4,
    ),
    (
        (25,),
        1389537,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().tribonacci(*inputs)
    assert output == expected
