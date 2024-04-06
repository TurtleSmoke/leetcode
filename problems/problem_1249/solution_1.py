import pytest


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s)
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    s[i] = ""
        for i in stack:
            s[i] = ""
        return "".join(s)


tests = [
    (
        ("lee(t(c)o)de)",),
        "lee(t(c)o)de",
    ),
    (
        ("a)b(c)d",),
        "ab(c)d",
    ),
    (
        ("))((",),
        "",
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().minRemoveToMakeValid(*inputs)
    assert output == expected
