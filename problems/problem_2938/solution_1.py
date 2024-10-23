import pytest


class Solution:
    def minimumSteps(self, s: str) -> int:
        res, black = 0, 0
        for c in s:
            if c == "0":
                res += black
            elif c == "1":
                black += 1

        return res


tests = [
    (
        ("101",),
        1,
    ),
    (
        ("100",),
        2,
    ),
    (
        ("0111",),
        0,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().minimumSteps(*inputs)
    assert output == expected
