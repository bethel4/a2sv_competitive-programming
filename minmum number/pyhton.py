from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = []

        for i in range(len(boxes)):
            count = 0  # Reset count for each iteration of the outer loop
            for j in range(len(boxes)):
                if i == j:
                    continue

                if j >= 0 and j < len(boxes) and boxes[j] == '1':
                    count += abs(i - j)

            result.append(count)

        return result
