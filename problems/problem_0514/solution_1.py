from collections import defaultdict

import pytest


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        pos = defaultdict(list)
        for i, c in enumerate(ring):
            pos[c].append(i)

        state = {0: 0}
        for c in key:
            next_state = {}
            for j in pos[c]:
                next_state[j] = float("inf")
                for i in state:
                    next_state[j] = min(next_state[j], min(abs(i - j), len(ring) - abs(i - j)) + state[i])
            state = next_state
        return min(state.values()) + len(key)


tests = [
    (
        ("godding", "gd"),
        4,
    ),
    (
        ("godding", "godding"),
        13,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().findRotateSteps(*inputs)
    assert output == expected
