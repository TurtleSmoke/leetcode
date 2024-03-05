import pytest
from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l, r = 0, len(tokens) - 1

        cur_score = res = 0
        while l <= r:
            if tokens[l] <= power:
                power -= tokens[l]
                cur_score += 1
                res = max(cur_score, res)
                l += 1
            elif cur_score > 0:
                power += tokens[r]
                cur_score -= 1
                r -= 1
            else:
                break

        return res


tests = [
    (
        ([100], 50),
        0,
    ),
    (
        ([200, 100], 150),
        1,
    ),
    (
        ([100, 200, 300, 400], 200),
        2,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().bagOfTokensScore(*inputs)
    assert output == expected
