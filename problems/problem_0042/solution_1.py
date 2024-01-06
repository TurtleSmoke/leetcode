import pytest
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0

        res = 0
        max_left, max_right, left, right = height[0], height[-1], 1, len(height) - 2
        while left <= right:
            if max_left < max_right:
                if height[left] > max_left:
                    max_left = height[left]
                else:
                    res += max_left - height[left]
                left += 1
            else:
                if height[right] > max_right:
                    max_right = height[right]
                else:
                    res += max_right - height[right]
                right -= 1

        return res


tests = [
    (
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],),
        6,
    ),
    (
        ([4, 2, 0, 3, 2, 5],),
        9,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().trap(*inputs)
    assert output == expected
