import pytest
from typing import List


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        res = 0
        current_max = float("-inf")
        for n in sorted(nums):
            if current_max < n + k:
                res += 1
                current_max = max(current_max + 1, n - k)
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
