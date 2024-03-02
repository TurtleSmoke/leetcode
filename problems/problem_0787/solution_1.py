from collections import defaultdict
from typing import List

import pytest


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        queue = [(src, 0)]
        min_cost = [float("inf") for _ in range(n)]
        steps = 0
        while queue and steps <= k:
            for _ in range(len(queue)):
                cur, prev_cost = queue.pop(0)
                for neighbour, cost in graph[cur]:
                    if prev_cost + cost >= min_cost[neighbour]:
                        continue
                    min_cost[neighbour] = prev_cost + cost
                    queue.append((neighbour, min_cost[neighbour]))

            steps += 1

        return min_cost[dst] if min_cost[dst] != float("inf") else -1


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
