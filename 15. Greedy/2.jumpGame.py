#vsCode

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0

def main():
    solution = Solution()
    nums = list(map(int, input("Enter the list of numbers, separated by spaces: ").split()))
    result = solution.canJump(nums)
    print("Can jump to the last index:", result)

if __name__ == "__main__":
    main()
