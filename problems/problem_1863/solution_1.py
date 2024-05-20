import pytest
from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i, xor):
            if i == len(nums):
                return xor
            return dfs(i + 1, xor) + dfs(i + 1, xor ^ nums[i])

        return dfs(0, 0)


tests = [
    (
        ([1, 3],),
        6,
    ),
    (
        ([5, 1, 6],),
        28,
    ),
    (
        ([3, 4, 5, 6, 7, 8],),
        480,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().subsetXORSum(*inputs)
    assert output == expected
