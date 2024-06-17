from typing import List

import pytest


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        res, cur = 0, 0
        count = {0: (1, 0)}
        for i, a in enumerate(arr):
            cur ^= a
            n, total = count.get(cur, (0, 0))
            res += i * n - total
            count[cur] = (n + 1, total + i + 1)
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
