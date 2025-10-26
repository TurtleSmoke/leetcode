import pytest
import itertools
from collections import Counter


class Solution:
    def isBalanced(self, i):
        return all(int(k) == v for k, v in Counter(str(i)).items())

    def nextBeautifulNumber(self, n: int) -> int:
        for i in itertools.count(n + 1):
            if self.isBalanced(i):
                return i
        return -1


tests = [
    (
        (1,),
        22,
    ),
    (
        (1000,),
        1333,
    ),
    (
        (3000,),
        3133,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().nextBeautifulNumber(*inputs)
    assert output == expected
