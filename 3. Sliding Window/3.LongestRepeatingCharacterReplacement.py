#vsCode

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

        return (r - l + 1)

def main():
    input_string = input("Enter a string: ")
    k = int(input("Enter the value of k: "))
    solution = Solution()
    result = solution.characterReplacement(input_string, k)
    print("Length of longest substring after character replacement:", result)

if __name__ == "__main__":
    main()
