import pytest


class Solution:
    def numSteps(self, s: str) -> int:
        odd = 0
        carry = 0
        for c in s[:1:-1]:
            odd += (c == "1") + (carry == 1)
            carry |= c == "1"

        return odd + carry + len(s) - 1


tests = [
    (
        ("1101",),
        6,
    ),
    (
        ("10",),
        1,
    ),
    (
        ("1",),
        0,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().numSteps(*inputs)
    assert output == expected
