import heapq
from collections import defaultdict
from typing import List

import pytest


class Solution:
    def maxProbability(
        self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int
    ) -> float:
        graph = defaultdict(list)
        for (s, d), w in zip(edges, succProb, strict=False):
            graph[s].append((w, d))
            graph[d].append((w, s))

        pq = [(-1, start_node)]
        seen = set()

        while pq:
            cost, current = heapq.heappop(pq)
            if current == end_node:
                return -cost

            seen.add(current)
            for weight, neighbor in graph[current]:
                if neighbor not in seen:
                    heapq.heappush(pq, (cost * weight, neighbor))

        return 0


tests = [
    (
        (3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2),
        0.25000,
    ),
    (
        (3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2),
        0.30000,
    ),
    (
        (3, [[0, 1]], [0.5], 0, 2),
        0.00000,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().maxProbability(*inputs)
    assert output == expected
