from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needed = {}
        for i, num in enumerate(nums):
            if target - num in needed:
                return [needed[target - num], i]
            needed[num] = i


tests = [
    (
        ([2, 7, 11, 15], 9),
        [0, 1],
    ),
    (
        ([3, 2, 4], 6),
        [1, 2],
    ),
    (
        ([3, 3], 6),
        [0, 1],
    ),
]
