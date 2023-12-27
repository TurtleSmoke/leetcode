import pytest
from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        colors += " "
        max_cost = 0
        cost = 0
        for i in range(len(colors) - 1):
            if colors[i] == colors[i + 1]:
                cost += neededTime[i]
                max_cost = max(max_cost, neededTime[i])
            elif max_cost > 0:
                cost += neededTime[i] - max(max_cost, neededTime[i])
                max_cost = 0

        return cost


tests = [
    (
        ("abaac", [1, 2, 3, 4, 5]),
        3,
    ),
    (
        ("abc", [1, 2, 3]),
        0,
    ),
    (
        ("aabaa", [1, 2, 3, 4, 1]),
        2,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().minCost(*inputs)
    assert output == expected
