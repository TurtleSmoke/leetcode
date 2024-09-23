from typing import List

import pytest


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        cur = 1
        for _ in range(n):
            res.append(cur)
            if cur * 10 <= n:
                cur *= 10
            else:
                if cur >= n:
                    cur //= 10
                cur += 1
                while cur % 10 == 0:
                    cur //= 10

        return res


tests = [
    (
        (13,),
        [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9],
    ),
    (
        (2,),
        [1, 2],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().lexicalOrder(*inputs)
    assert output == expected
