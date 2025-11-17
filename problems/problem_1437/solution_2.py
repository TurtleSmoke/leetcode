import pytest
from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_pos = float("-inf")
        for i, n in enumerate(nums):
            if n == 1:
                if i - last_pos <= k:
                    return False
                last_pos = i
        return True


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
