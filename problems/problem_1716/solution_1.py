import pytest


class Solution:
    def totalMoney(self, n: int) -> int:
        q, r = divmod(n, 7)
        return 28 * q + 7 * q * (q - 1) // 2 + r * (r + 1) // 2 + q * r


tests = [
    (
        (4,),
        10,
    ),
    (
        (10,),
        37,
    ),
    (
        (20,),
        96,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().totalMoney(*inputs)
    assert output == expected
