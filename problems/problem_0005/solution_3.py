class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        dp = [[False] * len(s), [True] * len(s)]

        res = s[0]
        for left in range(len(s) - 1):
            if s[left] == s[left + 1]:
                dp[0][left] = True
                res = s[left : left + 2]

        for size in range(3, len(s) + 1):
            for left in range(len(s) + 1 - size):
                mid = left + (size - 1) // 2
                dp[size % 2][mid] = dp[size % 2][mid] and s[left] == s[left + size - 1]
                if dp[size % 2][mid] and size > len(res):
                    res = s[left : left + size]
        return res


tests = [
    (
        ("babcd",),
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
    (
        ("joqfacbdeedbcaljqwq",),
        "acbdeedbca",
    ),
    (
        ("ccc",),
        "ccc",
    ),
]
