import pytest


class Solution:
    def compressedString(self, word: str) -> str:
        res = ""
        i = 0
        while i < len(word):
            j = i
            while j < len(word) and (j - i) < 9 and word[i] == word[j]:
                j += 1
            res += str(j - i) + word[i]
            i = j
        return res


tests = [
    (
        ("abcde",),
        "1a1b1c1d1e",
    ),
    (
        ("aaaaaaaaaaaaaabb",),
        "9a5a2b",
    ),
    (
        ("abcde",),
        "1a1b1c1d1e",
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().compressedString(*inputs)
    assert output == expected
