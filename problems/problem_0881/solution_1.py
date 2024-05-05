from typing import List

import pytest


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res = 0
        people.sort()
        i, j = 0, len(people) - 1
        while i <= j:
            if people[j] + people[i] <= limit:
                i += 1
            j -= 1
            res += 1

        return res


tests = [
    (
        ([1, 2], 3),
        1,
    ),
    (
        ([3, 2, 2, 1], 3),
        3,
    ),
    (
        ([3, 5, 3, 4], 5),
        4,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().numRescueBoats(*inputs)
    assert output == expected
