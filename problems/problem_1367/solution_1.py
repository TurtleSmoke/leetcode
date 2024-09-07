from typing import Optional

import pytest

from problems.utils import ListNode
from problems.utils import TreeNode


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(head, root):
            if not head:
                return True
            if not root:
                return False
            return head.val == root.val and (dfs(head.next, root.left) or dfs(head.next, root.right))

        if not head:
            return True
        if not root:
            return False
        return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)


tests = [
    (
        ([4, 2, 8], [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3]),
        True,
    ),
    (
        ([1, 4, 2, 6], [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3]),
        True,
    ),
    (
        ([1, 4, 2, 6, 8], [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3]),
        False,
    ),
    (
        ([1, 10], [1, None, 1, 10, 1, 9]),
        True,
    ),
    (
        ([2, 2, 1], [2, None, 2, None, 2, None, 1]),
        True,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().isSubPath(ListNode.from_list(inputs[0]), TreeNode.from_list(inputs[1]))
    assert output == expected
