#vsCode

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}  # key=(i, buying) val=max_profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]

        return dfs(0, True)

# Manual Input
prices = [7, 1, 5, 3, 6, 4]  # Replace this with your input

# Create an instance of the Solution class
solution = Solution()

# Call the maxProfit method with your input
result = solution.maxProfit(prices)

# Print the result
print("The maximum profit is:", result)
