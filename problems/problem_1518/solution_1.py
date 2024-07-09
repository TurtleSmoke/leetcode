import pytest


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        while numBottles >= numExchange:
            res += numBottles // numExchange
            numBottles = numBottles % numExchange + numBottles // numExchange

        return res


tests = [
    (
        (9, 3),
        13,
    ),
    (
        (15, 4),
        19,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().numWaterBottles(*inputs)
    assert output == expected
