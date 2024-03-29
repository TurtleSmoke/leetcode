from typing import List

import pytest


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        query = max(nums)
        res = cur = i = 0

        for j in range(len(nums)):
            cur += nums[j] == query
            while cur >= k:
                cur -= nums[i] == query
                i += 1
            res += i

        return res


tests = [
    (
        ([1, 3, 2, 3, 3], 2),
        6,
    ),
    (
        ([1, 3, 2, 3, 2, 3], 2),
        8,
    ),
    (
        ([1, 3, 3, 2], 2),
        4,
    ),
    (
        ([1, 3, 2, 3, 3, 1], 2),
        10,
    ),
    (
        ([1, 4, 2, 1], 3),
        0,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().countSubarrays(*inputs)
    assert output == expected
