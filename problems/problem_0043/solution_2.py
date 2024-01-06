import itertools

import pytest


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        mul_digits = []
        for tenfold, c1 in enumerate(num1[::-1]):
            rest = 0
            cur_res = [0] * tenfold
            for c2 in num2[::-1]:
                (rest, val) = divmod(int(c1) * int(c2) + rest, 10)
                cur_res.append(val)
            if rest > 0:
                cur_res.append(rest)
            mul_digits.append(cur_res)

        res = mul_digits.pop()
        for cur_res in mul_digits:
            rest = 0
            new_res = []
            for d1, d2 in itertools.zip_longest(res, cur_res, fillvalue=0):
                (rest, val) = divmod(d1 + d2 + rest, 10)
                new_res.append(val)
            if rest > 0:
                new_res.append(rest)
            res = new_res
        return "".join(map(str, reversed(res)))


tests = [
    (
        ("2", "3"),
        "6",
    ),
    (
        ("123", "456"),
        "56088",
    ),
    (
        ("9133", "0"),
        "0",
    ),
    (
        ("123456789", "987654321"),
        "121932631112635269",
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().multiply(*inputs)
    assert output == expected
