import pytest
from typing import Optional

from problems.utils import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            left, right = dfs(node.left), dfs(node.right)
            res = max(res, left + right)
            return 1 + max(left, right)

        dfs(root)
        return res


tests = [
    (
        ([1, 2, 3, 4, 5],),
        3,
    ),
    (
        ([1, 2],),
        1,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    input = TreeNode.from_list(inputs[0])
    output = Solution().diameterOfBinaryTree(input)
    assert output == expected
