from typing import Optional

import pytest

from problems.utils import ListNode
from problems.utils import TreeNode


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        sub_path = []
        while head:
            sub_path.append(head.val)
            head = head.next

        suffix_dp = [0] * len(sub_path)
        j = 0
        for i in range(1, len(sub_path)):
            while j and sub_path[i] != sub_path[j]:
                j = suffix_dp[j - 1]
            j += sub_path[i] == sub_path[j]
            suffix_dp[i] = j

        def dfs(root, i):
            if not root:
                return False
            while i and root.val != sub_path[i]:
                i = suffix_dp[i - 1]
            i += root.val == sub_path[i]
            return i == len(suffix_dp) or dfs(root.left, i) or dfs(root.right, i)

        return dfs(root, 0)


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
