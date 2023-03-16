from typing import List
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        current = head
        while True:
            min_index = None
            for i, l in enumerate(lists):
                if l and (min_index is None or l.val < lists[min_index].val):
                    min_index = i
            if min_index is None:
                break
            current.next = lists[min_index]
            lists[min_index] = lists[min_index].next
            current = current.next
        return head.next


tests = [
    (
        ([[1, 4, 5], [1, 3, 4], [2, 6]],),
        [1, 1, 2, 3, 4, 4, 5, 6],
    ),
    (
        ([],),
        [],
    ),
    (
        ([[]],),
        [],
    ),
]


def list_to_ListNode(l):
    head = ListNode()
    current = head
    for i in l:
        current.next = ListNode(i)
        current = current.next
    return head.next


def validator(mergeKLists, inputs, expected):
    output = mergeKLists(list(list_to_ListNode(l) for l in inputs[0]))
    expected = list_to_ListNode(expected)
    while output and expected:
        assert output.val == expected.val, (output.val, expected.val)
        output = output.next
        expected = expected.next
    assert not output and not expected, (output, expected)
