from typing import List
from typing import Optional

import pytest

from problems.utils import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)

        res = ListNode(next=head)
        head = res
        while head and head.next:
            if head.next.val in nums:
                head.next = head.next.next
            else:
                head = head.next

        return res.next


tests = [
    (
        ([1, 2, 3], [1, 2, 3, 4, 5]),
        [4, 5],
    ),
    (
        ([1], [1, 2, 1, 2, 1, 2]),
        [2, 2, 2],
    ),
    (
        ([5], [1, 2, 3, 4]),
        [1, 2, 3, 4],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().modifiedList(inputs[0], ListNode.from_list(inputs[1]))
    assert ListNode.to_list(output) == expected
