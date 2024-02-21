import pytest
from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        return max(count, key=count.get)


tests = [
    (
        ([3, 2, 3],),
        3,
    ),
    (
        ([2, 2, 1, 1, 1, 2, 2],),
        2,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().majorityElement(*inputs)
    assert output == expected
