class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x and x % 10 == 0):
            return False

        right = 0
        while x > right:
            right = right * 10 + x % 10
            x //= 10

        return x in (right, right // 10)


tests = [
    (
        (121,),
        True,
    ),
    (
        (-121,),
        False,
    ),
    (
        (10,),
        False,
    ),
    (
        (-101,),
        False,
    ),
]
