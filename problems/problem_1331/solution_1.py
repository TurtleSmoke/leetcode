from typing import List

import pytest


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {x: i + 1 for i, x in (enumerate(sorted(set(arr))))}
        return [rank[x] for x in arr]


tests = [
    (
        ([40, 10, 20, 30],),
        [4, 1, 2, 3],
    ),
    (
        ([100, 100, 100],),
        [1, 1, 1],
    ),
    (
        ([37, 12, 28, 9, 100, 56, 80, 5, 12],),
        [5, 3, 4, 2, 8, 6, 7, 1, 3],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().arrayRankTransform(*inputs)
    assert output == expected
