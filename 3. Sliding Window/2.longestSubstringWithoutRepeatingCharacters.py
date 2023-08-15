#vsCode

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

def main():
    input_string = input("Enter a string: ")
    solution = Solution()
    longest_length = solution.lengthOfLongestSubstring(input_string)
    print("Length of longest substring without repeating characters:", longest_length)

if __name__ == "__main__":
    main()
