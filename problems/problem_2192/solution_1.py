from collections import defaultdict, deque
from typing import List

import pytest


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        in_degree = [0] * n
        for s, d in edges:
            graph[s].append(d)
            in_degree[d] += 1

        in_nodes = deque([i for i in range(n) if in_degree[i] == 0])

        topological_order = []
        while in_nodes:
            s = in_nodes.popleft()
            topological_order.append(s)
            for neighbor in graph[s]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    in_nodes.append(neighbor)

        ancestors = [set() for _ in range(n)]
        for s in topological_order:
            for neighbor in graph[s]:
                ancestors[neighbor].update(ancestors[s] | {s})

        return [list(sorted(a)) for a in ancestors]


tests = [
    (
        (8, [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]),
        [[], [], [], [0, 1], [0, 2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3]],
    ),
    (
        (5, [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]),
        [[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().getAncestors(*inputs)
    assert output == expected
