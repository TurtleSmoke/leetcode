import pytest


class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        dirs = {"N": 1, "S": -1, "E": 1j, "W": -1j}
        pos, res = 0, 0
        for i, c in enumerate(s):
            pos += dirs[c]
            res = max(res, min(abs(pos.real) + abs(pos.imag) + 2 * k, i + 1))
        return int(res)


tests = [
    (
        ("NN", 1),
        2,
    ),
    (
        ("NWSE", 1),
        3,
    ),
    (
        ("NSWWEW", 3),
        6,
    ),
    (
        ("NWSE", 1),
        3,
    ),
]


@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().maxDistance(*inputs)
    assert output == expected
