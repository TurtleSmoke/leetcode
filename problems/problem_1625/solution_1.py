import pytest
from collections import deque


class Solution:
    def add(self, s: str, a: int) -> str:
        return "".join(str((int(c) + a) % 10) if i % 2 == 1 else c for i, c in enumerate(s))

    def rotate(self, s: str, b: int) -> str:
        b = b % len(s)
        return s[-b:] + s[:-b]

    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        queue = deque([s])
        visited = set()
        res = s
        while queue:
            current = queue.popleft()
            if current in visited:
                continue
            visited.add(current)
            if current < res:
                res = current

            for _ in range(a):
                queue.append(self.add(current, a))
            for _ in range(b):
                queue.append(self.rotate(current, b))

        return res


tests = [
    (
        ("5525", 9, 2),
        "2050",
    ),
    (
        ("74", 5, 1),
        "24",
    ),
    (
        ("0011", 4, 2),
        "0011",
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().findLexSmallestString(*inputs)
    assert output == expected
