class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        res = ""
        width = 2 * (numRows - 1)
        for i in range(numRows):
            for j in range(i, len(s), width):
                res += s[j]
                if i != 0 and i != numRows - 1 and j + width - 2 * i < len(s):
                    res += s[j + width - 2 * i]
        return res


tests = [
    (
        ("PAYPALISHIRING", 3),
        "PAHNAPLSIIGYIR",
    ),
    (
        ("PAYPALISHIRING", 4),
        "PINALSIGYAHRPI",
    ),
    (
        ("A", 1),
        "A",
    ),
    (
        ("ABCD", 3),
        "ABDC",
    ),
]
