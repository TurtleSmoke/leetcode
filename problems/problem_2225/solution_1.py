import pytest
from typing import List
from collections import Counter


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = {match[0] for match in matches}
        losers = Counter(match[1] for match in matches)
        return [
            list(sorted(winners - losers.keys())),
            list(sorted(loser for loser, count in losers.items() if count == 1)),
        ]


tests = [
    (
        ([[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]],),
        [[1, 2, 10], [4, 5, 7, 8]],
    ),
    (
        ([[2, 3], [1, 3], [5, 4], [6, 4]],),
        [[1, 2, 5, 6], []],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().findWinners(*inputs)
    assert output == expected
