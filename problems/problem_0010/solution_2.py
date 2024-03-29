class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        for i in range(len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 2] or (i > 0 and dp[i - 1][j] and p[j - 2] in (s[i - 1], "."))
                else:
                    dp[i][j] = i > 0 and dp[i - 1][j - 1] and p[j - 1] in (s[i - 1], ".")
        return dp[-1][-1]


tests = [
    (
        ("aa", "a"),
        False,
    ),
    (
        ("aa", "a*"),
        True,
    ),
    (
        ("ab", ".*"),
        True,
    ),
    (
        ("aab", "c*a*b"),
        True,
    ),
]
