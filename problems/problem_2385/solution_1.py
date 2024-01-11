from collections import defaultdict
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
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)

        def dfs(node):
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                dfs(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                dfs(node.right)

        dfs(root)
        visited = set()
        queue = [start]
        time = -1
        while queue:
            next_queue = []
            for node in queue:
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        next_queue.append(neighbor)
            queue = next_queue
            time += 1

        return time


tests = [
    (
        ([1, 5, 3, None, 4, 10, 6, 9, 2], 3),
        4,
    ),
    (
        ([1], 1),
        0,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    root, start = inputs
    output = Solution().amountOfTime(TreeNode.list_to_TreeNode(root), start)
    assert output == expected
