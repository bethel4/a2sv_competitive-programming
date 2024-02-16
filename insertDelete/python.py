import random

class RandomizedSet:

    def __init__(self):
        self.result = []

    def insert(self, val: int) -> bool:
        if val not in self.result:
            self.result.append(val)
            return True
        else:
            return False
        
      
    def remove(self, val: int) -> bool:
        if val in self.result:
            self.result.remove(val)
            return True
        else:
            return False
    


    def getRandom(self) -> int:
        return random.choice(self.result)
