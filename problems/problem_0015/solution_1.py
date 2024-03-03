from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.add(tuple(sorted((nums[i], nums[j], nums[k]))))
        return list(map(list, res))


tests = [
    (
        ([-1, 0, 1, 2, -1, -4],),
        [
            [-1, -1, 2],
            [-1, 0, 1],
        ],
    ),
    (
        ([],),
        [],
    ),
    (
        ([0, 1, 1],),
        [],
    ),
    (
        ([0, 0, 0],),
        [[0, 0, 0]],
    ),
]


def validator(threeSum, inputs, expected):
    output = sorted(threeSum(*inputs))
    expected = sorted(expected)
    assert output == expected, (output, expected)
