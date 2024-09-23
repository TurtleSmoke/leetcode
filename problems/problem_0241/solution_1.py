import operator

import pytest
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        func = {"+": operator.add, "-": operator.sub, "*": operator.mul}
        res = []
        for i, c in enumerate(expression):
            if c in func:
                for left in self.diffWaysToCompute(expression[:i]):
                    for right in self.diffWaysToCompute(expression[i + 1 :]):
                        res.append(func[c](left, right))

        return res if res else [int(expression)]


tests = [
    (
        ("2-1-1",),
        [2, 0],
    ),
    (
        ("2*3-4*5",),
        [-34, -10, -14, -10, 10],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().diffWaysToCompute(*inputs)
    assert output == expected
