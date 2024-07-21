from collections import deque, defaultdict
from typing import List

import numpy as np
import pytest


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topological_sort(graph):
            res = []
            in_degree = [0] * (k + 1)
            for node in graph:
                for neighbor in graph[node]:
                    in_degree[neighbor] += 1

            queue = deque([i for i in range(1, k + 1) if in_degree[i] == 0])
            while queue:
                node = queue.popleft()
                res.append(node)
                for neighbor in graph[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)

            return res if len(res) == k else []

        graph_row = defaultdict(list)
        graph_col = defaultdict(list)
        for s, d in rowConditions:
            graph_row[s].append(d)
        for s, d in colConditions:
            graph_col[s].append(d)

        row_order = {n: i for i, n in enumerate(topological_sort(graph_row))}
        col_order = {n: i for i, n in enumerate(topological_sort(graph_col))}

        if not row_order or not col_order:
            return []

        res = [[0 for _ in range(k)] for _ in range(k)]
        for n in range(1, k + 1):
            res[row_order[n]][col_order[n]] = n

        return res


tests = [
    (
        (3, [[1, 2], [3, 2]], [[2, 1], [3, 2]]),
        [[3, 0, 0], [0, 0, 1], [0, 2, 0]],
    ),
    (
        (3, [[1, 2], [2, 3], [3, 1], [2, 3]], [[2, 1]]),
        [],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    k, expected_row_order, expected_col_order = inputs
    output = Solution().buildMatrix(k, expected_row_order, expected_col_order)
    if expected:
        output = np.asarray(output)
        output_row_order = {n: i for i, n in enumerate(output[np.nonzero(output)])}
        output_col_order = {n: i for i, n in enumerate(output.T[np.nonzero(output.T)])}
        for s, d in expected_row_order:
            assert output_row_order[s] < output_row_order[d]
        for s, d in expected_col_order:
            assert output_col_order[s] < output_col_order[d]
    else:
        assert output == expected
