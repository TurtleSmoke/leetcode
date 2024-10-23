import pytest


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        def rec(a, b, c, aa, bb, cc):
            if a < b:
                return rec(b, a, c, bb, aa, cc)
            if b < c:
                return rec(a, c, b, aa, cc, bb)
            if b == 0:
                return aa * min(2, a)
            use_a = min(2, a)
            use_b = 1 if a - use_a >= b else 0
            return aa * use_a + bb * use_b + rec(a - use_a, b - use_b, c, aa, bb, cc)

        return rec(a, b, c, "a", "b", "c")


tests = [
    (
        (1, 1, 7),
        "ccaccbcc",
    ),
    (
        (7, 1, 0),
        "aabaa",
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().longestDiverseString(*inputs)
    assert output == expected
