from typing import List

import pytest


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        return any(arr[i] % 2 == 1 and arr[i + 1] % 2 == 1 and arr[i + 2] % 2 == 1 for i in range(len(arr) - 2))


tests = [
    (
        ([2, 6, 4, 1],),
        False,
    ),
    (
        ([1, 2, 34, 3, 4, 5, 7, 23, 12],),
        True,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().threeConsecutiveOdds(*inputs)
    assert output == expected
