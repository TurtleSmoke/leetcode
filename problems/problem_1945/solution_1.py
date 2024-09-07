import pytest


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res = "".join(map(lambda x: str(ord(x) - 96), s))
        for _ in range(k):
            res = str(sum(map(int, res)))
        return int(res)


tests = [
    (
        ("iiii", 1),
        36,
    ),
    (
        ("leetcode", 2),
        6,
    ),
    (
        ("zbax", 2),
        8,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().getLucky(*inputs)
    assert output == expected
