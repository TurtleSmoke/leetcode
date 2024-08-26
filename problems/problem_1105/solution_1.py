from typing import List

import pytest


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        dp = [float("inf") for _ in range(len(books) + 1)]
        dp[0] = 0
        for i in range(1, len(books) + 1):
            max_width = shelfWidth
            max_height = 0
            j = i - 1
            while j >= 0 and max_width - books[j][0] >= 0:
                max_width -= books[j][0]
                max_height = max(max_height, books[j][1])
                dp[i] = min(dp[i], dp[j] + max_height)
                j -= 1

        return dp[len(books)]


tests = [
    (
        ([[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4),
        6,
    ),
    (
        ([[1, 3], [2, 4], [3, 2]], 6),
        4,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().minHeightShelves(*inputs)
    assert output == expected
