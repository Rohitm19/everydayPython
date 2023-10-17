#vsCode

from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res

# Manual input of the piles and h
piles = [int(x) for x in input("Enter the piles (separated by spaces): ").split()]
h = int(input("Enter the number of hours available: "))

# Calculate the minimum eating speed
solution = Solution()
min_speed = solution.minEatingSpeed(piles, h)
print("Minimum eating speed:", min_speed)
