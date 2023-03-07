from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        partition_size = total // 2

        if len(nums1) > len(
            nums2
        ):  # Ensure we apply binary search to the smaller array
            nums1, nums2 = nums2, nums1

        left, right = 0, len(nums1) - 1

        while True:  # Solution is guaranteed to exist
            mid1 = (left + right) // 2
            mid2 = partition_size - mid1 - 2

            left1 = nums1[mid1] if mid1 >= 0 else float("-inf")
            right1 = nums1[mid1 + 1] if mid1 < len(nums1) - 1 else float("inf")
            left2 = nums2[mid2] if mid2 >= 0 else float("-inf")
            right2 = nums2[mid2 + 1] if mid2 < len(nums2) - 1 else float("inf")

            if left1 <= right2 and left2 <= right1:
                if total % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                return max(left1, left2)
            elif left1 > right2:
                right = mid1 - 1
            else:
                left = mid1 + 1


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
