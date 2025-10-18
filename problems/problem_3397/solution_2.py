import pytest
from typing import List
from collections import Counter


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        next_available = float("-inf")
        res = 0

        for num in sorted(counter.keys()):
            start_pos = max(next_available, num - k)
            placeable = min(counter[num], num + k - start_pos + 1)
            next_available = start_pos + placeable
            res += placeable

        return res


tests = [
    (
        ([1, 2, 2, 3, 3, 4], 2),
        6,
    ),
    (
        ([4, 4, 4, 4], 1),
        3,
    ),
    (
        ([8, 7, 8, 7, 10], 1),
        5,
    ),
    (
        ([10, 10, 10], 0),
        1,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().maxDistinctElements(*inputs)
    assert output == expected
