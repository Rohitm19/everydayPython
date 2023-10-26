#vsCode

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # Manually input a choice (1 for include, 0 for not include) for nums[i]
            choice = 1  # Change to 0 or 1 as needed
            
            if choice == 1:
                subset.append(nums[i])
                dfs(i + 1)
                subset.pop()

            if choice == 0:
                dfs(i + 1)

        dfs(0)
        return res

# Manually input your list of integers here
nums = [1, 2, 3]

# Create an instance of the Solution class
solution = Solution()

# Call the subsets method to generate subsets based on your manual input
result = solution.subsets(nums)

# Print the generated subsets
print(result)