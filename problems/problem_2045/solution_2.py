import heapq
from collections import defaultdict
from typing import List

import pytest


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        dists = [[] for _ in range(n + 1)]
        dists[1] = [0]
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        heap = [(0, 1)]
        while heap:
            dist, node = heapq.heappop(heap)
            if node == n and len(dists[n]) >= 2:
                return max(dists[n])

            for neighbour in graph[node]:
                new_dist = dist + time
                if (dist // change) % 2 == 1:
                    new_dist += change - dist % change

                if not dists[neighbour] or (len(dists[neighbour]) == 1 and dists[neighbour][0] != new_dist):
                    dists[neighbour].append(new_dist)
                    heapq.heappush(heap, (new_dist, neighbour))


tests = [
    (
        (5, [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]], 3, 5),
        13,
    ),
    (
        (2, [[1, 2]], 3, 2),
        11,
    ),
    (
        (6, [[1, 2], [1, 3], [2, 4], [3, 5], [5, 4], [4, 6]], 3, 100),
        12,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().secondMinimum(*inputs)
    assert output == expected
