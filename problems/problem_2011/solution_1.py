import pytest
from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(ord(",") - ord(s[1]) for s in operations)


tests = [
    (
        (["--X", "X++", "X++"],),
        1,
    ),
    (
        (["++X", "++X", "X++"],),
        3,
    ),
    (
        (["X++", "++X", "--X", "X--"],),
        0,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().finalValueAfterOperations(*inputs)
    assert output == expected
