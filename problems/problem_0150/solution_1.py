import pytest
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "/": lambda x, y: int(x / y),
            "*": lambda x, y: x * y,
        }

        stack = []
        for token in tokens:
            if token in operators:
                y = stack.pop()
                x = stack.pop()
                stack.append(operators[token](x, y))
            else:
                stack.append(int(token))

        return stack.pop()


tests = [
    (
        (["2", "1", "+", "3", "*"],),
        9,
    ),
    (
        (["4", "13", "5", "/", "+"],),
        6,
    ),
    (
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],),
        22,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().evalRPN(*inputs)
    assert output == expected
