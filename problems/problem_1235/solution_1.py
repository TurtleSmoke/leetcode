import bisect
from typing import List

import pytest


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        dp = [[0, 0]]

        for job_end, job_start, job_profit in sorted(zip(endTime, startTime, profit, strict=False)):
            i = bisect.bisect(dp, [job_start + 1]) - 1
            if dp[i][1] + job_profit > dp[-1][1]:
                dp.append([job_end, dp[i][1] + job_profit])

        return dp[-1][1]


tests = [
    (
        ([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]),
        120,
    ),
    (
        ([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]),
        150,
    ),
    (
        ([1, 1, 1], [2, 3, 4], [5, 6, 4]),
        6,
    ),
    (
        ([1, 2, 3, 3], [3, 4, 5, 1000000000], [50, 10, 40, 70]),
        120,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().jobScheduling(*inputs)
    assert output == expected
