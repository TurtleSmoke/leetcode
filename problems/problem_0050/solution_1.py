import pytest


class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n


tests = [
    (
        (2.0, 10),
        1024.00000,
    ),
    (
        (2.1, 3),
        9.26100,
    ),
    (
        (2.0, -2),
        0.25000,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().myPow(*inputs)
    assert abs(output - expected) < 1e-5
