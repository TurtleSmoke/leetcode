from collections import deque

import pytest
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        norths = deque([(0, i) for i in range(m)] + [(i, 0) for i in range(1, n)])
        souths = deque([(n - 1, i) for i in range(m)] + [(i, m - 1) for i in range(n - 1)])

        def bfs(queue):
            visited = set()
            while queue:
                pos = queue.popleft()
                visited.add(pos)
                for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                    x, y = pos[0] + dx, pos[1] + dy
                    if 0 <= x < n and 0 <= y < m and (x, y) not in visited and heights[x][y] >= heights[pos[0]][pos[1]]:
                        queue.append((x, y))
            return visited

        return list(bfs(norths) & bfs(souths))


tests = [
    (
        ([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]],),
        [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]],
    ),
    (
        ([[1]],),
        [[0, 0]],
    ),
    (
        ([[1, 1], [1, 1], [1, 1]],),
        [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1]],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().pacificAtlantic(*inputs)
    output = set(map(tuple, output))
    assert output == set(map(tuple, expected))
