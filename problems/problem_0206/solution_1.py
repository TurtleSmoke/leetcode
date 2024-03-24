import pytest
from typing import Optional
from problems.utils import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev


tests = [
    (
        ([1, 2, 3, 4, 5],),
        [5, 4, 3, 2, 1],
    ),
    (
        ([1, 2],),
        [2, 1],
    ),
    (
        ([],),
        [],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = ListNode.to_list(Solution().reverseList(ListNode.from_list(inputs[0])))
    assert output == expected
