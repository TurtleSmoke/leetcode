import pytest


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(c**0.5) + 1):
            tmp = c - i * i
            if int(tmp**0.5) ** 2 == tmp:
                return True
        return False


tests = [
    (
        (5,),
        True,
    ),
    (
        (3,),
        False,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().judgeSquareSum(*inputs)
    assert output == expected
