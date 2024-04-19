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
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)

        def dfs(node, level):
            if not node:
                return node

            if level == 0:
                node.left = TreeNode(val, node.left, None)
                node.right = TreeNode(val, None, node.right)
            else:
                dfs(node.left, level - 1)
                dfs(node.right, level - 1)

            return node

        return dfs(root, depth - 2)


tests = [
    (
        ([4, 2, 6, 3, 1, 5], 1, 2),
        [4, 1, 1, 2, None, None, 6, 3, 1, 5],
    ),
    (
        ([4, 2, None, 3, 1], 1, 3),
        [4, 2, None, 1, 1, 3, None, None, 1],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().addOneRow(TreeNode.from_list(inputs[0]), *inputs[1:])
    assert TreeNode.to_list(output) == expected
