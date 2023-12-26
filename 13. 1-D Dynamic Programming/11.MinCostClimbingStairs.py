#neetCode
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])

#vsCode
from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])

# Manual Input
cost = [10, 15, 20]

# Create an instance of the Solution class
solution = Solution()

# Call the minCostClimbingStairs method with your input
min_cost = solution.minCostClimbingStairs(cost)

# Print the result
print("Minimum Cost:", min_cost)
