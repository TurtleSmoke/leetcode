import pytest


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_indexes = {}

        res = -1
        for i, c in enumerate(s):
            if c in char_indexes:
                res = max(res, i - char_indexes[c] - 1)
            else:
                char_indexes[c] = i

        return res


tests = [
    (
        ("aa",),
        0,
    ),
    (
        ("abca",),
        2,
    ),
    (
        ("cbzxy",),
        -1,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().maxLengthBetweenEqualCharacters(*inputs)
    assert output == expected
