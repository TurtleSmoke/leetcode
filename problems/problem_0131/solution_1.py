from typing import List

import pytest


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = [[s[0]]]
        for i in range(1, len(s)):
            new_res = []
            for sub_str in res:
                new_res.append(sub_str + [s[i]])
                new_res.append(sub_str[:-1] + [sub_str[-1] + s[i]])
            res = new_res

        new_res = []
        for sub_str in res:
            if all(s == s[::-1] for s in sub_str):
                new_res.append(sub_str)

        return new_res


tests = [
    (
        ("aab",),
        [["a", "a", "b"], ["aa", "b"]],
    ),
    (
        ("a",),
        [["a"]],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().partition(*inputs)
    assert sorted(output) == sorted(expected)
