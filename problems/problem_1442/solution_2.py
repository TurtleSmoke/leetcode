from functools import reduce
from typing import List

import pytest


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        arr.insert(0, 0)
        arr = [reduce(lambda x, y: x ^ y, arr[:i]) for i in range(1, len(arr) + 1)]
        res = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] == arr[j]:
                    res += j - i - 1

        return res


tests = [
    (
        ([2, 3, 1, 6, 7],),
        4,
    ),
    (
        ([1, 1, 1, 1, 1],),
        10,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().countTriplets(*inputs)
    assert output == expected
