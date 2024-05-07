from typing import Optional

import pytest

from problems.utils import ListNode


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def dfs(node):
            if node is None:
                return

            dfs(node.next)
            node.val *= 2
            if node.next and node.next.val >= 10:
                node.val += node.next.val // 10
                node.next.val %= 10

        if head.val >= 5:
            head = ListNode(0, head)

        dfs(head)
        return head


tests = [
    (
        ([1, 8, 9],),
        [3, 7, 8],
    ),
    (
        ([9, 9, 9],),
        [1, 9, 9, 8],
    ),
    (
        ([5],),
        [1, 0],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().doubleIt(ListNode.from_list(inputs[0]))
    assert ListNode.to_list(output) == expected
