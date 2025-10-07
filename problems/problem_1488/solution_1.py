import pytest
from typing import List


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        full_lakes = {}
        dry_days = []
        res = [-1] * len(rains)

        for i, lake in enumerate(rains):
            if lake == 0:
                dry_days.append(i)
            else:
                if lake in full_lakes:
                    for j in range(len(dry_days)):
                        if dry_days[j] > full_lakes[lake]:
                            res[dry_days[j]] = lake
                            dry_days.pop(j)
                            break
                    else:
                        return []
                full_lakes[lake] = i

        for day in dry_days:
            res[day] = 1

        return res


tests = [
    (
        ([1, 2, 3, 4],),
        [-1, -1, -1, -1],
    ),
    (
        ([1, 2, 0, 0, 2, 1],),
        [-1, -1, 2, 1, -1, -1],
    ),
    (
        ([1, 2, 0, 1, 2],),
        [],
    ),
    (
        ([69, 0, 0, 0, 69],),
        [-1, 69, 1, 1, -1],
    ),
    (
        ([0, 1, 1],),
        [],
    ),
    (
        ([1, 0, 2, 0, 2, 1],),
        [-1, 1, -1, 2, -1, -1],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().avoidFlood(*inputs)
    assert output == expected
