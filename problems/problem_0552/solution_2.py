import pytest


class Solution:
    def checkRecord(self, n):
        if n == 1:
            return 3
        if n == 0:
            return 0
        nums = [1, 1, 2]
        i = 2
        while i < n:
            nums.append((nums[i] + nums[i - 1] + nums[i - 2]) % 1000000007)
            i += 1
        result = (nums[n] + nums[n - 1] + nums[n - 2]) % 1000000007
        for i in range(n):
            result += nums[i + 1] * nums[n - i] % 1000000007
            result %= 1000000007
        return result


tests = [
    ((0,), 0),
    (
        (1,),
        3,
    ),
    (
        (2,),
        8,
    ),
    (
        (3,),
        19,
    ),
    (
        (4,),
        43,
    ),
    (
        (5,),
        94,
    ),
    (
        (10101,),
        183236316,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().checkRecord(*inputs)
    assert output == expected
