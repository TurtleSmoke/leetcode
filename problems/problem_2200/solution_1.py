import pytest
from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        idx_occ = [i for i, v in enumerate(nums) if v == key]
        return list(sorted(set(n for idx in idx_occ for n in range(max(0, idx - k), min(len(nums), idx + k + 1)))))


tests = [
    (
        ([3, 4, 9, 1, 3, 9, 5], 9, 1),
        [1, 2, 3, 4, 5, 6],
    ),
    (
        ([2, 2, 2, 2, 2], 2, 2),
        [0, 1, 2, 3, 4],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().findKDistantIndices(*inputs)
    assert output == expected
