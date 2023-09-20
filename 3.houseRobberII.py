#vsCode

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        rob1, rob2 = 0, 0

        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2

def main():
    solution = Solution()
    nums = [int(x) for x in input("Enter a list of integers for nums, separated by spaces: ").split()]
    result = solution.rob(nums)
    print("Maximum amount that can be robbed:", result)

if __name__ == "__main__":
    main()
