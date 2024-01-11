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
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        res = 0

        def dfs(node):
            nonlocal res
            if node is None:
                return 0

            left, right = dfs(node.left), dfs(node.right)
            if node.val == start:
                res = max(left, right)
                return -1
            elif left >= 0 and right >= 0:
                return max(left, right) + 1
            else:
                res = max(res, abs(left - right))
                return min(left, right) - 1

        dfs(root)
        return res


tests = [
    (
        ([1, 5, 3, None, 4, 10, 6, 9, 2], 3),
        4,
    ),
    (
        ([1], 1),
        0,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    root, start = inputs
    output = Solution().amountOfTime(TreeNode.list_to_TreeNode(root), start)
    assert output == expected
