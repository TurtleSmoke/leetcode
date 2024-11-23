import pytest


class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = x
        remaining = n - 1
        pos = 1
        while remaining:
            if not (x & pos):
                res |= (remaining & 1) * pos
                remaining >>= 1
            pos <<= 1
        return res


tests = [
    (
        (3, 4),
        6,
    ),
    (
        (2, 7),
        15,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().minEnd(*inputs)
    assert output == expected
