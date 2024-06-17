import pytest


class Solution:
    def numSteps(self, s: str) -> int:
        res = 0
        carry = 0
        for c in s[:0:-1]:
            if (c == "1") ^ (carry == 1):
                res += 1
                carry = 1
            else:
                carry = 1 if (c == "1") or (carry == 1) else 0
            res += 1

        return res + carry


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
