from functools import cache

import pytest


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache
        def rec(i, prev_c, len_c, num_del):
            if i == len(s):
                return 0

            if s[i] == prev_c:
                keep = int(len_c in [1, 9, 99]) + rec(i + 1, prev_c, len_c + 1, num_del)
            else:
                keep = 1 + rec(i + 1, s[i], 1, num_del)

            if num_del == 0:
                return keep

            delete = rec(i + 1, prev_c, len_c, num_del - 1)

            return min(delete, keep)

        return rec(0, "", 0, k)


tests = [
    (
        ("aaab", 1),
        2,
    ),
    (
        ("aaabcccd", 2),
        4,
    ),
    (
        ("aabbaa", 2),
        2,
    ),
    (
        ("aaaaaaaaaaa", 0),
        3,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().getLengthOfOptimalCompression(*inputs)
    assert output == expected
