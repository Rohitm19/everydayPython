#vsCode

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Manual Input for testing
        nums_input = list(map(int, input("Enter space-separated numbers: ").split()))

        res = 0
        for n in nums_input:
            res = n ^ res
        return res

# Example Usage
solution = Solution()
result = solution.singleNumber([])
print(f"Single Number: {result}")
