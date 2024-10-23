from collections import deque, defaultdict
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
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dq = deque([(root, 1)])
        while dq:
            cousins = defaultdict(int)
            for i in range(len(dq)):
                node, parent_id = dq[i]
                cousins[parent_id] += node.val

            for i in range(len(dq)):
                node, parent_id = dq.popleft()
                if node.left:
                    dq.append((node.left, i))
                if node.right:
                    dq.append((node.right, i))
                node.val = sum(cousins.values()) - cousins[parent_id]

        return root


tests = [
    (
        ([5, 4, 9, 1, 10, None, 7],),
        [0, 0, 0, 7, 7, None, 11],
    ),
    (
        ([3, 1, 2],),
        [0, 0, 0],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().replaceValueInTree(TreeNode.from_list(*inputs))
    assert TreeNode.to_list(output) == expected
