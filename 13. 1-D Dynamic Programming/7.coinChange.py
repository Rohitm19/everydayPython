#vsCode

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1

def main():
    solution = Solution()
    coins_input = input("Enter the coin denominations (comma-separated): ")
    coins = [int(coin) for coin in coins_input.split(',')]
    amount = int(input("Enter the amount: "))
    result = solution.coinChange(coins, amount)
    print("Minimum number of coins needed:", result)

if __name__ == "__main__":
    main()
