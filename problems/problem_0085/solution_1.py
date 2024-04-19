import pytest
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix[0])
        height = [0] * (n + 1)
        res = 0
        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == "1" else 0
            stack = [-1]
            for i in range(n + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    res = max(res, h * w)
                stack.append(i)
        return res


tests = [
    (
        ([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]],),
        6,
    ),
    (
        ([["0"]],),
        0,
    ),
    (
        ([["1"]],),
        1,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().maximalRectangle(*inputs)
    assert output == expected
