from typing import List

import pytest


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            new_res = []
            for l in res:
                for i in range(len(l) + 1):
                    new_res.append(l[:i] + [n] + l[i:])
            res = new_res
        return res


tests = [
    (
        ([1, 2, 3],),
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
    ),
    (
        ([0, 1],),
        [[0, 1], [1, 0]],
    ),
    (
        ([1],),
        [[1]],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().permute(*inputs)
    assert sorted(output) == sorted(expected)
