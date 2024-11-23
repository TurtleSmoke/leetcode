from typing import List

import pytest


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        res = [["."] * len(box) for _ in range(len(box[0]))]
        for i in range(len(box)):
            pos = len(box[0]) - 1
            for j in range(len(box[0]) - 1, -1, -1):
                if box[i][j] == "*":
                    res[j][len(box) - 1 - i] = "*"
                    pos = j - 1
                elif box[i][j] == "#":
                    res[pos][len(box) - 1 - i] = "#"
                    pos -= 1
        return res


tests = [
    (
        ([["#", ".", "#"]],),
        [["."], ["#"], ["#"]],
    ),
    (
        ([["#", ".", "*", "."], ["#", "#", "*", "."]],),
        [["#", "."], ["#", "#"], ["*", "*"], [".", "."]],
    ),
    (
        ([["#", "#", "*", ".", "*", "."], ["#", "#", "#", "*", ".", "."], ["#", "#", "#", ".", "#", "."]],),
        [[".", "#", "#"], [".", "#", "#"], ["#", "#", "*"], ["#", "*", "."], ["#", ".", "*"], ["#", ".", "."]],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().rotateTheBox(*inputs)
    assert output == expected
