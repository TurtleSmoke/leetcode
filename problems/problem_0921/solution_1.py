import pytest


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        opening = 0
        for c in s:
            if c == "(":
                opening += 1
            elif c == ")" and opening > 0:
                opening -= 1
            else:
                res += 1

        return res + opening


tests = [
    (
        ("())",),
        1,
    ),
    (
        ("(((",),
        3,
    ),
    (
        ("()))((",),
        4,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().minAddToMakeValid(*inputs)
    assert output == expected
