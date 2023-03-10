class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        res = ""
        for i in range(len(roman)):
            k = num // value[i]
            res += roman[i] * k
            num -= k * value[i]
        return res


tests = [
    (
        (3,),
        "III",
    ),
    (
        (4,),
        "IV",
    ),
    (
        (58,),
        "LVIII",
    ),
    (
        (1994,),
        "MCMXCIV",
    ),
]
