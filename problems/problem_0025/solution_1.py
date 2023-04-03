from typing import Optional

import pytest

from problems.utils import ListNode


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        dummy = ListNode(0, head)
        head = dummy
        while head.next:
            tail = head
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next

            prev, curr = tail.next, head.next
            for _ in range(k):
                curr.next, prev, curr = prev, curr, curr.next
            head.next, head = prev, head.next

        return dummy.next


tests = [
    (
        ([1, 2, 3, 4, 5], 2),
        [2, 1, 4, 3, 5],
    ),
    (
        ([1, 2, 3, 4, 5], 3),
        [3, 2, 1, 4, 5],
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
    output = f(ListNode.list_to_ListNode(inputs[0]), inputs[1])
    expected = ListNode.list_to_ListNode(expected)
    ListNode.assert_list_equal(output, expected)
