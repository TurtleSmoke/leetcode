import pytest


class Solution:
    def minChanges(self, s: str) -> int:
        return sum(a != b for a, b in zip(s[::2], s[1::2], strict=False))


tests = [
    (
        ("1001",),
        2,
    ),
    (
        ("10",),
        1,
    ),
    (
        ("0000",),
        0,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().minChanges(*inputs)
    assert output == expected
