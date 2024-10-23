import pytest


class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(map(int, str(num)))
        last = {x: i for i, x in enumerate(num)}
        for i, x in enumerate(num):
            for d in range(9, x, -1):
                if last.get(d, -1) > i:
                    num[i], num[last[d]] = num[last[d]], num[i]
                    return int("".join(map(str, num)))
        return int("".join(map(str, num)))


tests = [
    (
        (2736,),
        7236,
    ),
    (
        (9973,),
        9973,
    ),
    (
        (1993,),
        9913,
    ),
    (
        (98368,),
        98863,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().maximumSwap(*inputs)
    assert output == expected
