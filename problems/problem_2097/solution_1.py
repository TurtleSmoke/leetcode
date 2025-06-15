from collections import defaultdict
from typing import List

import pytest


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        degree = defaultdict(int)
        for a, b in pairs:
            graph[a].append(b)
            degree[a] += 1
            degree[b] -= 1

        # Find Eulerian start node
        node = pairs[0][0]
        for p in degree:
            if degree[p] == 1:
                node = p
                break

        # Iterate vertex by vertex
        res = []
        stack = [node]

        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            res.append(stack.pop())

        res.reverse()
        return [[res[i], res[i + 1]] for i in range(len(res) - 1)]


tests = [
    (
        ([[5, 1], [4, 5], [11, 9], [9, 4]],),
        [[11, 9], [9, 4], [4, 5], [5, 1]],
    ),
    (
        ([[1, 3], [3, 2], [2, 1]],),
        [[1, 3], [3, 2], [2, 1]],
    ),
    (
        ([[1, 2], [1, 3], [2, 1]],),
        [[1, 2], [2, 1], [1, 3]],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().validArrangement(*inputs)
    assert output == expected
