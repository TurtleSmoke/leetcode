import pytest


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n and not (n & n - 1)


tests = [
    (
        (1,),
        True,
    ),
    (
        (16,),
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
    output = Solution().isPowerOfTwo(*inputs)
    assert output == expected
