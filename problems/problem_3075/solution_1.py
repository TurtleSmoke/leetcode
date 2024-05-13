import pytest
from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        sorted_happiness = sorted(happiness, reverse=True)[:k]
        return sum(max(0, v - i) for i, v in enumerate(sorted_happiness))


tests = [
    (
        ([1, 2, 3], 2),
        4,
    ),
    (
        ([1, 1, 1, 1], 2),
        1,
    ),
    (
        ([2, 3, 4, 5], 1),
        5,
    ),
    (
        ([2, 83, 62], 3),
        144,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().maximumHappinessSum(*inputs)
    assert output == expected
