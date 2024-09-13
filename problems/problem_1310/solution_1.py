import pytest
from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        dp = [arr[0]] * (len(arr) + 1)
        for i in range(len(arr)):
            dp[i + 1] = dp[i] ^ arr[i]
        return [dp[left] ^ dp[right + 1] for (left, right) in queries]


tests = [
    (
        ([1, 3, 4, 8], [[0, 1], [1, 2], [0, 3], [3, 3]]),
        [2, 7, 14, 8],
    ),
    (
        ([4, 8, 2, 10], [[2, 3], [1, 3], [0, 0], [0, 3]]),
        [8, 0, 4, 4],
    ),
    (
        ([16], [[0, 0], [0, 0], [0, 0]]),
        [16, 16, 16],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().xorQueries(*inputs)
    assert output == expected
