import pytest


class Solution:
    def minimumDeletions(self, s: str) -> int:
        res = 0
        nbr_b = 0
        for _, c in enumerate(s):
            if c == "b":
                nbr_b += 1
            else:
                res = min(res + 1, nbr_b)

        return res


tests = [
    (
        ("aababbab",),
        2,
    ),
    (
        ("bbaaaaabb",),
        2,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().minimumDeletions(*inputs)
    assert output == expected
