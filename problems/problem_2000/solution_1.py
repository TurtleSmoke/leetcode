import pytest


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)
        if idx == -1:
            return word

        return word[idx::-1] + word[idx + 1 :]


tests = [
    (
        ("abcdefd", "d"),
        "dcbaefd",
    ),
    (
        ("xyxzxe", "z"),
        "zxyxxe",
    ),
    (
        ("abcd", "z"),
        "abcd",
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().reversePrefix(*inputs)
    assert output == expected
