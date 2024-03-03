from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        mini, maxi = min(strs), max(strs)
        res = ""
        for i in range(len(min(mini, maxi))):
            if mini[i] != maxi[i]:
                break
            res += mini[i]
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
    (
        (["", "b"],),
        "",
    ),
]
