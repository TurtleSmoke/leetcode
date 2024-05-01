from collections import deque

import pytest
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(node):
            for i in range(4):
                x = int(node[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    yield node[:i] + str(y) + node[i + 1 :]

        deadends = set(deadends)
        if "0000" in deadends:
            return -1

        q = deque(["0000"])
        steps = 0
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == target:
                    return steps
                for neighbor in neighbors(curr):
                    if neighbor in deadends:
                        continue
                    deadends.add(neighbor)
                    q.append(neighbor)
            steps += 1

        return -1


tests = [
    (
        (["0201", "0101", "0102", "1212", "2002"], "0202"),
        6,
    ),
    (
        (["8888"], "0009"),
        1,
    ),
    (
        (["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888"),
        -1,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().openLock(*inputs)
    assert output == expected
