from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i + 1 :]):
                if a + b == target:
                    return [i, j + i + 1]


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
