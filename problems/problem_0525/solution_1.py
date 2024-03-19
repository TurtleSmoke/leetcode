import pytest
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        res = 0
        cache = {0: 0}
        for i, n in enumerate(nums, 1):
            count += 1 if n == 1 else -1
            if count in cache:
                res = max(res, i - cache[count])
            else:
                cache[count] = i

        return res


tests = [
    (
        ([0, 1],),
        2,
    ),
    (
        ([0, 1, 0],),
        2,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().findMaxLength(*inputs)
    assert output == expected
