from typing import Optional

import pytest

from problems.utils import TreeNode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            return root1.val == root2.val and dfs(root1.left, root2.left) and dfs(root1.right, root2.right)

        return dfs(p, q)


tests = [
    (
        ([1, 2, 3], [1, 2, 3]),
        True,
    ),
    (
        ([1, 2], [1, None, 2]),
        False,
    ),
    (
        ([1, 2, 1], [1, 1, 2]),
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
    output = Solution().isSameTree(TreeNode.list_to_TreeNode(root1), TreeNode.list_to_TreeNode(root2))
    assert output == expected
