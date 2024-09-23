import pytest
from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints = [int(time[:2]) * 60 + int(time[3:]) for time in timePoints]
        timePoints.sort()
        return min((y - x) % (24 * 60) for x, y in zip(timePoints, timePoints[1:] + timePoints[:1]))


tests = [
    (
        (["23:59", "00:00"],),
        1,
    ),
    (
        (["00:00", "23:59", "00:00"],),
        0,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().findMinDifference(*inputs)
    assert output == expected
