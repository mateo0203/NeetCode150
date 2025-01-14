import random

class RandomizedSet:
    def __init__(self):
        self.randomSet = {}
        self.randomList = []

    def insert(self, val: int) -> bool:
        if val in self.randomSet:
            return False
        else:
            self.randomList.append(val)
            self.randomSet[val] = len(self.randomList) - 1
            return True

    def remove(self, val: int) -> bool:
        if val in self.randomSet:
            idx = self.randomSet[val]
            self.randomList[idx] = self.randomList[-1]
            self.randomSet[self.randomList[idx]] = idx
            self.randomList.pop()
            del self.randomSet[val]
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        if len(self.randomSet) == 0:
            return None
        num = random.randint(0, len(self.randomList)-1)
        return self.randomList[num]