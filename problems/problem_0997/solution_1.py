from collections import defaultdict

import pytest
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        potential_judges = set(range(1, n + 1))
        has_trust = defaultdict(int)
        for a, b in trust:
            potential_judges.discard(a)
            has_trust[b] += 1

        for judge in potential_judges:
            if has_trust[judge] == n - 1:
                return judge

        return -1


tests = [
    (
        (2, [[1, 2]]),
        2,
    ),
    (
        (3, [[1, 3], [2, 3]]),
        3,
    ),
    (
        (3, [[1, 3], [2, 3], [3, 1]]),
        -1,
    ),
    (
        (4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]),
        3,
    ),
    (
        (3, [[1, 2], [2, 3]]),
        -1,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().findJudge(*inputs)
    assert output == expected
