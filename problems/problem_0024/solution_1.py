from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        new_head = head.next
        head.next = self.swapPairs(new_head.next)
        new_head.next = head

        return new_head


tests = [
    (
        ([1, 2, 3, 4],),
        [2, 1, 4, 3],
    ),
    (
        ([],),
        [],
    ),
    (
        ([1],),
        [1],
    ),
]


def list_to_ListNode(l):
    head = ListNode()
    current = head
    for i in l:
        current.next = ListNode(i)
        current = current.next
    return head.next


def validator(swapPairs, inputs, expected):
    output = swapPairs(list_to_ListNode(inputs[0]))
    expected = list_to_ListNode(expected)
    while output and expected:
        print(output.val, expected.val)
        assert output.val == expected.val, (output.val, expected.val)
        output = output.next
        expected = expected.next
    assert not output and not expected, (output, expected)
