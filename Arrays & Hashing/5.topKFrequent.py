#VS Code
from typing import List
import sys
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] += 1
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        # O(n)

def main():
    nums = []
    while True:
        n = input("Enter a number: ")
        if n == "":
            break
        nums.append(int(n))

    k = int(input("Enter the number of top frequent numbers: "))

    solution = Solution()
    result = solution.topKFrequent(nums, k)

    print("The top {} frequent numbers are: {}".format(k, result))

if __name__ == "__main__":
    main()