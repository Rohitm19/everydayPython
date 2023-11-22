#neetCode
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

#VS Code
from typing import List
def containsDuplicate(nums: List[int]) -> bool:  # main logic
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

        
while True:                                                           # this part is to take input from command line
    nums_str = input("Enter a list of ints separated by commas: ")
    nums = list(map(int, nums_str.split(",")))
    if nums and nums != []:
        break

print(containsDuplicate(nums))

