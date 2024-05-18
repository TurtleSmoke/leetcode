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
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(node, parent):
            if not node:
                return 0
            moves = dfs(node.left, node) + dfs(node.right, node)
            if parent:
                parent.val += node.val - 1
            moves += abs(node.val - 1)
            return moves

        return dfs(root, None)


tests = [
    (
        ([3, 0, 0],),
        2,
    ),
    (
        ([0, 3, 0],),
        3,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().distributeCoins(TreeNode.from_list(inputs[0]))
    assert output == expected
