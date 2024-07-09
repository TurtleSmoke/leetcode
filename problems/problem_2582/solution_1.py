import pytest


class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        return n - abs(n - 1 - time % ((n - 1) * 2))


tests = [
    (
        (4, 5),
        2,
    ),
    (
        (3, 2),
        3,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().passThePillow(*inputs)
    assert output == expected
