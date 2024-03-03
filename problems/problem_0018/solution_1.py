from typing import List


def twoSum(nums: List[int], target: int) -> List[List[int]]:
    res = []
    left = 0
    right = len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            res.append([nums[left], nums[right]])
            left += 1
            right -= 1
            while left < right and nums[left] == nums[left - 1]:
                left += 1
            while left < right and nums[right] == nums[right + 1]:
                right -= 1
        elif s < target:
            left += 1
        else:
            right -= 1
    return res


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                for s in twoSum(nums[j + 1 :], target - nums[i] - nums[j]):
                    res.append([nums[i], nums[j], *s])
        return res


tests = [
    (
        ([1, 0, -1, 0, -2, 2], 0),
        [
            [-2, -1, 1, 2],
            [-2, 0, 0, 2],
            [-1, 0, 0, 1],
        ],
    ),
    (
        ([], 0),
        [],
    ),
    (
        ([0, 0, 0, 0], 0),
        [[0, 0, 0, 0]],
    ),
    (
        ([2, 2, 2, 2, 2], 8),
        [[2, 2, 2, 2]],
    ),
]
