import pytest
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1.sort(key=lambda x: arr2.index(x) if x in arr2 else len(arr2) + x)
        return arr1


tests = [
    (
        ([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]),
        [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19],
    ),
    (
        ([28, 6, 22, 8, 44, 17], [22, 28, 8, 6]),
        [22, 28, 8, 6, 17, 44],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().relativeSortArray(*inputs)
    assert output == expected
