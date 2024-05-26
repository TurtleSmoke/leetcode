import pytest


class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 10**9 + 7
        a, b, d = 1, 1, 1
        c, e, f = 0, 0, 0

        for _ in range(n - 1):
            a, b, c, d, e, f = (a + b + c) % mod, a, b, (a + b + c + d + e + f) % mod, d, e

        return (a + b + c + d + e + f) % mod


tests = [
    (
        (1,),
        3,
    ),
    (
        (2,),
        8,
    ),
    (
        (3,),
        19,
    ),
    (
        (4,),
        43,
    ),
    (
        (5,),
        94,
    ),
    (
        (10101,),
        183236316,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().checkRecord(*inputs)
    assert output == expected
