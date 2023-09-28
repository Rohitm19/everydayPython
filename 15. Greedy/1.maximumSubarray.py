#vsCode

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]

        total = 0
        for n in nums:
            total += n
            res = max(res, total)
            if total < 0:
                total = 0
        return res

def main():
    solution = Solution()
    nums = list(map(int, input("Enter the list of numbers, separated by spaces: ").split()))
    result = solution.maxSubArray(nums)
    print("Maximum Subarray Sum:", result)

if __name__ == "__main__":
    main()
