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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, is_left):
            if node is None:
                return 0

            if node.left is None and node.right is None and is_left:
                return node.val

            return dfs(node.left, True) + dfs(node.right, False)

        return dfs(root, False)


tests = [
    (
        ([3, 9, 20, None, None, 15, 7],),
        24,
    ),
    (
        ([1],),
        0,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().sumOfLeftLeaves(TreeNode.from_list(inputs[0]))
    assert output == expected
