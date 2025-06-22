from collections import Counter

import pytest


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        counter = Counter(word)
        res = len(word)
        for a in counter.values():
            deleted = 0
            for b in counter.values():
                if a > b:
                    deleted += b
                elif b > a + k:
                    deleted += b - (a + k)
            res = min(res, deleted)
        return res


tests = [
    (
        ("aabcaba", 0),
        3,
    ),
    (
        ("dabdcbdcdcd", 2),
        2,
    ),
    (
        ("aaabaaa", 2),
        1,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().minimumDeletions(*inputs)
    assert output == expected
