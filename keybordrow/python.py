class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm"),
        ]
        result = []
        for word in words:
            word_set=set(word.lower())
            if any(word_set.issubset(row) for row in rows):
                result.append(word)
          
        return result
