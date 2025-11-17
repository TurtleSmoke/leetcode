import pytest
from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        positions = [i for i, n in enumerate(nums) if n == 1]
        return all(x >= k for x in [a - b - 1 for a, b in zip(positions[1:], positions[:-1], strict=False)])


tests = [
    (
        ([1, 0, 0, 0, 1, 0, 0, 1], 2),
        True,
    ),
    (
        ([1, 0, 0, 1, 0, 1], 2),
        False,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().kLengthApart(*inputs)
    assert output == expected
