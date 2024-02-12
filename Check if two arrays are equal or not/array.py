#User function Template for python3

class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        
       

        count_dict1 = {}
        count_dict2 = {}
    
        for element in A:
            count_dict1[element] = count_dict1.get(element, 0) + 1
    
        for element in B:
            count_dict2[element] = count_dict2.get(element, 0) + 1
    
        return count_dict1 == count_dict2


