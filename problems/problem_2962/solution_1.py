import pytest
from typing import List
from collections import defaultdict


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # Get dict of idx per value
        idx_per_value = defaultdict(list)
        for i, n in enumerate(nums):
            idx_per_value[n].append(i)

        query = max(idx_per_value.keys())
        indexes = idx_per_value[query] + [len(nums)]

        res = 0
        for i in range(len(indexes) - k):
            res += (indexes[i] + 1) * (indexes[i + k] - indexes[i + k - 1])

        return res


tests = [
    (
        ([1, 3, 2, 3, 3], 2),
        6,
    ),
    (
        ([1, 3, 2, 3, 2, 3], 2),
        8,
    ),
    (
        ([1, 3, 3, 2], 2),
        4,
    ),
    (
        ([1, 3, 2, 3, 3, 1], 2),
        10,
    ),
    (
        ([1, 4, 2, 1], 3),
        0,
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
