from typing import List
import pytest


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        union_find = {}

        def find(x):
            if x != union_find[x]:
                union_find[x] = find(union_find[x])
            return union_find[x]

        def union(x, y):
            union_find.setdefault(x, x)
            union_find.setdefault(y, y)
            union_find[find(x)] = find(y)

        for x, y in stones:
            union(x, ~y)

        return len(stones) - len({find(x) for x in union_find})


tests = [
    (
        ([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]],),
        5,
    ),
    (
        ([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]],),
        3,
    ),
    (
        ([[0, 0]],),
        0,
    ),
    (
        ([[0, 1], [1, 0], [1, 1]],),
        2,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().removeStones(*inputs)
    assert output == expected
