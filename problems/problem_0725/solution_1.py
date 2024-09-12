from typing import List
from typing import Optional

import pytest

from problems.utils import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        current, length = head, 0
        while current:
            current, length = current.next, length + 1

        quotient, remainder = divmod(length, k)
        res = [quotient + 1] * remainder + [quotient] * (k - remainder)

        previous, current = None, head
        for i, size in enumerate(res):
            if previous:
                previous.next = None
            res[i] = current
            for _ in range(size):
                previous, current = current, current.next

        return res


tests = [
    (
        ([1, 2, 3], 5),
        [[1], [2], [3], [], []],
    ),
    (
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3),
        [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().splitListToParts(ListNode.from_list(inputs[0]), inputs[1])
    output = [ListNode.to_list(node) if node is not None else [] for node in output]
    assert output == expected
