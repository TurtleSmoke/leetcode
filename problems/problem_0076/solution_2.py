from collections import Counter

import pytest


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start, min_start, min_end = 0, 0, len(s) + 1
        count, delta = Counter(t), len(t)

        for end, c in enumerate(s, 1):
            delta -= count[c] > 0
            count[c] -= 1

            if delta == 0:
                while start < end and count[s[start]] < 0:
                    count[s[start]] += 1
                    start += 1
                if end - start < min_end - min_start:
                    min_start, min_end = start, end

        return "" if min_end == len(s) + 1 else s[min_start:min_end]


tests = [
    (
        ("ADOBECODEBANC", "ABC"),
        "BANC",
    ),
    (
        ("a", "a"),
        "a",
    ),
    (
        ("a", "aa"),
        "",
    ),
    (
        (
            "zfvdiuibotzsqrpgfnbfwudczyruzvuyaselommcfmuxdmgkzhpydsafttzsowrrovccjqhpcdohpurpeiphdrmwkooykfracvemmldqpragmtxqcmxfdmbnapomxfmzdqlpeofvghbubzkdnjirxlgxaujzcxzfqmuudbrllsfmtrpjczaakgzmdlofinkybgugjlrugygzrxiuwkwitvxwilbranrbvmigzbbfcjhthrpfclqxjntrawkajcdgqlmpppxrzemivcpzpfwauruuneuyiyeylrqagnthrgpokhozmmaheudryysjywhjpzmymhhfnxwxemzsyzbcvfwvfoedmoocnccckjjzifzoryhqxkuurspwgubtkqxxuzbeilersdhkdoccbywsrlpxhssriprdqujzhnsaszmvqoxrotjfhafqtxkdpbifvsgfhafccr",
            "xshxlvswdb",
        ),
        "bywsrlpxhssriprdqujzhnsaszmvqox",
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().minWindow(*inputs)
    assert output == expected
