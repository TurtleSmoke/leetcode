import pytest
from typing import List


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        return max(sum(x) for x in zip(*[map(int, format(x, "064b")) for x in candidates]))


tests = [
    (
        ([16, 17, 71, 62, 12, 24, 14],),
        4,
    ),
    (
        ([8, 8],),
        2,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().largestCombination(*inputs)
    assert output == expected
