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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, path):
            if node is None:
                return 0

            path = path * 10 + node.val
            if node.left is None and node.right is None:
                return path

            return dfs(node.left, path) + dfs(node.right, path)

        return dfs(root, 0)


tests = [
    (
        ([1, 2, 3],),
        25,
    ),
    (
        ([4, 9, 0, 5, 1],),
        1026,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().sumNumbers(TreeNode.from_list(inputs[0]))
    assert output == expected
