from typing import List

import numpy as np
import pytest
from scipy.ndimage import maximum_filter


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        return maximum_filter(np.array(grid), size=3, mode="constant", cval=0)[1:-1, 1:-1].tolist()


tests = [
    (
        ([[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]],),
        [[9, 9], [8, 6]],
    ),
    (
        ([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]],),
        [[2, 2, 2], [2, 2, 2], [2, 2, 2]],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().largestLocal(*inputs)
    assert output == expected
