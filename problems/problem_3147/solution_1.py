import pytest
from typing import List


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        for i in range(len(energy) - k - 1, -1, -1):
            energy[i] += energy[i + k]
        return max(energy)


tests = [
    (
        ([5, 2, -10, -5, 1], 3),
        3,
    ),
    (
        ([-2, -3, -1], 2),
        -1,
    ),
    (
        ([5, -10, 4, 3, 5, -9, 9, -7], 2),
        23,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().maximumEnergy(*inputs)
    assert output == expected
