import pytest


class Solution:
    def minMaxDifference(self, num: int) -> int:
        num = str(num)
        max_num = int(num.replace(next((c for c in num if c != "9"), "9"), "9"))
        min_num = int(num.replace(num[0], "0"))
        return max_num - min_num


tests = [
    (
        (11891,),
        99009,
    ),
    (
        (90,),
        99,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().minMaxDifference(*inputs)
    assert output == expected
