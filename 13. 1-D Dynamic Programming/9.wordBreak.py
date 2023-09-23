#vsCode

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]

def main():
    solution = Solution()
    s = input("Enter the string: ")
    word_dict_input = input("Enter the word dictionary (comma-separated): ")
    word_dict = word_dict_input.split(',')
    result = solution.wordBreak(s, word_dict)
    print("Can be segmented into words from the word dictionary:", result)

if __name__ == "__main__":
    main()
