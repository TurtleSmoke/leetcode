from typing import List

import pytest


class Solution:
    class Trie:
        def __init__(self, nums):
            self.root = [None] * 10
            for num in nums:
                node = self.root
                for digit in str(num):
                    idx = int(digit)
                    if not node[idx]:
                        node[idx] = [None] * 10
                    node = node[idx]

        def find_longest_prefix(self, num):
            node = self.root

            res = 0
            for digit in str(num):
                idx = int(digit)
                if node[idx]:
                    res += 1
                    node = node[idx]
                else:
                    break

            return res

    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Solution.Trie(arr1)

        return max(trie.find_longest_prefix(num) for num in arr2)


tests = [
    (
        ([1, 10, 100], [1000]),
        3,
    ),
    (
        ([1, 2, 3], [4, 4, 4]),
        0,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().longestCommonPrefix(*inputs)
    assert output == expected
