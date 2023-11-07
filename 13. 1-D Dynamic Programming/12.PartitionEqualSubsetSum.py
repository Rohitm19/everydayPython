#vsCode

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return False

# Manual Input
nums = [1, 5, 11, 5]  # Replace this with your input

# Create an instance of the Solution class
solution = Solution()

# Call the canPartition method with your input
result = solution.canPartition(nums)

# Print the result
if result:
    print("The input list can be partitioned into two subsets with equal sums.")
else:
    print("The input list cannot be partitioned into two subsets with equal sums.")
