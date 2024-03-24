import pytest
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[slow]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        while slow != fast:
            fast = nums[fast]
            slow = nums[slow]

        return slow


tests = [
    (
        ([1, 3, 4, 2, 2],),
        2,
    ),
    (
        ([3, 1, 3, 4, 2],),
        3,
    ),
    (
        ([3, 3, 3, 3, 3],),
        3,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().findDuplicate(*inputs)
    assert output == expected
