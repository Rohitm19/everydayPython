#neetCode
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i


#vsCode
from typing import List
class Solution:
    def twoSum(self, nums, target):             # for class self should be mentioned
        prevMap = {}  # val -> index             # creating hasmap using empty dictionary

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

def main():
    nums = []
    target = int(input("Enter the target value: "))
    nums = input("Enter a list of ints separated by commas: ")
    nums = list(map(int, nums.split(",")))
    print(nums)
    print(target)
    result = Solution().twoSum(nums, target)
    print(f"The indices of the two numbers that add up to {target} are: {result}")

if __name__ == "__main__":
    main()
