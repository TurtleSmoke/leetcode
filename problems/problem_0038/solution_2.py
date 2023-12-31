import pytest
import itertools


class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        for _ in range(1, n):
            result = "".join(str(len(list(group))) + digit for digit, group in itertools.groupby(result))
        return result


tests = [
    (
        (1,),
        "1",
    ),
    (
        (4,),
        "1211",
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().countAndSay(*inputs)
    assert output == expected
