import pytest
from typing import List
import numpy as np


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        matrix = np.asarray(matrix)

        while matrix.size > 0:
            res.extend(matrix[0])
            matrix = np.rot90(matrix[1:])

        return res


tests = [
    (
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]],),
        [1, 2, 3, 6, 9, 8, 7, 4, 5],
    ),
    (
        ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],),
        [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().spiralOrder(*inputs)
    assert output == expected
