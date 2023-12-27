import pytest


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack_left = []
        start = -1
        res = 0

        for i, c in enumerate(s):
            if c == "(":
                stack_left.append(i)
            else:
                if not stack_left:
                    start = i
                else:
                    stack_left.pop()
                    if not stack_left:
                        res = max(res, i - start)
                    else:
                        res = max(res, i - stack_left[-1])

        return res


tests = [
    (
        ("(()",),
        2,
    ),
    (
        (")()())",),
        4,
    ),
    (
        ("",),
        0,
    ),
    (
        ("(())()",),
        6,
    ),
    (
        ("(())()))(())()",),
        6,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().longestValidParentheses(*inputs)
    assert output == expected
