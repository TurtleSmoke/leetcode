import pytest


class Solution:
    def areSentencesSimilar(self, sentences1: str, sentence2: str) -> bool:
        words1, words2 = map(str.split, (sentences1, sentence2))
        if len(words1) > len(words2):
            (words1, words2) = (words2, words1)

        left, right = 0, len(words1) - 1
        while left <= right and words1[left] == words2[left]:
            left += 1
        while right >= left and words1[right] == words2[right + len(words2) - len(words1)]:
            right -= 1

        return left > right


tests = [
    (
        ("My name is Haley", "My Haley"),
        True,
    ),
    (
        ("of", "A lot of words"),
        False,
    ),
    (
        ("Eating right now", "Eating"),
        True,
    ),
    (
        ("c h p Ny", "c BDQ r h p Ny"),
        True,
    ),
    (
        ("a BaabbAABbBbbaAb", "a BbbA baaaaBaAabB bbab AaAB"),
        False,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().areSentencesSimilar(*inputs)
    assert output == expected
