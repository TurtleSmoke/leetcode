from collections import deque
from typing import Optional

import pytest

from problems.utils import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dq = deque([(root, root.val)])
        while dq:
            level_sum = sum(node.val for node, _ in dq)
            for _ in range(len(dq)):
                node, local_sum = dq.popleft()
                node.val = level_sum - local_sum

                children_sum = 0 + (node.left.val if node.left else 0) + (node.right.val if node.right else 0)
                if node.left:
                    dq.append((node.left, children_sum))
                if node.right:
                    dq.append((node.right, children_sum))

        return root


tests = [
    (
        ([5, 4, 9, 1, 10, None, 7],),
        [0, 0, 0, 7, 7, None, 11],
    ),
    (
        ([3, 1, 2],),
        [0, 0, 0],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().replaceValueInTree(TreeNode.from_list(*inputs))
    assert TreeNode.to_list(output) == expected
