import pytest
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                last = stack.pop()
                res[last] = i - last
            stack.append(i)

        return res


tests = [
    (
        ([73, 74, 75, 71, 69, 72, 76, 73],),
        [1, 1, 4, 2, 1, 1, 0, 0],
    ),
    (
        ([30, 40, 50, 60],),
        [1, 1, 1, 0],
    ),
    (
        ([30, 60, 90],),
        [1, 1, 0],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().dailyTemperatures(*inputs)
    assert output == expected
