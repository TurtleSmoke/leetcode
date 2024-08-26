import heapq
from collections import defaultdict
from typing import List

import pytest


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], costs: List[int]) -> int:
        graph = defaultdict(list)
        for s, d, c in zip(original, changed, costs):
            graph[s].append((d, c))

        def shortest_path(start, end):
            heap = [(0, start)]
            visited = set()
            while heap:
                cost, current = heapq.heappop(heap)
                visited.add(current)
                if current == end:
                    return cost
                for nn, cc in graph[current]:
                    if nn not in visited:
                        heapq.heappush(heap, (cost + cc, nn))

            return -1

        res = 0
        cache = {}
        for i in range(len(source)):
            if (source[i], target[i]) in cache:
                res += cache[(source[i], target[i])]
                continue
            cost = shortest_path(source[i], target[i])
            if cost == -1:
                return -1
            cache[(source[i], target[i])] = cost
            res += cost

        return res


tests = [
    (
        ("abcd", "acbe", ["a", "b", "c", "c", "e", "d"], ["b", "c", "b", "e", "b", "e"], [2, 5, 5, 1, 2, 20]),
        28,
    ),
    (
        ("aaaa", "bbbb", ["a", "c"], ["c", "b"], [1, 2]),
        12,
    ),
    (
        ("abcd", "abce", ["a"], ["e"], [10000]),
        -1,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().minimumCost(*inputs)
    assert output == expected
