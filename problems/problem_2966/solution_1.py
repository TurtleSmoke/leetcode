import pytest
from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(0, len(nums), 3):
            if nums[i + 2] - nums[i] > k:
                return []
            res.append(nums[i : i + 3])
        return res


tests = [
    (
        ([1, 3, 4, 8, 7, 9, 3, 5, 1], 2),
        [[1, 1, 3], [3, 4, 5], [7, 8, 9]],
    ),
    (
        ([2, 4, 2, 2, 5, 2], 2),
        [],
    ),
    (
        ([4, 2, 9, 8, 2, 12, 7, 12, 10, 5, 8, 5, 5, 7, 9, 2, 5, 11], 14),
        [[2, 2, 2], [4, 5, 5], [5, 5, 7], [7, 8, 8], [9, 9, 10], [11, 12, 12]],
    ),
]


# @pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    _, k = inputs
    output = Solution().divideArray(*inputs)
    for triplet in output:
        assert len(triplet) == 3, output
        assert triplet[1] - triplet[0] <= k, output
        assert triplet[2] - triplet[0] <= k, output
        assert triplet[2] - triplet[1] <= k, output
    assert len(output) == len(expected), output
