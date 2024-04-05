import pytest


class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and abs(ord(c) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)


tests = [
    (
        ("leEeetcode",),
        "leetcode",
    ),
    (
        ("abBAcC",),
        "",
    ),
    (
        ("s",),
        "s",
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().makeGood(*inputs)
    assert output == expected
