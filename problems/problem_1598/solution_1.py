import pytest
from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        for log in logs:
            if log == "../":
                res = max(0, res - 1)
            elif log == "./":
                continue
            else:
                res += 1
        return res


tests = [
    (
        (["d1/", "d2/", "../", "d21/", "./"],),
        2,
    ),
    (
        (["d1/", "d2/", "./", "d3/", "../", "d31/"],),
        3,
    ),
    (
        (["d1/", "../", "../", "../"],),
        0,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().minOperations(*inputs)
    assert output == expected
