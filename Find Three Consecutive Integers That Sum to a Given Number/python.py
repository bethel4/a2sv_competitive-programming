class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        consecutive_sum = 0
        for i in range(1, num):
            consecutive_sum = i + (i + 1) + (i + 2)
            if consecutive_sum == num:
                return [i, i + 1, i + 2]
        return []
