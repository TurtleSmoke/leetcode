from typing import List
import numpy as np
import pytest


class Solution:
    def maxSatisfied(self, c: List[int], g: List[int], m: int) -> int:
        c = np.array(c)
        g = np.array(g)
        return int((c * (g ^ 1)).sum() + np.convolve(c * g, np.ones(m), mode="valid").max())


tests = [
    (
        ([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3),
        16,
    ),
    (
        ([1], [0], 1),
        1,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().maxSatisfied(*inputs)
    assert output == expected
