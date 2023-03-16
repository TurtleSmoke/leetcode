from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def rec(s, left, right):
            if len(s) == 2 * n:
                yield s
            if left < n:
                yield from rec(s + "(", left + 1, right)
            if right < left:
                yield from rec(s + ")", left, right + 1)

        return list(rec("", 0, 0))


tests = [
    (
        (3,),
        ["((()))", "(()())", "(())()", "()(())", "()()()"],
    ),
    (
        (1,),
        ["()"],
    ),
]
