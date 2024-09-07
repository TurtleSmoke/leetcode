import pytest
from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sum_n = mean * (n + len(rolls)) - sum(rolls)
        if sum_n > n * 6 or sum_n < n:
            return []

        res = [0] * n
        for i, v in enumerate(range(n, 0, -1)):
            res[i] = int(sum_n / v)
            sum_n -= int(sum_n / v)

        return res


tests = [
    (
        ([3, 2, 4, 3], 4, 2),
        [6, 6],
    ),
    (
        ([1, 5, 6], 3, 4),
        [2, 3, 2, 2],
    ),
    (
        ([1, 2, 3, 4], 6, 4),
        [],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().missingRolls(*inputs)
    assert all(x != 0 for x in output) and sum(output) == sum(expected)
