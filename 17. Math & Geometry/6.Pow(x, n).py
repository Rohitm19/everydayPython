#vsCode

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1

            res = helper(x * x, n // 2)
            return x * res if n % 2 else res

        # Manual Input
        base = float(input("Enter the base (x): "))
        exponent = int(input("Enter the exponent (n): "))

        result = self.myPow(base, exponent)
        print("Result:", result)

# Create an instance of the Solution class
solution = Solution()

# Use the myPow method with manual input
solution.myPow(x, n)
