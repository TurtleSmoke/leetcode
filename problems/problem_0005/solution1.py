class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        longest = s[0]
        for i in range(len(s)):
            for j in range(len(s) - i + 1):
                substring = s[i : i + j]
                if substring == substring[::-1] and len(substring) > len(longest):
                    longest = substring

        return longest


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
