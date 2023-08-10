#VS Code
from typing import List
import sys

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

def main():
    nums = []
    while True:
        n = input("Enter a number: ")
        if n == "":
            break
        nums.append(int(n))

    solution = Solution()
    result = solution.productExceptSelf(nums)

    print("The product of all numbers except self for each element is: {}".format(result))

if __name__ == "__main__":
    main()
