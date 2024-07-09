import pytest
from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        res = 0
        ending = 0
        for arrival, time in customers:
            ending = max(ending, arrival) + time
            res += ending - arrival
        return res / len(customers)


tests = [
    (
        ([[1, 2], [2, 5], [4, 3]],),
        5.00000,
    ),
    (
        ([[5, 2], [5, 4], [10, 3], [20, 1]],),
        3.25000,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().averageWaitingTime(*inputs)
    assert output == expected
