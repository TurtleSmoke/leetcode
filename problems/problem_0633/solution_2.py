import numpy as np
import pytest


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        A = np.array([[1, -2, 2], [2, -1, 2], [2, -2, 3]])
        B = np.array([[1, 2, 2], [2, 1, 2], [2, 2, 3]])
        C = np.array([[-1, 2, 2], [-2, 1, 2], [-2, 2, 3]])

        def compute_all_pythagorean_triples(abc):
            if abc[-1] == c:
                return True
            if abc[-1] > c:
                return False
            return (
                compute_all_pythagorean_triples(A @ abc)
                or compute_all_pythagorean_triples(B @ abc)
                or compute_all_pythagorean_triples(C @ abc)
            )

        return compute_all_pythagorean_triples([3, 4, 5])


tests = [
    (
        (5,),
        True,
    ),
    (
        (3,),
        False,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    output = Solution().judgeSquareSum(*inputs)
    assert output == expected
