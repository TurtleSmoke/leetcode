import pytest
from collections import defaultdict
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cache = defaultdict(int, {0: 1})
        cumsum = 0
        res = 0
        for n in nums:
            cumsum = (cumsum + n) % k
            res += cache[cumsum]
            cache[cumsum] += 1

        return res


tests = [
    (
        ([4, 5, 0, -2, -3, 1], 5),
        7,
    ),
    (
        ([5], 9),
        0,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().subarraysDivByK(*inputs)
    assert output == expected
