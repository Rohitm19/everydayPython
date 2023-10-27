#vsCode

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        # Base case: If the input list contains only one element, return it as a permutation.
        if len(nums) == 1:
            return [nums[:]]  # nums[:] is a deep copy

        for i in range(len(nums)):
            n = nums.pop(i)  # Manually select an element at index 'i' to include in the permutation

            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            res.extend(perms)

            nums.insert(i, n)  # Restore the list by inserting the element back at index 'i'

        return res

# Manually input your list of integers here
nums = [1, 2, 3]

# Create an instance of the Solution class
solution = Solution()

# Call the permute method to generate permutations based on your manual input
result = solution.permute(nums)

# Print the generated permutations
print(result)
