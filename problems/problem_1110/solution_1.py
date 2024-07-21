from typing import List
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
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        res = []

        def dfs(root, has_parent):
            if root is None:
                return None

            delete = root.val in to_delete
            if not has_parent and not delete:
                res.append(root)
            root.left = dfs(root.left, not delete)
            root.right = dfs(root.right, not delete)
            return None if delete else root

        dfs(root, False)
        return res


tests = [
    (
        ([1, 2, 3, 4, 5, 6, 7], [3, 5]),
        [[1, 2, None, 4], [6], [7]],
    ),
    (
        ([1, 2, 4, None, 3], [3]),
        [[1, 2, 4]],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().delNodes(TreeNode.from_list(inputs[0]), inputs[1])
    output = [TreeNode.to_list(node) for node in output]
    assert output == expected
