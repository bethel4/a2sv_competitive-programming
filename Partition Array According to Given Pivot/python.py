class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        result = [n for n in nums if n < pivot]
        result.extend([pivot] * nums.count(pivot))
        result.extend([n for n in nums if n > pivot])
        return result
