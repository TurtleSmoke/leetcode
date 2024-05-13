from typing import List

import pytest


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        mapping = ["Gold Medal", "Silver Medal", "Bronze Medal"] + list(map(str, range(4, len(score) + 1)))
        return [mapping[sorted_score.index(s)] for s in score]


tests = [
    (
        ([5, 4, 3, 2, 1],),
        ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"],
    ),
    (
        ([10, 3, 8, 9, 4],),
        ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().findRelativeRanks(*inputs)
    assert output == expected
