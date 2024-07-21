from typing import List

import pytest


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        res = [[0 for _ in range(len(colSum))] for _ in range(len(rowSum))]
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                res[i][j] = min(colSum[j], rowSum[i])
                colSum[j] -= res[i][j]
                rowSum[i] -= res[i][j]

        return res


tests = [
    (
        ([3, 8], [4, 7]),
        [[3, 0], [1, 7]],
    ),
    (
        ([5, 7, 10], [8, 6, 8]),
        [[0, 5, 0], [6, 1, 0], [2, 0, 8]],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    import numpy as np

    rowSum, colSum = inputs
    output = np.asarray(Solution().restoreMatrix(rowSum[:], colSum[:]))
    assert np.all(output.sum(axis=0) == colSum)
    assert np.all(output.sum(axis=1) == rowSum)
