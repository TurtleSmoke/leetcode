from typing import Optional

import pytest

from problems.utils import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        # Find the middle of the linked list
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        # Reverse the second half of the linked list
        prev, slow, prev.next = slow, slow.next, None
        while slow:
            slow.next, slow, prev = prev, slow.next, slow
        fast, slow = head, prev

        # Compare the first and second half of the linked list
        while slow:
            if fast.val != slow.val:
                return False
            fast, slow = fast.next, slow.next

        return True


tests = [
    (
        ([1, 2, 2, 1],),
        True,
    ),
    (
        ([1, 2],),
        False,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().isPalindrome(ListNode.from_list(inputs[0]))
    assert output == expected
