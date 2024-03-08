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
        def dfs(node, mini, maxi):
            if not node:
                return maxi - mini

            mini = min(mini, node.val)
            maxi = max(maxi, node.val)
            return max(dfs(node.left, mini, maxi), dfs(node.right, mini, maxi))

        return dfs(root, root.val, root.val)


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
    output = Solution().maxAncestorDiff(TreeNode.from_list(inputs[0]))
    assert output == expected
