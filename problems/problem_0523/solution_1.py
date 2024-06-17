from typing import List
import pytest


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cache = {0: -1}
        cumsum = 0
        for i, n in enumerate(nums):
            cumsum = (cumsum + n) % k
            if cumsum in cache:
                if i - cache[cumsum] >= 2:
                    return True
            else:
                cache[cumsum] = i
        return False


tests = [
    (
        ([23, 2, 4, 6, 7], 6),
        True,
    ),
    (
        ([23, 2, 6, 4, 7], 6),
        True,
    ),
    (
        ([23, 2, 6, 4, 7], 13),
        False,
    ),
    (
        ([0], 1),
        False,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().checkSubarraySum(*inputs)
    assert output == expected
