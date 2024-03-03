from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        while nums1 and nums2:
            if nums1[0] < nums2[0]:
                nums.append(nums1.pop(0))
            else:
                nums.append(nums2.pop(0))
        nums += nums1 + nums2

        length = len(nums)
        if length % 2 == 0:
            return (nums[length // 2 - 1] + nums[length // 2]) / 2
        return nums[length // 2]


tests = [
    (
        ([1, 3], [2]),
        2.0,
    ),
    (
        ([1, 2], [3, 4]),
        2.5,
    ),
    (
        ([0, 0], [0, 0]),
        0.0,
    ),
    (
        ([], [1]),
        1.0,
    ),
    (
        ([2], []),
        2.0,
    ),
]
