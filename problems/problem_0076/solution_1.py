from collections import Counter
import pytest


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sub_windows = []
        for window_size in range(len(t), len(s) + 1):
            for i in range(len(s) - window_size + 1):
                sub_windows.append(s[i : i + window_size])
        res = ""
        t = Counter(t)
        for c in sub_windows:
            if t & Counter(c) == t and (res == "" or len(c) < len(res)):
                res = c
        return res


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
