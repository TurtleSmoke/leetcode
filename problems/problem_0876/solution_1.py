import pytest
from typing import Optional

from problems.utils import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


tests = [
    (
        ([1, 2, 3, 4, 5],),
        [3, 4, 5],
    ),
    (
        ([1, 2, 3, 4, 5, 6],),
        [4, 5, 6],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().middleNode(ListNode.list_to_ListNode(*inputs))
    output = ListNode.ListNode_to_list(output)
    assert output == expected
