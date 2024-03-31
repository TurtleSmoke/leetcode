import pytest
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        j_min = j_max = j_bad = -1
        for i, n in enumerate(nums):
            if not minK <= n <= maxK:
                j_bad = i
            if n == minK:
                j_min = i
            if n == maxK:
                j_max = i

            res += max(0, min(j_min, j_max) - j_bad)

        return res


tests = [
    (
        ([1, 3, 5, 2, 7, 5], 1, 5),
        2,
    ),
    (
        ([7, 2, 1, 3, 5, 2, 7, 5], 1, 5),
        4,
    ),
    (
        ([1, 1, 1, 1], 1, 1),
        10,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().countSubarrays(*inputs)
    assert output == expected
