from typing import Optional

import pytest

from problems.utils import TreeNode


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        level = 0

        while queue:
            last = float("inf") if level % 2 == 1 else -1
            for _ in range(len(queue)):
                current = queue.pop(0)
                if (level % 2 == 0 and current.val % 2 == 1 and current.val > last) or (
                    level % 2 == 1 and current.val % 2 == 0 and current.val < last
                ):
                    last = current.val
                    queue += filter(None, [current.left, current.right])
                else:
                    return False
            level += 1

        return True


tests = [
    (
        ([1, 10, 4, 3, None, 7, 9, 12, 8, 6, None, None, 2],),
        True,
    ),
    (
        ([5, 4, 2, 3, 3, 7],),
        False,
    ),
    (
        ([5, 9, 1, 3, 5, 7],),
        False,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().isEvenOddTree(TreeNode.list_to_TreeNode(*inputs))
    assert output == expected
