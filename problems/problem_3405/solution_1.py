import pytest


class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        MAX_SIZE = 10**5
        # Put in cache fact and inv_fact, should be init once and not at each call but my parsing can't handle it =(
        fact = [0] * MAX_SIZE
        inv_fact = [0] * MAX_SIZE

        def fast_pow_mod(x, e):
            res = 1
            while e:
                if e & 1:
                    res = res * x % MOD
                x = x * x % MOD
                e >>= 1
            return res

        def comb(n, m):
            return fact[n] * inv_fact[m] % MOD * inv_fact[n - m] % MOD

        fact[0] = 1
        for i in range(1, MAX_SIZE):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact[MAX_SIZE - 1] = fast_pow_mod(fact[MAX_SIZE - 1], MOD - 2)
        for i in range(MAX_SIZE - 1, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD
        return m * comb(n - 1, k) % MOD * fast_pow_mod(m - 1, n - k - 1) % MOD


tests = [
    (
        (3, 2, 1),
        4,
    ),
    (
        (4, 2, 2),
        6,
    ),
    (
        (5, 2, 0),
        2,
    ),
    (
        (43828, 31013, 38787),
        289456936,
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize("inputs, expected", tests)
def test_validator(inputs, expected):
    output = Solution().countGoodArrays(*inputs)
    assert output == expected
