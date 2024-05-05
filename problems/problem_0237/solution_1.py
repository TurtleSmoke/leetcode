import pytest

from problems.utils import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


tests = [
    (
        ([4, 5, 1, 9], 5),
        [4, 1, 9],
    ),
    (
        ([4, 5, 1, 9], 1),
        [4, 5, 9],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    head = ListNode.from_list(inputs[0])
    input_head = head
    while input_head.val != inputs[1]:
        input_head = input_head.next
    Solution().deleteNode(input_head)
    assert ListNode.to_list(head) == expected
