from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode()
        current = head
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            current.next = ListNode(carry % 10)
            current = current.next
            carry //= 10
        return head.next

def list_to_ListNode(l):
    head = ListNode()
    current = head
    for i in l:
        current.next = ListNode(i)
        current = current.next
    return head.next

tests = [
    (
        ([2, 4, 3], [5, 6, 4]),
        [7, 0, 8],
    ),
    (
        ([0], [0]),
        [0],
    ),
    (
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]),
        [8, 9, 9, 9, 0, 0, 0, 1],
    ),
]

def validator(addTwoNumbers, inputs, expected):
    output = addTwoNumbers(*(list_to_ListNode(l) for l in inputs))
    expected = list_to_ListNode(expected)
    while output and expected:
        assert output.val == expected.val
        output = output.next
        expected = expected.next
    assert not output and not expected

