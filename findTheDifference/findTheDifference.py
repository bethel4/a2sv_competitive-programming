class Solution:
      def findTheDifference(self,s: str, t: str) -> str:
            char_count = {}

        # Count occurrences in string s
            for char in s:
                char_count[char] = char_count.get(char, 0) + 1

            # Subtract occurrences in string t
            for char in t:
                if char_count.get(char, 0) == 0:
                    # If the character is not found in char_count or the count is 0, it's the added letter
                    return char
                char_count[char] -= 1

            # The loop should have already returned if there was an added letter, but this is just to handle edge cases
            for char, count in char_count.items():
                if count > 0:
                    return char

