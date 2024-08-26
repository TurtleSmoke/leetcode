from typing import List
from problems.utils import Node

import pytest

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: "Node") -> List[int]:
        def dfs(node):
            if not node:
                return []

            res = []
            for child in node.children:
                res += dfs(child)
            res.append(node.val)
            return res

        return dfs(root)


tests = [
    (
        ([1, None, 3, 2, 4, None, 5, 6],),
        [5, 6, 3, 2, 4, 1],
    ),
    (
        (
            [
                1,
                None,
                2,
                3,
                4,
                5,
                None,
                None,
                6,
                7,
                None,
                8,
                None,
                9,
                10,
                None,
                None,
                11,
                None,
                12,
                None,
                13,
                None,
                None,
                14,
            ],
        ),
        [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().postorder(Node.from_list(inputs[0]))
    assert output == expected
