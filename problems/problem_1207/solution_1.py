import pytest
from typing import List
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occ = Counter(arr)
        return len(set(occ.values())) == len(occ.values())


tests = [
    (
        ([1, 2, 2, 1, 1, 3],),
        True,
    ),
    (
        ([1, 2],),
        False,
    ),
    (
        ([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0],),
        True,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().uniqueOccurrences(*inputs)
    assert output == expected
