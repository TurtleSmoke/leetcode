import math

import pytest
from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        bank = [v for v in (sum(c == "1" for c in line) for line in bank) if v > 0]
        return sum(math.prod(devices) for devices in zip(bank, bank[1:], strict=False))


tests = [
    (
        (["011001", "000000", "010100", "001000"],),
        8,
    ),
    (
        (["000", "111", "000"],),
        0,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().numberOfBeams(*inputs)
    assert output == expected
