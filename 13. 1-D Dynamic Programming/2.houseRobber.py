#neetCode
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

#vsCode

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

def main():
    solution = Solution()
    nums = [int(x) for x in input("Enter a list of integers for nums, separated by spaces: ").split()]
    result = solution.rob(nums)
    print("Maximum amount that can be robbed:", result)

if __name__ == "__main__":
    main()
