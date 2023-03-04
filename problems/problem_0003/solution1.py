class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        start = 0
        max_length = 0
        for i, c in enumerate(s):
            if c in seen and start <= seen[c]:
                start = seen[c] + 1
            else:
                max_length = max(max_length, i - start + 1)
            seen[c] = i
        return max_length


tests = [
    (
        ("abcabcbb",),
        3,
    ),
    (
        ("bbbbb",),
        1,
    ),
    (
        ("pwwkew",),
        3,
    ),
    (
        ("",),
        0,
    ),
    (
        ("tmmzuxt",),
        5,
    )
]
