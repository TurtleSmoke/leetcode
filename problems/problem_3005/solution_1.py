from collections import Counter
from typing import List

import pytest


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_freq = max(freq.values())
        return max_freq * sum(f == max_freq for f in freq.values())


tests = [
    (
        ([1, 2, 2, 3, 1, 4],),
        4,
    ),
    (
        ([1, 2, 3, 4, 5],),
        5,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().maxFrequencyElements(*inputs)
    assert output == expected
