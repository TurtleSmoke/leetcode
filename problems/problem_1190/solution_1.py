import pytest


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ")":
                temp = []
                while stack[-1] != "(":
                    temp.append(stack.pop())
                stack.pop()
                stack.extend(temp)
            else:
                stack.append(c)
        return "".join(stack)


tests = [
    (
        ("(abcd)",),
        "dcba",
    ),
    (
        ("(u(love)i)",),
        "iloveu",
    ),
    (
        ("(ed(et(oc))el)",),
        "leetcode",
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().reverseParentheses(*inputs)
    assert output == expected
