import pytest
from collections import Counter
from typing import List


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        self.res = 0
        words_score = [sum(score[ord(c) - ord("a")] for c in word) for word in words]
        words_counter = [Counter(word) for word in words]

        def dfs(i, curr_score, remaining_letters):
            if curr_score + sum(words_score[i:]) <= self.res:
                return

            self.res = max(self.res, curr_score)
            for j, word_counter in enumerate(words_counter[i:], i):
                if all(n <= remaining_letters.get(c, 0) for c, n in word_counter.items()):
                    dfs(j + 1, curr_score + words_score[j], remaining_letters - word_counter)

        dfs(0, 0, Counter(letters))
        return self.res


tests = [
    (
        (
            ["dog", "cat", "dad", "good"],
            ["a", "a", "c", "d", "d", "d", "g", "o", "o"],
            [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ),
        23,
    ),
    (
        (
            ["xxxz", "ax", "bx", "cx"],
            ["z", "a", "b", "c", "x", "x", "x"],
            [4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 10],
        ),
        27,
    ),
    (
        (
            ["leetcode"],
            ["l", "e", "t", "c", "o", "d"],
            [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        ),
        0,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().maxScoreWords(*inputs)
    assert output == expected
