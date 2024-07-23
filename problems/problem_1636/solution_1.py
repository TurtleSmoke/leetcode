import pytest
from collections import Counter
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        occ = Counter(nums)
        return sorted(nums, key=lambda x: (occ[x], -x))


tests = [
    (
        ([1, 1, 2, 2, 2, 3],),
        [3, 1, 1, 2, 2, 2],
    ),
    (
        ([2, 3, 1, 3, 2],),
        [1, 3, 3, 2, 2],
    ),
    (
        ([-1, 1, -6, 4, 5, -6, 1, 4, 1],),
        [5, -1, 4, 4, -6, -6, 1, 1, 1],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().frequencySort(*inputs)
    assert output == expected
