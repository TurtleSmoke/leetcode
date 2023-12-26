class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        res = numerals[s[-1]]
        for i in range(len(s) - 1):
            if numerals[s[i]] < numerals[s[i + 1]]:
                res -= numerals[s[i]]
            else:
                res += numerals[s[i]]

        return res


tests = [
    (
        ("III",),
        3,
    ),
    (
        ("IV",),
        4,
    ),
    (
        ("IX",),
        9,
    ),
    (
        ("LVIII",),
        58,
    ),
    (
        ("MCMXCIV",),
        1994,
    ),
]
