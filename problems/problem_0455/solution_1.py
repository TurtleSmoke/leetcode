import pytest
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        res = 0
        i, j = 0, 0

        while i + j < len(g) and i < len(s):
            if g[i + j] <= s[i]:
                res += 1
                i += 1
            else:
                j += 1

        return res


tests = [
    (
        ([1, 2, 3], [1, 1]),
        1,
    ),
    (
        ([1, 2], [1, 2, 3]),
        2,
    ),
    (
        ([1, 2, 3], []),
        0,
    ),
    (
        ([1, 2, 3], [3]),
        1,
    ),
    (
        ([10, 9, 8, 7], [5, 6, 7, 8]),
        2,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().findContentChildren(*inputs)
    assert output == expected
