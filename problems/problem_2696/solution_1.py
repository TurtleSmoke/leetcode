import pytest


class Solution:
    def minLength(self, s: str) -> int:
        while "AB" in s or "CD" in s:
            s = s.replace("AB", "").replace("CD", "")
        return len(s)


tests = [
    (
        ("ABFCACDB",),
        2,
    ),
    (
        ("ACBBD",),
        5,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().minLength(*inputs)
    assert output == expected
