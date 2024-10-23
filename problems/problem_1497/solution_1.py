from typing import List

import pytest


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder = [0] * k
        for num in arr:
            remainder[num % k] += 1

        if remainder[0] % 2 != 0:
            return False

        for i in range(1, k // 2 + 1):
            if remainder[i] != remainder[k - i]:
                return False

        return True


tests = [
    (
        ([1, 2, 3, 4, 5, 10, 6, 7, 8, 9], 5),
        True,
    ),
    (
        ([1, 2, 3, 4, 5, 6], 7),
        True,
    ),
    (
        ([1, 2, 3, 4, 5, 6], 10),
        False,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().canArrange(*inputs)
    assert output == expected
