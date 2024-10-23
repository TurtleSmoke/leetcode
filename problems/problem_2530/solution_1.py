import heapq
from typing import List

import pytest


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        pq = [-x for x in nums]
        heapq.heapify(pq)
        res = 0
        for _ in range(k):
            x = -heapq.heappop(pq)
            res += x
            heapq.heappush(pq, -((x + 2) // 3))
        return res


tests = [
    (
        ([10, 10, 10, 10, 10], 5),
        50,
    ),
    (
        ([1, 10, 3, 3, 3], 3),
        17,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().maxKelements(*inputs)
    assert output == expected
