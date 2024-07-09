import pytest

from problems.utils import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(node, greater):
            if node.right is not None:
                greater = dfs(node.right, greater)

            node.val += greater
            greater = node.val

            if node.left is not None:
                greater = dfs(node.left, greater)

            return greater

        dfs(root, 0)
        return root


tests = [
    (
        ([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8],),
        [30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8],
    ),
    (
        ([0, None, 1],),
        [1, None, 1],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().bstToGst(TreeNode.from_list(inputs[0]))
    assert TreeNode.to_list(output) == expected
