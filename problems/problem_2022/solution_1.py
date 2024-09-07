import pytest
from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []

        return [[original[j * n + i] for i in range(n)] for j in range(m)]


tests = [
    (
        ([1, 2, 3, 4], 2, 2),
        [[1, 2], [3, 4]],
    ),
    (
        ([1, 2, 3], 1, 3),
        [[1, 2, 3]],
    ),
    (
        ([1, 2], 1, 1),
        [],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().construct2DArray(*inputs)
    assert output == expected
