class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        my_list = []
        for i in  range(0,n):
            my_list.append(nums[i])
            my_list.append(nums[i+n])
        return my_list
