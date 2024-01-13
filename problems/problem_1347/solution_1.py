import pytest
from collections import Counter, defaultdict


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s = defaultdict(int, Counter(s))
        t = defaultdict(int, Counter(t))

        return sum(abs(s[key] - t[key]) for key in set(s.keys()) | set(t.keys())) // 2


tests = [
    (
        ("bab", "aba"),
        1,
    ),
    (
        ("leetcode", "practice"),
        5,
    ),
    (
        ("anagram", "mangaar"),
        0,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().minSteps(*inputs)
    assert output == expected
