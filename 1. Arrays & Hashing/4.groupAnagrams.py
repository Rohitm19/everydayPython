#neetCode
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()

#VS Code
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()

def main():
    strs = []
    while True:
        s = input("Enter a string: ")
        if s == "":
            break
        strs.append(s)

    solution = Solution()
    result = solution.groupAnagrams(strs)

    for group in result:
        print(group)

if __name__ == "__main__":
    main()
