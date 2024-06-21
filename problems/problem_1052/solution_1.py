from typing import List

import pytest


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        tmp = sum(grumpy[i] * customers[i] for i in range(minutes))
        non_satisfied = tmp
        satisfied = 0

        for i in range(len(customers) - minutes):
            satisfied += customers[i] * (grumpy[i] ^ 1)
            tmp += -grumpy[i] * customers[i] + grumpy[i + minutes] * customers[i + minutes]
            non_satisfied = max(non_satisfied, tmp)

        for i in range(len(customers) - minutes, len(customers)):
            satisfied += customers[i] * (grumpy[i] ^ 1)

        return satisfied + non_satisfied


tests = [
    (
        ([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3),
        16,
    ),
    (
        ([1], [0], 1),
        1,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().maxSatisfied(*inputs)
    assert output == expected
