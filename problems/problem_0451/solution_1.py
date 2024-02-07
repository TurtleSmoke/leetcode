import pytest
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join(c * n for c, n in sorted(Counter(s).items(), key=lambda x: -x[1]))


tests = [
    (
        ("tree",),
        "eetr",
    ),
    (
        ("cccaaa",),
        "cccaaa",
    ),
    (
        ("Aabb",),
        "bbAa",
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().frequencySort(*inputs)
    assert output == expected
