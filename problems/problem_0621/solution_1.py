from collections import Counter
from typing import List

import pytest


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks).values()
        max_count = max(task_counts)
        max_count_tasks = sum(count == max_count for count in task_counts)
        return max(len(tasks), (max_count - 1) * (n + 1) + max_count_tasks)


tests = [
    (
        (["A", "A", "A", "B", "B", "B"], 2),
        8,
    ),
    (
        (["A", "C", "A", "B", "D", "B"], 1),
        6,
    ),
    (
        (["A", "A", "A", "B", "B", "B"], 3),
        10,
    ),
    (
        (["A", "B", "C", "D", "E", "A", "B", "C", "D", "E"], 4),
        10,
    ),
    (
        (["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 1),
        12,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().leastInterval(*inputs)
    assert output == expected
