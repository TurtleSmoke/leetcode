import pytest
from typing import Optional
from problems.utils import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def dfs(node, path):
            if not node:
                return 0

            path ^= 1 << node.val
            if not node.left and not node.right and path.bit_count() <= 1:
                return 1
            return dfs(node.left, path) + dfs(node.right, path)

        return dfs(root, 0)


tests = [
    (
        ([2, 3, 1, 3, 1, None, 1],),
        2,
    ),
    (
        ([2, 1, 1, 1, 3, None, None, None, None, None, 1],),
        1,
    ),
    (
        ([9],),
        1,
    ),
    (
        ([1, 2, None, 1, None, 2, None, 1, None, 2, None, 1, None, 2, None],),
        1,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    root = TreeNode.list_to_TreeNode(inputs[0])
    output = Solution().pseudoPalindromicPaths(root)
    assert output == expected
