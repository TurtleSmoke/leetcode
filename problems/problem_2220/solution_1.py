import pytest


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return sum(x == "1" for x in bin(start ^ goal))


tests = [
    (
        (10, 7),
        3,
    ),
    (
        (3, 4),
        3,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().minBitFlips(*inputs)
    assert output == expected
