import pytest
from typing import List
from collections import defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(set)
        for src, dst in edges:
            graph[src].add(dst)
            graph[dst].add(src)

        leaves = [node for (node, neighbors) in graph.items() if len(neighbors) == 1]
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves

        return leaves


tests = [
    (
        (4, [[1, 0], [1, 2], [1, 3]]),
        [1],
    ),
    (
        (6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]),
        [3, 4],
    ),
    (
        (1, []),
        [0],
    ),
    (
        (3, [[0, 1], [0, 2]]),
        [0],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().findMinHeightTrees(*inputs)
    assert sorted(output) == sorted(expected)
