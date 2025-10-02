import pytest


class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        while numBottles >= numExchange:
            numBottles += 1 - numExchange
            numExchange += 1
            res += 1
        return res


tests = [
    (
        (13, 6),
        15,
    ),
    (
        (10, 3),
        13,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().maxBottlesDrunk(*inputs)
    assert output == expected
