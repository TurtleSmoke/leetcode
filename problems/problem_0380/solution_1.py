import random


class RandomizedSet:
    def __init__(self):
        self.map = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False

        self.map[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False

        idx, last = self.map[val], self.data[-1]
        self.data[idx] = last
        self.map[last] = idx
        self.data.pop()
        del self.map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)
