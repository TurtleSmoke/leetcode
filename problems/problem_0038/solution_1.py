import pytest


class Solution:
    def countAndSay(self, n: int) -> str:
        def say(s):
            if len(s) == 1:
                return "1" + s
            else:
                count = 1
                result = ""
                for i in range(1, len(s)):
                    if s[i] == s[i - 1]:
                        count += 1
                    else:
                        result += str(count) + s[i - 1]
                        count = 1
                result += str(count) + s[-1]
                return result

        result = "1"
        for _ in range(1, n):
            result = say(result)
        return result


tests = [
    (
        (1,),
        "1",
    ),
    (
        (4,),
        "1211",
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().countAndSay(*inputs)
    assert output == expected
