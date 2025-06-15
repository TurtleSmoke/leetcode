import pytest


class Solution:
    def maxDiff(self, num: int) -> int:
        num = str(num)
        max_num = int(num.replace(next((c for c in num if c != "9"), "9"), "9"))
        min_num1 = int(num.replace(next((c for c in num if c != num[0] and c != "0"), "0"), "0"))
        min_num2 = int(num.replace(num[0], "1"))
        return max_num - min(min_num1, min_num2)


tests = [
    (
        (555,),
        888,
    ),
    (
        (9,),
        8,
    ),
    (
        (123456,),
        820000,
    ),
    (
        (9288,),
        8700,
    ),
    (
        (1101057,),
        8808050,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().maxDiff(*inputs)
    assert output == expected
