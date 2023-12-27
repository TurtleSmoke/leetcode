import pytest


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack_left = []
        res = [0] * len(s)

        for i, c in enumerate(s):
            if c == "(":
                stack_left.append(i)
            else:
                if stack_left:
                    j = stack_left.pop()
                    res[j] = i - j + 1

        max_len = 0
        i = 0
        while i < len(res):
            j = i
            while j < len(res) and res[j] != 0:
                j += res[j]

            if i != j:
                max_len = max(max_len, j - i)

            i = j + 1

        return max_len


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
