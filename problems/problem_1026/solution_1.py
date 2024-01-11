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
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            mini, maxi, diff = node.val, node.val, 0
            if node.left:
                lmini, lmaxi, ldiff = dfs(node.left)
                mini = min(mini, lmini)
                maxi = max(maxi, lmaxi)
                diff = max(diff, ldiff)
            if node.right:
                rmini, rmaxi, rdiff = dfs(node.right)
                mini = min(mini, rmini)
                maxi = max(maxi, rmaxi)
                diff = max(diff, rdiff)
            diff = max(abs(node.val - mini), abs(node.val - maxi), diff)
            return mini, maxi, diff

        return dfs(root)[2]


tests = [
    (
        ([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13],),
        7,
    ),
    (
        ([1, None, 2, None, 0, 3],),
        3,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().maxAncestorDiff(TreeNode.list_to_TreeNode(inputs[0]))
    assert output == expected
