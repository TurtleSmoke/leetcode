class Solution:
    def isValid(self, s: str) -> bool:
        brackets_pairs = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if not stack or brackets_pairs[stack.pop()] != c:
                    return False
        return not stack


tests = [
    (
        ("()",),
        True,
    ),
    (
        ("()[]{}",),
        True,
    ),
    (
        ("(]",),
        False,
    ),
    (
        ("([)]",),
        False,
    ),
]
