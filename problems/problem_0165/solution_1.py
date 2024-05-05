import pytest


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(x) for x in version1.split(".")]
        v2 = [int(x) for x in version2.split(".")]

        v1 += [0] * (len(v2) - len(v1))
        v2 += [0] * (len(v1) - len(v2))

        return (v1 > v2) - (v1 < v2)


tests = [
    (
        ("1.01", "1.001"),
        0,
    ),
    (
        ("1.0", "1.0.0"),
        0,
    ),
    (
        ("0.1", "1.1"),
        -1,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().compareVersion(*inputs)
    assert output == expected
