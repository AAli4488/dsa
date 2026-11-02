#2965 question of array

from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        total = n * n
        count = [0] * (total + 1)

        for row in grid:
            for x in row:
                count[x] += 1

        a = b = -1
        for num in range(1, total + 1):
            if count[num] == 2:
                a = num
            elif count[num] == 0:
                b = num

        return [a, b]
