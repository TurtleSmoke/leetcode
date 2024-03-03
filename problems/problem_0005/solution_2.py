import itertools


def max_palindrome(s: str, mid: int, even: int) -> str:
    for j in itertools.count(0):
        if s[mid - j] != s[mid + j + even]:
            return s[mid - j + 1 : mid + j + even]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        return max(
            (max_palindrome("#" + s + "^", mid + 1, even) for mid in range(len(s)) for even in (0, 1)),
            key=len,
        )


tests = [
    (
        ("babad",),
        "bab",
    ),
    (
        ("cbbd",),
        "bb",
    ),
    (
        ("a",),
        "a",
    ),
    (
        ("",),
        "",
    ),
]
