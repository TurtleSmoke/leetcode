import pytest
from typing import List
from collections import Counter


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        return any(2 * x in cnt and x != 0 for x in arr) or cnt[0] > 1


tests = [
    (
        ([10, 2, 5, 3],),
        True,
    ),
    (
        ([3, 1, 7, 11],),
        False,
    ),
    (
        ([7, 1, 14, 11],),
        True,
    ),
    (
        ([-2, 0, 10, -19, 4, 6, -8],),
        False,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().checkIfExist(*inputs)
    assert output == expected
