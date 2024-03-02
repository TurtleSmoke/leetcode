from typing import List

import pytest
from math import sqrt


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        parent = list(range(len(nums)))
        set_size = [1 for i in range(len(nums))]

        def get_parent(x):
            if parent[x] == x:
                return x
            parent[x] = get_parent(parent[x])
            return parent[x]

        def union_set(x, y):
            x, y = get_parent(x), get_parent(y)
            if x != y:
                if set_size[x] < set_size[y]:
                    x, y = y, x
                parent[y] = x
                set_size[x] += set_size[y]

        def get_prime_factors(x):
            for j in range(2, int(sqrt(x)) + 1):
                if x % j == 0:
                    while x % j == 0:
                        x //= j
                    yield j

            if x != 1:
                yield x

        seen = {}
        for i in range(len(nums)):
            if nums[i] == 1:
                return False

            for prime in get_prime_factors(nums[i]):
                if prime in seen:
                    union_set(i, seen[prime])
                else:
                    seen[prime] = i

        return set_size[get_parent(0)] == len(nums)


tests = [
    (
        ([2, 3, 6],),
        True,
    ),
    (
        ([3, 9, 5],),
        False,
    ),
    (
        ([4, 3, 12, 8],),
        True,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().canTraverseAllPairs(*inputs)
    assert output == expected
