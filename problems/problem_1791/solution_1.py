import pytest
from collections import defaultdict
from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for s, d in edges:
            graph[s].add(d)
            graph[d].add(s)

        return max(graph, key=lambda x: len(graph[x]))


tests = [
    (
        ([[1, 2], [2, 3], [4, 2]],),
        2,
    ),
    (
        ([[1, 2], [5, 1], [1, 3], [1, 4]],),
        1,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().findCenter(*inputs)
    assert output == expected
