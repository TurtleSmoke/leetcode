import pytest


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        occ = s.count("1")
        return "1" * (occ - 1) + "0" * (len(s) - occ) + "1"


tests = [
    (
        ("010",),
        "001",
    ),
    (
        ("0101",),
        "1001",
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().maximumOddBinaryNumber(*inputs)
    assert output == expected
