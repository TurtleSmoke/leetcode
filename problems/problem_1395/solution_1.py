from typing import List

import pytest


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0
        for i in range(1, len(rating) - 1):
            less = [0, 0]
            greater = [0, 0]
            for j in range(len(rating)):
                if rating[i] > rating[j]:
                    less[i > j] += 1
                if rating[i] < rating[j]:
                    greater[i > j] += 1
            res += less[0] * greater[1] + greater[0] * less[1]

        return res


tests = [
    (
        ([2, 5, 3, 4, 1],),
        3,
    ),
    (
        ([2, 1, 3],),
        0,
    ),
    (
        ([1, 2, 3, 4],),
        4,
    ),
    (
        ([2, 5, 3, 4, 1, 6, 0],),
        13,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().numTeams(*inputs)
    assert output == expected
