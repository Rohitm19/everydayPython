#vsCode
import sys

class Solution:                                       #main logic
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

def main():                                            # logic for manual input
    s = input("Enter the first string: ")
    t = input("Enter the second string: ")

    solution = Solution()
    result = solution.isAnagram(s, t)

    if result:
        print("The two strings are anagrams.")
    else:
        print("The two strings are not anagrams.")

if __name__ == "__main__":
    main()
