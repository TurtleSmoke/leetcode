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
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0
            res = 0
            if low <= node.val <= high:
                res += node.val
            if node.val > low:
                res += dfs(node.left)
            if node.val < high:
                res += dfs(node.right)
            return res

        return dfs(root)


tests = [
    (
        ([10, 5, 15, 3, 7, None, 18], 7, 15),
        32,
    ),
    (
        ([10, 5, 15, 3, 7, 13, 18, 1, None, 6], 6, 10),
        23,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    tree, low, high = inputs
    output = Solution().rangeSumBST(TreeNode.list_to_TreeNode(tree), low, high)
    assert output == expected
