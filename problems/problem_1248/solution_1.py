from typing import List

import pytest


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        left = 0
        sub_res = 0

        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                k -= 1
                sub_res = 0

            while k == 0:
                if nums[left] % 2 == 1:
                    k += 1
                sub_res += 1
                left += 1

            res += sub_res
        return res


tests = [
    (
        ([1, 1, 2, 1, 1], 3),
        2,
    ),
    (
        ([2, 4, 6], 1),
        0,
    ),
    (
        ([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2),
        16,
    ),
    (
        ([1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1], 4),
        6,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().numberOfSubarrays(*inputs)
    assert output == expected
