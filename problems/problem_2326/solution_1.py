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
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1] * n for _ in range(m)]
        x, dx, y, dy = 0, 1, 0, 0
        while head:
            res[y][x] = head.val
            head = head.next
            if x + dx >= n or x + dx < 0 or y + dy >= m or y + dy < 0 or res[y + dy][x + dx] != -1:
                dx, dy = -dy, dx

            x, y = x + dx, y + dy

        return res


tests = [
    (
        (3, 5, [3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0]),
        [[3, 0, 2, 6, 8], [5, 0, -1, -1, 1], [5, 2, 4, 9, 7]],
    ),
    (
        (1, 4, [0, 1, 2]),
        [[0, 1, 2, -1]],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().spiralMatrix(*inputs[:2], ListNode.from_list(inputs[2]))
    assert output == expected
