#neetCode
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]

        # O(n * m) O(n)

#vsCode

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]

# Accept manual input for m and n
m = int(input("Enter the number of rows (m): "))
n = int(input("Enter the number of columns (n): "))

# Create an instance of the Solution class
solution = Solution()

# Calculate the unique paths
result = solution.uniquePaths(m, n)

# Display the result
print("Unique paths:", result)
