import pytest
from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped_nums = [int("".join(str(mapping[int(d)]) for d in str(n))) for n in nums]
        return [nums[i] for i in sorted(range(len(nums)), key=lambda x: mapped_nums[x])]


tests = [
    (
        ([8, 9, 4, 0, 2, 1, 3, 5, 7, 6], [991, 338, 38]),
        [338, 38, 991],
    ),
    (
        ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [789, 456, 123]),
        [123, 456, 789],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().sortJumbled(*inputs)
    assert output == expected
