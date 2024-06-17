import pytest
from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        root = {}

        def find(x):
            root[x] = find(root[x] + 1) if x in root else x
            return root[x]

        res = sum(find(n) - n for n in nums)
        print(root)
        return res


tests = [
    (
        ([1, 2, 2],),
        1,
    ),
    (
        ([3, 2, 1, 2, 1, 7],),
        6,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().minIncrementForUnique(*inputs)
    assert output == expected
