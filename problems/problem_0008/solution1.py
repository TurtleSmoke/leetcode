class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        min_max_div_10 = 214748364
        while i < len(s) and s[i] == " ":
            i += 1

        sign = 1
        if i < len(s) and s[i] in ("-", "+"):
            if s[i] == "-":
                sign = -1
            i += 1

        res = 0
        while i < len(s) and s[i].isdigit():
            if res > min_max_div_10 or (res == min_max_div_10 and int(s[i]) > 7):
                return 2147483647 if sign == 1 else -2147483648
            res = res * 10 + int(s[i])
            i += 1

        return sign * res


tests = [
    (
        ("42",),
        42,
    ),
    (
        ("   -42",),
        -42,
    ),
    (
        ("4193 with words",),
        4193,
    ),
    (
        ("",),
        0,
    ),
    (
        ("words and 987",),
        0,
    ),
    (
        ("21474836460",),
        2147483647,
    ),
    (
        ("-91283472332",),
        -2147483648,
    ),
    (
        ("-2147483649",),
        -2147483648,
    ),
]
