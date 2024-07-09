import itertools
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
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        criticals_points = []
        prev = head.val
        mini = float("inf")
        for i in itertools.count(0):
            if head.next is None:
                break
            if prev < head.val > head.next.val or prev > head.val < head.next.val:
                criticals_points.append(i)
            if len(criticals_points) >= 2:
                mini = min(mini, criticals_points[-1] - criticals_points[-2])
            prev = head.val
            head = head.next

        if len(criticals_points) < 2:
            return [-1, -1]

        return [mini, criticals_points[-1] - criticals_points[0]]


tests = [
    (
        ([3, 1],),
        [-1, -1],
    ),
    (
        ([5, 3, 1, 2, 5, 1, 2],),
        [1, 3],
    ),
    (
        ([1, 3, 2, 2, 3, 2, 2, 2, 7],),
        [3, 3],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().nodesBetweenCriticalPoints(ListNode.from_list(inputs[0]))
    assert output == expected
