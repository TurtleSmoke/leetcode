from typing import List
from collections import Counter

import pytest


class Solution:
    def dividePlayers(self, skills: List[int]) -> int:
        objective = 2 * sum(skills) // len(skills)
        counter = Counter(skills)

        res = 0
        for skill, occ in counter.items():
            if occ != counter[objective - skill]:
                return -1
            res += occ * skill * (objective - skill)

        return res // 2


tests = [
    (
        ([3, 2, 5, 1, 3, 4],),
        22,
    ),
    (
        ([3, 4],),
        12,
    ),
    (
        ([1, 1, 2, 3],),
        -1,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().dividePlayers(*inputs)
    assert output == expected
