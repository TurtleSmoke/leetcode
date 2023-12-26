from typing import List
import pytest
from collections import Counter, defaultdict


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        word_len = len(words[0])
        words_len = len(words) * word_len
        words = Counter(words)
        if not s or not words or len(s) < words_len:
            return []
        for offset in range(word_len):
            (substring_start, current_word_start) = (offset, offset)
            current_words = defaultdict(int)
            while substring_start + words_len <= len(s):
                subword = s[current_word_start : current_word_start + word_len]
                current_word_start += word_len
                if subword not in words:
                    substring_start = current_word_start
                    current_words.clear()
                else:
                    current_words[subword] += 1
                    while current_words[subword] > words[subword]:
                        current_words[s[substring_start : substring_start + word_len]] -= 1
                        substring_start += word_len
                    if current_word_start - substring_start == words_len:
                        res.append(substring_start)
        return res


tests = [
    (
        ("barfoothefoobarman", ["foo", "bar"]),
        [0, 9],
    ),
    (
        ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]),
        [],
    ),
    (
        ("barfoofoobarthefoobarman", ["bar", "foo", "the"]),
        [6, 9, 12],
    ),
    (
        ("a" * 10000, ["a"] * 5000),
        list(range(5001)),
    ),
    (
        ("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]),
        [8],
    ),
]


@pytest.mark.timeout(20)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().findSubstring(*inputs)
    assert output == expected
