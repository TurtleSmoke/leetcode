import pytest


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        while len(s) < k:
            s += "1" + "".join("1" if c == "0" else "0" for c in s)[::-1]

        return s[k - 1]


tests = [
    (
        (3, 1),
        "0",
    ),
    (
        (4, 11),
        "1",
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().findKthBit(*inputs)
    assert output == expected
