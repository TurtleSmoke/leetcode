from collections import defaultdict
import pytest
from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        res = defaultdict(int)
        rows = [int("".join(map(str, row)), 2) for row in matrix]
        mask = (1 << len(matrix[0])) - 1
        for row in rows:
            res[row if row & 1 else ~row & mask] += 1
        return max(res.values())


tests = [
    (
        ([[0, 1], [1, 1]],),
        1,
    ),
    (
        ([[0, 1], [1, 0]],),
        2,
    ),
    (
        ([[0, 0, 0], [0, 0, 1], [1, 1, 0]],),
        2,
    ),
    (
        ([[0], [1], [0], [0], [1], [1], [1], [1], [0], [1]],),
        10,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().maxEqualRowsAfterFlips(*inputs)
    assert output == expected
