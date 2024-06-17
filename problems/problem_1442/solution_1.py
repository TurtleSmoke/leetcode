import pytest
from functools import reduce
from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        res = []
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                for k in range(j, len(arr)):
                    if reduce(lambda x, y: x ^ y, arr[i:j]) == reduce(lambda x, y: x ^ y, arr[j : k + 1]):
                        res.append((i, j, k))

        return len(res)


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
