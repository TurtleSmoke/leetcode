import pytest
from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list((Counter(nums1) & Counter(nums2)).elements())


tests = [
    (
        ([1, 2, 2, 1], [2, 2]),
        [2, 2],
    ),
    (
        ([4, 9, 5], [9, 4, 9, 8, 4]),
        [4, 9],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().intersect(*inputs)
    assert output == expected
