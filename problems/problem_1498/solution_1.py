import pytest
from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7

        nums = sorted(nums)
        res = 0
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                res = (res + 2 ** (right - left)) % MOD
                left += 1
        return res


tests = [
    (
        ([3, 5, 6, 7], 9),
        4,
    ),
    (
        ([3, 3, 6, 8], 10),
        6,
    ),
    (
        ([2, 3, 3, 4, 6, 7], 12),
        61,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().numSubseq(*inputs)
    assert output == expected
