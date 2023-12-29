from functools import cache
import pytest
from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], days: int) -> int:
        if len(jobDifficulty) < days:
            return -1

        @cache
        def dfs(i, d):
            if d == 1:
                return max(jobDifficulty[i:])

            res, max_cur_d = float("inf"), 0
            for j in range(i, len(jobDifficulty) - d + 1):
                max_cur_d = max(max_cur_d, jobDifficulty[j])
                res = min(res, max_cur_d + dfs(j + 1, d - 1))

            return res

        return dfs(0, days)


tests = [
    (
        ([6, 5, 4, 3, 2, 1], 2),
        7,
    ),
    (
        ([9, 9, 9], 4),
        -1,
    ),
    (
        ([1, 1, 1], 3),
        3,
    ),
    (
        (
            [
                380,
                302,
                102,
                681,
                863,
                676,
                243,
                671,
                651,
                612,
                162,
                561,
                394,
                856,
                601,
                30,
                6,
                257,
                921,
                405,
                716,
                126,
                158,
                476,
                889,
                699,
                668,
                930,
                139,
                164,
                641,
                801,
                480,
                756,
                797,
                915,
                275,
                709,
                161,
                358,
                461,
                938,
                914,
                557,
                121,
                964,
                315,
            ],
            10,
        ),
        3807,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().minDifficulty(*inputs)
    assert output == expected
