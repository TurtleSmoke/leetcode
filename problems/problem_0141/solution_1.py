from typing import Optional

import pytest

from problems.utils import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


tests = [
    (
        ([3, 2, 0, -4], 1),
        True,
    ),
    (
        ([1, 2], 0),
        True,
    ),
    (
        ([1], -1),
        False,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    list_node = ListNode.from_list(inputs[0])
    if inputs[1] != -1:
        cycle_node = list_node
        for _ in range(inputs[1]):
            cycle_node = cycle_node.next
        current = list_node
        while current.next:
            current = current.next
        current.next = cycle_node

    output = Solution().hasCycle(list_node)
    assert output == expected
