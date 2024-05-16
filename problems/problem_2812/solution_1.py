import heapq
from typing import List

import numpy as np
import pytest
from scipy.ndimage import distance_transform_cdt


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        cost_matrix = distance_transform_cdt(np.asarray(grid) == 0, metric="manhattan")

        visited = set()
        heap = [(-cost_matrix[(0, 0)], (0, 0))]
        while heap:
            cost, coor = heapq.heappop(heap)
            if coor in visited:
                continue
            visited.add(coor)
            if coor == (len(grid) - 1, len(grid[0]) - 1):
                return -cost

            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                neighbor = (coor[0] + dx, coor[1] + dy)
                if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]):
                    heapq.heappush(heap, (max(cost, -cost_matrix[neighbor]), neighbor))

        return 0


tests = [
    (
        ([[1, 0, 0], [0, 0, 0], [0, 0, 1]],),
        0,
    ),
    (
        ([[0, 0, 1], [0, 0, 0], [0, 0, 0]],),
        2,
    ),
    (
        ([[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]],),
        2,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().maximumSafenessFactor(*inputs)
    assert output == expected
