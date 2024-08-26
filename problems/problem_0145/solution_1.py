import pytest
from typing import List
from typing import Optional
from problems.utils import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def bfs(node):
            if node is None:
                return []
            res = bfs(node.left)
            res += bfs(node.right)
            return res + [node.val]

        return bfs(root)


tests = [
    (
        ([1, None, 2, 3],),
        [3, 2, 1],
    ),
    (
        ([],),
        [],
    ),
    (
        ([1],),
        [1],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().postorderTraversal(TreeNode.from_list(inputs[0]))
    assert output == expected
