class Solution:
    def reverse(self, x: int) -> int:
        min_max_div_10 = 214748364
        sign = 1 if x >= 0 else -1
        x = sign * x
        res = 0
        while x:
            if res > min_max_div_10 or (
                res == min_max_div_10 and ((sign == 1 and x % 10 > 7) or (sign == -1 and x % 10 > 8))
            ):
                return 0
            res = res * 10 + x % 10
            x //= 10
        return sign * res


tests = [
    (
        (123,),
        321,
    ),
    (
        (-123,),
        -321,
    ),
    (
        (120,),
        21,
    ),
    (
        (1534236469,),
        0,
    ),
    (
        (7463847412,),
        2147483647,
    ),
]
