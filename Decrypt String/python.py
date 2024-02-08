class Solution:
    def freqAlphabets(self, s: str) -> str:
        result=[]
        i=0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
              
                num = int(s[i:i + 2])
                result.append(chr(ord('a') + num - 1))
                i += 3
            else:
               
                num = int(s[i])
                result.append(chr(ord('a') + num - 1))
                i += 1

        return ''.join(result)

