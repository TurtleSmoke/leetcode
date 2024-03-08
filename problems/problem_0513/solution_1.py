import pytest
from typing import Optional

from problems.utils import TreeNode


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        node = root
        while queue:
            node = queue.pop(0)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)

        return node.val


tests = [
    (
        ([2, 1, 3],),
        1,
    ),
    (
        ([1, 2, 3, 4, None, 5, 6, None, None, 7],),
        7,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().findBottomLeftValue(TreeNode.from_list(*inputs))
    assert output == expected
