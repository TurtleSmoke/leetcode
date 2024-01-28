import collections

import pytest
from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        for row in matrix:
            for i in range(1, len(row)):
                row[i] += row[i - 1]

        res = 0
        for i in range(len(matrix[0])):
            for j in range(i, len(matrix[0])):
                c = collections.defaultdict(int)
                cur, c[0] = 0, 1
                for k in range(len(matrix)):
                    cur += matrix[k][j] - (matrix[k][i - 1] if i > 0 else 0)
                    res += c[cur - target]
                    c[cur] += 1

        return res


tests = [
    (
        ([[0, 1, 0], [1, 1, 1], [0, 1, 0]], 0),
        4,
    ),
    (
        ([[1, -1], [-1, 1]], 0),
        5,
    ),
    (
        ([[904]], 0),
        0,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().numSubmatrixSumTarget(*inputs)
    assert output == expected
