from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = ""
        for i in range(len(strs[0])):
            if any(i >= len(s) or s[i] != strs[0][i] for s in strs[1:]):
                return res
            res += strs[0][i]
        return res


tests = [
    (
        (["flower", "flow", "flight"],),
        "fl",
    ),
    (
        (["dog", "racecar", "car"],),
        "",
    ),
]
