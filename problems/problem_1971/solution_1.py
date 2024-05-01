import pytest
from typing import List
from collections import defaultdict


class Solution:
    def validPath(self, _: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)

        def dfs(src):
            if src not in seen:
                seen.add(src)
                for dst in graph[src]:
                    dfs(dst)

        seen = set()
        dfs(source)
        return destination in seen


tests = [
    (
        (3, [[0, 1], [1, 2], [2, 0]], 0, 2),
        True,
    ),
    (
        (6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5),
        False,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().validPath(*inputs)
    assert output == expected
