import pytest
from math import gcd
from typing import Optional
from problems.utils import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        first, second = head, head.next
        while second:
            first.next = ListNode(gcd(first.val, second.val), second)
            first, second = second, second.next

        return head


tests = [
    (
        ([18, 6, 10, 3],),
        [18, 6, 6, 2, 10, 1, 3],
    ),
    (
        ([7],),
        [7],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().insertGreatestCommonDivisors(ListNode.from_list(inputs[0]))
    assert ListNode.to_list(output) == expected
