import pytest


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        limits = {c: s.count(c) - k for c in "abc"}
        if any(x < 0 for x in limits.values()):
            return -1

        current = {c: 0 for c in "abc"}
        res = 0
        l = 0
        for r, c in enumerate(s):
            current[c] += 1
            while current[c] > limits[c]:
                current[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return len(s) - res


tests = [
    (
        ("aabaaaacaabc", 2),
        8,
    ),
    (
        ("a", 1),
        -1,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().takeCharacters(*inputs)
    assert output == expected
