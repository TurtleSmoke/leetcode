import pytest


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        res = [0] * (len(num1) + len(num2))
        for i2, d2 in enumerate(num1[::-1]):
            for i1, d1 in enumerate(num2[::-1]):
                idx = i1 + i2
                rest, val = divmod(int(d1) * int(d2) + res[idx], 10)
                res[idx] = val
                res[idx + 1] += rest

        if res[-1] == 0:
            res.pop()

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
