#vsCode

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1

# Manual input of nums and target
nums_input = input("Enter the numbers in the list separated by spaces: ")
nums = [int(num) for num in nums_input.split()]
target = int(input("Enter the target value: "))

# Perform binary search
solution = Solution()
result = solution.search(nums, target)
print("Index of the target in the list:", result)
