from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first = head
        second = head
        for _ in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next


tests = [
    (
        ([1, 2, 3, 4, 5], 2),
        [1, 2, 3, 5],
    ),
    (
        ([1], 1),
        [],
    ),
    (
        ([1, 2], 1),
        [1],
    ),
]


def list_to_ListNode(l):
    head = ListNode()
    node = head
    for i in l:
        node.next = ListNode(i)
        node = node.next
    return head.next


def validator(removeNthFromEnd, inputs, expected):
    head, n = inputs
    head = list_to_ListNode(head)
    expected = list_to_ListNode(expected)
    output = removeNthFromEnd(head, n)
    while output and expected:
        assert output.val == expected.val
        output = output.next
        expected = expected.next
    assert not output and not expected
