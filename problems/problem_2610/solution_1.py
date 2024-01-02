from collections import Counter
from typing import List

import pytest


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums = Counter(nums)

        print(list(nums.elements())[0 :: max(nums.values())])
        res = [[] for _ in range(max(nums.values()))]

        for num, occ in nums.items():
            for i in range(occ):
                res[i].append(num)

        return res


tests = [
    (
        ([1, 3, 4, 1, 2, 3, 1],),
        [[1, 3, 4, 2], [1, 3], [1]],
    ),
    (
        ([2, 1, 1],),
        [[1, 2], [1]],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().findMatrix(*inputs)
    output = [list(sorted(sublist)) for sublist in output]
    expected = [list(sorted(sublist)) for sublist in expected]
    assert output == expected
