from typing import Optional

import pytest

from problems.utils import ListNode


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(None, head)
        prev = dummy
        current = head
        while current and current.next:
            prev.next = current.next
            current.next = current.next.next
            prev.next.next = current
            prev, current = current, current.next

        return dummy.next


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


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    f = getattr(
        Solution(),
        next(method for method in dir(Solution()) if not method.startswith("_")),
    )
    output = f(ListNode.list_to_ListNode(inputs[0]))
    expected = ListNode.list_to_ListNode(expected)
    ListNode.assert_list_equal(output, expected)
