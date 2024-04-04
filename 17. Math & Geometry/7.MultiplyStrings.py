#neetCode
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"

        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                res[i1 + i2] += digit
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] = res[i1 + i2] % 10

        res, beg = res[::-1], 0
        while beg < len(res) and res[beg] == 0:
            beg += 1
        res = map(str, res[beg:])
        return "".join(res)

#vsCode

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Check if any of the numbers is 0
        if "0" in [num1, num2]:
            return "0"

        # Reverse the input numbers for easier computation
        num1, num2 = num1[::-1], num2[::-1]

        # Initialize an array to store the result
        res = [0] * (len(num1) + len(num2))

        # Perform multiplication
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                res[i1 + i2] += digit
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] = res[i1 + i2] % 10

        # Reverse the result and remove leading zeros
        res, beg = res[::-1], 0
        while beg < len(res) and res[beg] == 0:
            beg += 1
        res = map(str, res[beg:])

        # Join the result and return as a string
        return "".join(res)

# Manual Input
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Create an instance of the Solution class
solution = Solution()

# Use the multiply method with manual input
result = solution.multiply(num1, num2)
print("Result:", result)
