import pytest
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for i, c in enumerate(s):
            if counter[c] == 1:
                return i

        return -1


tests = [
    (
        ("leetcode",),
        0,
    ),
    (
        ("loveleetcode",),
        2,
    ),
    (
        ("aabb",),
        -1,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().firstUniqChar(*inputs)
    assert output == expected
