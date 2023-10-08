#vsCode

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

def main():
    solution = Solution()
    nums_str = input("Enter the list of numbers separated by commas: ")
    nums = [int(num) for num in nums_str.split(",")]
    result = solution.missingNumber(nums)
    print("Missing number is:", result)

if __name__ == "__main__":
    main()
