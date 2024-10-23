import pytest
from typing import Optional
from problems.utils import TreeNode
from collections import deque


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        dq = deque([root])
        res = []
        while dq:
            level_sum = 0
            for _ in range(len(dq)):
                node = dq.popleft()
                level_sum += node.val
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            res.append(level_sum)

        if k > len(res):
            return -1

        return sorted(res, reverse=True)[k - 1]


tests = [
    (
        ([5, 8, 9, 2, 1, 3, 7, 4, 6], 2),
        13,
    ),
    (
        ([1, 2, None, 3], 1),
        3,
    ),
    (
        ([5, 8, 9, 2, 1, 3, 7], 4),
        -1,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().kthLargestLevelSum(TreeNode.from_list(inputs[0]), inputs[1])
    assert output == expected
