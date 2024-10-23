from collections import Counter

import pytest


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)

        for i in range(len(s2)):
            if s2[i] in counter:
                counter[s2[i]] -= 1
            if i >= len(s1) and s2[i - len(s1)] in counter:
                counter[s2[i - len(s1)]] += 1

            if all(v == 0 for v in counter.values()):
                return True

        return False


tests = [
    (
        ("ab", "eidbaooo"),
        True,
    ),
    (
        ("ab", "eidboaoo"),
        False,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().checkInclusion(*inputs)
    assert output == expected
