from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        res = float("inf")
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return s
                res = min(res, s, key=lambda x: abs(x - target))

                if s < target:
                    l += 1
                else:
                    r -= 1
        return res


tests = [
    (
        ([-1, 2, 1, -4], 1),
        2,
    ),
    (
        ([0, 0, 0], 1),
        0,
    ),
]
