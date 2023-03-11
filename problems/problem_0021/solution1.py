from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode()
        cur = head
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2
        return head.next


tests = [
    (
        ([1, 2, 4], [1, 3, 4]),
        [1, 1, 2, 3, 4, 4],
    ),
    (
        ([], []),
        [],
    ),
    (
        ([], [0]),
        [0],
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
