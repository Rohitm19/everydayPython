#neetCode
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return

            # All subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            # All subsets that don't include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res

#vsCode

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return

            # Include the current element
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            # Skip duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            # Exclude the current element
            backtrack(i + 1, subset)

        # Manually input your list of integers here
        nums = [1, 2, 2]

        backtrack(0, [])
        return res

# Create an instance of the Solution class
solution = Solution()

# Call the subsetsWithDup method to generate subsets based on your manual input
result = solution.subsetsWithDup(nums)

# Print the generated subsets
print(result)
