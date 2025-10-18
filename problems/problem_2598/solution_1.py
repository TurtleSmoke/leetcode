import pytest
from typing import List, Counter


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        remainders = Counter(n % value for n in nums)
        for i in range(len(nums)):
            if remainders[i % value] == 0:
                return i
            remainders[i % value] -= 1
        return len(nums)


tests = [
    (
        ([1, -10, 7, 13, 6, 8], 5),
        4,
    ),
    (
        ([1, -10, 7, 13, 6, 8], 7),
        2,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().findSmallestInteger(*inputs)
    assert output == expected
