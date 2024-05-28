import pytest


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left, right = 0, 0
        for right in range(len(s)):
            maxCost -= abs(ord(s[right]) - ord(t[right]))
            if maxCost < 0:
                maxCost += abs(ord(s[left]) - ord(t[left]))
                left += 1

        return right - left + 1


tests = [
    (
        ("abcd", "bcdf", 3),
        3,
    ),
    (
        ("abcd", "cdef", 3),
        1,
    ),
    (
        ("abcd", "acde", 0),
        1,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().equalSubstring(*inputs)
    assert output == expected
