from typing import List

import pytest


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        walls = set(map(tuple, walls)) | set(map(tuple, guards))
        res = m * n - len(walls)
        seen = set(map(tuple, guards))
        for x, y in guards:
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = (x + dx, y + dy)
                while 0 <= nx < m and 0 <= ny < n and ((nx, ny) not in walls):
                    if (nx, ny) not in seen:
                        seen.add((nx, ny))
                        res -= 1
                    nx += dx
                    ny += dy
        return res


tests = [
    (
        (4, 6, [[0, 0], [1, 1], [2, 3]], [[0, 1], [2, 2], [1, 4]]),
        7,
    ),
    (
        (3, 3, [[1, 1]], [[0, 1], [1, 0], [2, 1], [1, 2]]),
        4,
    ),
    (
        (2, 7, [[1, 5], [1, 1], [1, 6], [0, 2]], [[0, 6], [0, 3], [0, 5]]),
        1,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().countUnguarded(*inputs)
    assert output == expected
