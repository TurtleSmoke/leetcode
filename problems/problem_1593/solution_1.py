import pytest


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def dfs(i, j, taken):
            if i >= len(s) or j >= len(s):
                return 1 if s[i:j] not in taken else 0

            res = 0
            if s[i:j] not in taken:
                taken.add(s[i:j])
                res = 1 + dfs(j, j + 1, taken)
                taken.remove(s[i:j])

            return max(res, dfs(i, j + 1, taken))

        return dfs(0, 1, set())


tests = [
    (
        ("ababccc",),
        5,
    ),
    (
        ("aba",),
        2,
    ),
    (
        ("aa",),
        1,
    ),
    (
        ("aaaa",),
        2,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().maxUniqueSplit(*inputs)
    assert output == expected
