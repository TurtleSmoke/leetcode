import pytest
from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        res = 0
        for t in trainers:
            if players[res] <= t:
                res += 1
            if res >= len(players):
                break

        return res


tests = [
    (
        ([4, 7, 9], [8, 2, 5, 8]),
        2,
    ),
    (
        ([1, 1, 1], [10]),
        1,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().matchPlayersAndTrainers(*inputs)
    assert output == expected
