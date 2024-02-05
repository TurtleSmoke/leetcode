import pytest
from typing import List
from collections import Counter, defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            anagrams[tuple(sorted(word))].append(word)
        return list(anagrams.values())


tests = [
    (
        (["eat", "tea", "tan", "ate", "nat", "bat"],),
        [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
    ),
    (
        ([""],),
        [[""]],
    ),
    (
        (["a"],),
        [["a"]],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().groupAnagrams(*inputs)
    assert sorted(map(sorted, output)) == sorted(map(sorted, expected))
