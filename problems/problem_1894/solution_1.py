import bisect
import pytest
from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        cum_sum = [0] * len(chalk)
        cum_sum[0] = chalk[0]
        for i in range(1, len(chalk)):
            cum_sum[i] = cum_sum[i - 1] + chalk[i]
        k = k % cum_sum[-1]
        return bisect.bisect_right(cum_sum, k)


tests = [
    (
        ([5, 1, 5], 22),
        0,
    ),
    (
        ([3, 4, 1, 2], 25),
        1,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().chalkReplacer(*inputs)
    assert output == expected
