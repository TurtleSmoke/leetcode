import heapq
from typing import List

import pytest


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted([float(w) / q, q] for w, q in zip(wage, quality, strict=False))
        res = float("inf")
        qsum = 0
        heap = []
        for r, q in workers:
            heapq.heappush(heap, -q)
            qsum += q
            if len(heap) > k:
                qsum += heapq.heappop(heap)
            if len(heap) == k:
                res = min(res, qsum * r)

        return res


tests = [
    (
        ([10, 20, 5], [70, 50, 30], 2),
        105.00000,
    ),
    (
        ([3, 1, 10, 10, 1], [4, 8, 2, 2, 7], 3),
        30.66667,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().mincostToHireWorkers(*inputs)
    assert round(output, 5) == round(expected, 5)
