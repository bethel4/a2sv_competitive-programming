class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max =0
        count=0
        for i in nums:
            if i ==1:
               count+=1
               if max<count:
                max=count
            if i==0:
                count=0
            
        return max
