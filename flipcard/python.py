from typing import List

class Solution:
    def good(self, value, fronts, backs):
        for i in range(len(fronts)):
            if fronts[i] == backs[i] == value:
                return False
            if backs[i] == value:
                continue
            if fronts[i] == value:
                backs[i], fronts[i] = fronts[i], backs[i]
        return True

    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        for value in range(1, 2001):
            if(value in fronts+backs)and self.good(value, fronts, backs):
                return value
        return 0
