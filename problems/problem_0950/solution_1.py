from typing import List

import pytest


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck = sorted(deck)
        res = [0] * len(deck)
        q = list(range(len(deck)))
        for i in deck:
            res[q.pop(0)] = i
            if q:
                q.append(q.pop(0))

        return res


tests = [
    (
        ([17, 13, 11, 2, 3, 5, 7],),
        [2, 13, 3, 11, 5, 17, 7],
    ),
    (
        ([1, 1000],),
        [1, 1000],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().deckRevealedIncreasing(*inputs)
    assert output == expected
