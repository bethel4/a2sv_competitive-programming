class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_str = strs[0]

    
        prefix = ""

            
        for i in range(len(first_str)):
            if all(len(s) > i and s[i] == first_str[i] for s in strs):
                prefix += first_str[i]
            else:
                    
                break

        return prefix

   
