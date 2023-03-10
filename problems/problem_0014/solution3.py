from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return res


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
    (
        ([-2, 0, 1, 1, 2],),
        [[-2, 0, 2], [-2, 1, 1]],
    ),
]


def validator(threeSum, inputs, expected):
    output = sorted(threeSum(*inputs))
    expected = sorted(expected)
    assert output == expected, (output, expected)
