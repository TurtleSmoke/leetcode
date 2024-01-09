import pytest
from typing import Optional
from problems.utils import TreeNode
import itertools


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node.left:
                yield from dfs(node.left)
            if node.right:
                yield from dfs(node.right)
            if not node.left and not node.right:
                yield node.val

        return all(a == b for a, b in itertools.zip_longest(dfs(root1), dfs(root2)))


tests = [
    (
        ([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4], [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]),
        True,
    ),
    (
        ([1, 2, 3], [1, 3, 2]),
        False,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    root1, root2 = inputs
    output = Solution().leafSimilar(TreeNode.list_to_TreeNode(root1), TreeNode.list_to_TreeNode(root2))
    assert output == expected
