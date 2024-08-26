import pytest
from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(int(detail[11:13]) > 60 for detail in details)


tests = [
    (
        (["7868190130M7522", "5303914400F9211", "9273338290F4010"],),
        2,
    ),
    (
        (["1313579440F2036", "2921522980M5644"],),
        0,
    ),
    (
        (["1313579440F6036", "2921522980M6144"],),
        1,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().countSeniors(*inputs)
    assert output == expected
