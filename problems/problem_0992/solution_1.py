from collections import Counter
from typing import List

import pytest


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def subarrays_with_at_most_k_distinct(nums: List[int], k: int) -> int:
            count = Counter()
            res = i = 0
            for j in range(len(nums)):
                if count[nums[j]] == 0:
                    k -= 1
                count[nums[j]] += 1
                while k < 0:
                    count[nums[i]] -= 1
                    if count[nums[i]] == 0:
                        k += 1
                    i += 1
                res += j - i + 1

            return res

        return subarrays_with_at_most_k_distinct(nums, k) - subarrays_with_at_most_k_distinct(nums, k - 1)


tests = [
    (
        ([1, 2, 1, 2, 3], 2),
        7,
    ),
    (
        ([1, 2, 1, 3, 4], 3),
        3,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().subarraysWithKDistinct(*inputs)
    assert output == expected
