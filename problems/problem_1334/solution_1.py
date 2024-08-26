import heapq
from collections import defaultdict
from typing import List

import pytest


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        def bfs(start):
            heap = [(0, start)]
            seen = set()
            while heap:
                dist, node = heapq.heappop(heap)
                seen.add(node)
                for neighbour, dist2 in graph[node]:
                    if neighbour not in seen and dist + dist2 <= distanceThreshold:
                        heapq.heappush(heap, (dist + dist2, neighbour))
            return len(seen), -start

        return min(range(n), key=bfs)


tests = [
    (
        (4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4),
        3,
    ),
    (
        (5, [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], 2),
        0,
    ),
    (
        (6, [[0, 1, 10], [0, 2, 1], [2, 3, 1], [1, 3, 1], [1, 4, 1], [4, 5, 10]], 20),
        5,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().findTheCity(*inputs)
    assert output == expected
