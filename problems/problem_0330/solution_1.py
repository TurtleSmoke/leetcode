from typing import List
import pytest


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 0
        res = 0
        i = 0
        while miss < n:
            x = nums[i] if i < len(nums) else n + 2
            if x > miss + 1:
                miss = miss * 2 + 1
                res += 1
            else:
                miss += x
                i += 1
        return res


tests = [
    (
        ([1, 3], 6),
        1,
    ),
    (
        ([1, 5, 10], 20),
        2,
    ),
    (
        ([1, 2, 2], 5),
        0,
    ),
    (
        ([1, 3], 2147483647),
        30,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().minPatches(*inputs)
    assert output == expected
