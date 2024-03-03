class Solution:
    def longestPalindrome(self, s: str) -> str:
        sbogus = "^#" + "#".join(s) + "#$"
        dp = [0] * len(sbogus)
        res = ""
        center, max_right = 0, 0
        for mid in range(1, len(sbogus) - 1):
            if mid < max_right:
                dp[mid] = min(dp[2 * center - mid], max_right - mid)

            while sbogus[mid + dp[mid] + 1] == sbogus[mid - dp[mid] - 1]:
                dp[mid] += 1

            if mid + dp[mid] > max_right:
                center, max_right = mid, mid + dp[mid]

            if dp[mid] > len(res):
                res = s[(mid - dp[mid]) // 2 : (mid + dp[mid]) // 2]

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
