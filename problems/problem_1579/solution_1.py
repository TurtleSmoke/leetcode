from typing import List

import pytest


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        lines = list(range(n + 1))
        res, e1, e2 = 0, 0, 0

        def find(x):
            if x != lines[x]:
                lines[x] = find(lines[x])
            return lines[x]

        def union(x, y):
            x, y = find(x), find(y)
            if x == y:
                return 0

            lines[x] = y
            return 1

        for _, i, j in filter(lambda e: e[0] == 3, edges):
            if union(i, j):
                e1 += 1
                e2 += 1
            else:
                res += 1

        both_lines = lines[:]
        for _, i, j in filter(lambda e: e[0] == 1, edges):
            if union(i, j):
                e1 += 1
            else:
                res += 1

        lines = both_lines
        for _, i, j in filter(lambda e: e[0] == 2, edges):
            if union(i, j):
                e2 += 1
            else:
                res += 1

        return res if e1 == e2 == n - 1 else -1


tests = [
    (
        (4, [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]),
        2,
    ),
    (
        (4, [[3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]]),
        0,
    ),
    (
        (4, [[3, 2, 3], [1, 1, 2], [2, 3, 4]]),
        -1,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().maxNumEdgesToRemove(*inputs)
    assert output == expected
