class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
       
        common = set(list1) & set(list2)
        least_sum = float('inf')
        result = []

        for c in common:
            if c in list1 and c in list2:
              sum_of_indices = list1.index(c) + list2.index(c)

              if sum_of_indices < least_sum:
                 least_sum = sum_of_indices
                 result = [c]
              elif sum_of_indices == least_sum:
                    result.append(c)

        return result

        
