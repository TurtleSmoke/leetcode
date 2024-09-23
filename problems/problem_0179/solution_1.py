import pytest
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        return str(int("".join(sorted(map(str, nums), key=lambda x: x * 9, reverse=True))))


tests = [
    (
        ([10, 2],),
        "210",
    ),
    (
        ([3, 30, 34, 5, 9],),
        "9534330",
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().largestNumber(*inputs)
    assert output == expected
