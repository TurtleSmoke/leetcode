import heapq
from collections import defaultdict
from typing import List

import pytest


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for s, d, c in flights:
            graph[s].append((d, c))

        heap = [(0, src, k + 1)]
        while heap:
            total_cost, current_city, remaining_step = heapq.heappop(heap)
            if current_city == dst:
                return total_cost

            if remaining_step > 0:
                for neighbour, cost in graph[current_city]:
                    heapq.heappush(heap, (total_cost + cost, neighbour, remaining_step - 1))

        return -1


tests = [
    (
        (4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1),
        700,
    ),
    (
        (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1),
        200,
    ),
    (
        (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0),
        500,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().findCheapestPrice(*inputs)
    assert output == expected
