import pytest


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        tenfold1 = 1
        res = 0
        for c1 in num1[::-1]:
            tenfold2 = 1
            for c2 in num2[::-1]:
                res += (ord(c1) - ord("0")) * (ord(c2) - ord("0")) * tenfold1 * tenfold2
                tenfold2 *= 10
            tenfold1 *= 10

        return str(res)


tests = [
    (
        ("2", "3"),
        "6",
    ),
    (
        ("123", "456"),
        "56088",
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().multiply(*inputs)
    assert output == expected
