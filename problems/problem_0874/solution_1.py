from typing import List

import pytest


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = set((x + y * 1j for x, y in obstacles))
        res = 0
        pos = 0
        direction = 1j
        for cmd in commands:
            if cmd == -1:
                direction *= -1j
            elif cmd == -2:
                direction *= 1j
            else:
                for _ in range(cmd):
                    if pos + direction in obstacles:
                        break
                    pos += direction
                res = max(res, int(pos.real) ** 2 + int(pos.imag) ** 2)

        return res


tests = [
    (
        ([4, -1, 3], []),
        25,
    ),
    (
        ([4, -1, 4, -2, 4], [[2, 4]]),
        65,
    ),
    (
        ([6, -1, -1, 6], []),
        36,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().robotSim(*inputs)
    assert output == expected
