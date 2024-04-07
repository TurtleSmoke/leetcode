import pytest


class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin = cmax = 0
        for c in s:
            cmax += -1 if c == ")" else 1
            cmin = cmin + 1 if c == "(" else max(cmin - 1, 0)

            if cmax < 0:
                return False

        return cmin == 0


tests = [
    (
        ("()",),
        True,
    ),
    (
        ("(*)",),
        True,
    ),
    (
        ("(*))",),
        True,
    ),
    (
        ("(",),
        False,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().checkValidString(*inputs)
    assert output == expected
