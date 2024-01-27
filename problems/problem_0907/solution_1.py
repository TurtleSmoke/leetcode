from typing import List

import pytest


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res = 0
        mod = 10**9 + 7
        stack = []
        arr = [0] + arr + [0]
        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                j = stack.pop()
                k = stack[-1]
                res += arr[j] * (i - j) * (j - k) % mod
            stack.append(i)

        return res % mod


tests = [
    (
        ([3, 1, 2, 4],),
        17,
    ),
    (
        ([11, 81, 94, 43, 3],),
        444,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().sumSubarrayMins(*inputs)
    assert output == expected
