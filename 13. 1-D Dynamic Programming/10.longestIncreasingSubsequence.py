class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)

def main():
    solution = Solution()
    nums_input = input("Enter the list of numbers (comma-separated): ")
    nums = [int(x) for x in nums_input.split(',')]
    result = solution.lengthOfLIS(nums)
    print("Length of Longest Increasing Subsequence:", result)

if __name__ == "__main__":
    main()
