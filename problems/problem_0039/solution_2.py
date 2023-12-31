import pytest
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = list(sorted(candidates))

        res = []

        def dfs(idx, target, path):
            if target == 0:
                res.append(path)

            for i, num in enumerate(candidates[idx:]):
                if num > target:
                    break
                dfs(idx + i, target - num, path + [num])

        dfs(0, target, [])
        return res


tests = [
    (
        ([2, 3, 6, 7], 7),
        [[2, 2, 3], [7]],
    ),
    (
        ([2, 3, 5], 8),
        [[2, 2, 2, 2], [2, 3, 3], [3, 5]],
    ),
    (
        ([2], 1),
        [],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().combinationSum(*inputs)
    assert output == expected
