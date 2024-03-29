import pytest
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            if nums[abs(n) - 1] < 0:
                res.append(abs(n))
            else:
                nums[abs(n) - 1] *= -1

        return res


tests = [
    (
        ([4, 3, 2, 7, 8, 2, 3, 1],),
        [2, 3],
    ),
    (
        ([1, 1, 2],),
        [1],
    ),
    (
        ([1],),
        [],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().findDuplicates(*inputs)
    assert output == expected
