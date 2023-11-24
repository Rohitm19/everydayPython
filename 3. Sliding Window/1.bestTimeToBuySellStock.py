#neetCode
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res

#vsCode
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res

def main():
    num_prices = int(input("Enter the number of prices: "))
    prices = []
    for _ in range(num_prices):
        price = int(input("Enter a price: "))
        prices.append(price)

    solution = Solution()
    max_profit = solution.maxProfit(prices)
    print("Maximum profit:", max_profit)

if __name__ == "__main__":
    main()
