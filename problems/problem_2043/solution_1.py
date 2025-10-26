import pytest
from typing import List


class Bank:
    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if (
            0 < account1 < len(self.balance) + 1
            and 0 < account2 < len(self.balance) + 1
            and self.balance[account1 - 1] >= money
        ):
            self.balance[account1 - 1] -= money
            self.balance[account2 - 1] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if 0 < account < len(self.balance) + 1:
            self.balance[account - 1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if 0 < account < len(self.balance) + 1 and self.balance[account - 1] >= money:
            self.balance[account - 1] -= money
            return True
        return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)return False


tests = [
    (
        (
            ["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"],
            [[[10, 100, 20, 50, 30]], [3, 10], [5, 1, 20], [5, 20], [3, 4, 15], [10, 50]],
        ),
        [None, True, True, True, False, False],
    ),
]


@pytest.mark.timeout(2)
@pytest.mark.parametrize(
    "inputs, expected",
    tests,
)
def test_validator(inputs, expected):
    bank = None
    res = []
    for i, command in enumerate(inputs[0]):
        if command == "Bank":
            bank = Bank(*inputs[1][i])
            res.append(None)
        elif command == "withdraw":
            res.append(bank.withdraw(*inputs[1][i]))
        elif command == "transfer":
            res.append(bank.transfer(*inputs[1][i]))
        elif command == "deposit":
            res.append(bank.deposit(*inputs[1][i]))

    assert res == expected
