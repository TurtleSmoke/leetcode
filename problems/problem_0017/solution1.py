from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = [""]
        map_digits_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        for d in digits:
            res = [l + f for l in res for f in map_digits_to_letters[d]]
        return res


tests = [
    (
        ("23",),
        ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
    ),
    (
        ("",),
        [],
    ),
    (
        ("2",),
        ["a", "b", "c"],
    ),
]
