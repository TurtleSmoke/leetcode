import pytest
from collections import Counter
from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = Counter(arr)
        distinct = [key for key, value in counter.items() if value == 1]
        if k > len(distinct):
            return ""

        return distinct[k - 1]


tests = [
    (
        (["d", "b", "c", "b", "c", "a"], 2),
        "a",
    ),
    (
        (["a", "b", "c", "b", "c", "d"], 2),
        "d",
    ),
    (
        (["aaa", "aa", "a"], 1),
        "aaa",
    ),
    (
        (["a", "b", "a"], 3),
        "",
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().kthDistinct(*inputs)
    assert output == expected
