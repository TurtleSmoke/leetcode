from typing import List

import pytest


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        res = [-1] * (len(nums) - k + 1)
        consecutive = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                consecutive += 1
            else:
                consecutive = 0

            if consecutive >= k - 1:
                res[i - k + 1] = nums[i]
        return res


tests = [
    (
        ([1, 2, 3, 4, 3, 2, 5], 3),
        [3, 4, -1, -1, -1],
    ),
    (
        ([2, 2, 2, 2, 2], 4),
        [-1, -1],
    ),
    (
        ([3, 2, 3, 2, 3, 2], 2),
        [-1, 3, -1, 3, -1],
    ),
    (
        ([1], 1),
        [1],
    ),
    (
        ([2, 3], 2),
        [3],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().resultsArray(*inputs)
    assert output == expected
