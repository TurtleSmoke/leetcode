import pytest
from typing import Optional
from problems.utils import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def dfs(node):
            if node is None:
                return None

            node.next = dfs(node.next)
            if node.next and node.val < node.next.val:
                return node.next

            return node

        return dfs(head)


tests = [
    (
        ([5, 2, 13, 3, 8],),
        [13, 8],
    ),
    (
        ([1, 1, 1, 1],),
        [1, 1, 1, 1],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().removeNodes(ListNode.from_list(inputs[0]))
    assert ListNode.to_list(output) == expected
