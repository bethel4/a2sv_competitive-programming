class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        index_mapping = {num: i for i, num in enumerate(nums)}

        for operation in operations:
            original_value, new_value = operation
            if original_value in index_mapping:
                index = index_mapping[original_value]
                nums[index] = new_value
                del index_mapping[original_value]
                index_mapping[new_value] = index

        return nums

