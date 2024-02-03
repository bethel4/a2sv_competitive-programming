class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        my_list = []
        n= min(len(word1),len(word2))

        for i in range(n):
            my_list.append(word1[i])
            my_list.append(word2[i])
        my_list.extend(word2[n:])
        my_list.extend(word1[n:])
        return ''.join(my_list)
