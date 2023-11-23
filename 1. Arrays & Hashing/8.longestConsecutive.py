#neetCode

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest


#vsCode
import sys
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

def main():
    nums = []
    while True:
        n = input("Enter a number: ")
        if n == "":
            break
        nums.append(int(n))

    solution = Solution()
    result = solution.longestConsecutive(nums)

    print("The longest consecutive sequence is of length: {}".format(result))

if __name__ == "__main__":
    main()
