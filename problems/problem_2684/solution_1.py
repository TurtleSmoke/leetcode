import pytest
from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        dp = [0] * len(grid)

        for j in range(len(grid[0]) - 2, -1, -1):
            curr_dp = [0] * len(grid)
            for i in range(len(grid)):
                for k in (i - 1, i, i + 1):
                    if 0 <= k < len(grid) and grid[k][j + 1] > grid[i][j]:
                        curr_dp[i] = max(curr_dp[i], 1 + dp[k])
            dp = curr_dp

        return max(dp)


tests = [
    (
        ([[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]],),
        3,
    ),
    (
        ([[3, 2, 4], [2, 1, 9], [1, 1, 7]],),
        0,
    ),
    (
        (
            [
                [187, 167, 209, 251, 152, 236, 263, 128, 135],
                [267, 249, 251, 285, 73, 204, 70, 207, 74],
                [189, 159, 235, 66, 84, 89, 153, 111, 189],
                [120, 81, 210, 7, 2, 231, 92, 128, 218],
                [193, 131, 244, 293, 284, 175, 226, 205, 245],
            ],
        ),
        3,
    ),
]


@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().maxMoves(*inputs)
    assert output == expected
