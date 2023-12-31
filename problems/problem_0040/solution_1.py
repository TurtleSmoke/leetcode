from typing import List
import pytest
from collections import Counter


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = Counter(candidates)
        sorted_keys = list(sorted(candidates.keys()))
        res = []

        def dfs(target, path, idx):
            if target == 0:
                return res.append(path)

            for i, digit in enumerate(sorted_keys[idx:]):
                if candidates[digit] > 0 and digit <= target:
                    candidates[digit] -= 1
                    dfs(target - digit, path + [digit], idx + i)
                    candidates[digit] += 1
            return res

        dfs(target, [], 0)
        return res


tests = [
    (
        ([10, 1, 2, 7, 6, 1, 5], 8),
        [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]],
    ),
    (
        ([2, 5, 2, 1, 2], 5),
        [[1, 2, 2], [5]],
    ),
    (
        ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 27),
        [],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().combinationSum2(*inputs)
    assert output == expected
