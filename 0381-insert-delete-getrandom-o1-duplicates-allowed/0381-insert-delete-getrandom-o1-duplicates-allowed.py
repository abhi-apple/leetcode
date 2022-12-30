import random
class RandomizedCollection:

    def __init__(self):
        self.items=[]
    def insert(self, val: int) -> bool:
        if val in self.items:
            self.items.append(val)
            return False
        self.items.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.items:
            return False
        self.items.remove(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.items)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()