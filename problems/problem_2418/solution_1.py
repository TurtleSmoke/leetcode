from typing import List

import pytest


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [names[i] for i in sorted(range(len(heights)), key=lambda x: -heights[x])]


tests = [
    (
        (["Mary", "John", "Emma"], [180, 165, 170]),
        ["Mary", "Emma", "John"],
    ),
    (
        (["Alice", "Bob", "Bob"], [155, 185, 150]),
        ["Bob", "Alice", "Bob"],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().sortPeople(*inputs)
    assert output == expected
