import pytest
import itertools


class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def createPalindrome(half, odd):
            res = half
            if odd:
                half //= 10
            while half > 0:
                res = res * 10 + half % 10
                half //= 10
            return res

        def isPalindrome(num, base):
            original = num
            reversed_num = 0
            while num > 0:
                reversed_num = reversed_num * base + num % base
                num //= base
            return original == reversed_num

        res = 0
        for length in itertools.count(1):
            start = 10 ** ((length - 1) // 2)
            end = 10 ** ((length + 1) // 2)

            for half in range(start, end):
                pal = createPalindrome(half, length % 2 == 1)
                if isPalindrome(pal, k):
                    res += pal
                    n -= 1
                    if n <= 0:
                        return res
        return -1


tests = [
    (
        (2, 5),
        25,
    ),
    (
        (3, 7),
        499,
    ),
    (
        (7, 17),
        20379000,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().kMirror(*inputs)
    assert output == expected
