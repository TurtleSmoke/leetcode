import pytest
from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        s += -len(s) % k * fill
        return [s[i : i + k] for i in range(0, len(s), k)]


tests = [
    (
        ("abcdefghi", 3, "x"),
        ["abc", "def", "ghi"],
    ),
    (
        ("abcdefghij", 3, "x"),
        ["abc", "def", "ghi", "jxx"],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().divideString(*inputs)
    assert output == expected
