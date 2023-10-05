#vsCode

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # O(1)
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        # Determine which rows/cols need to be zero
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        # Set zeros based on flags
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0

def main():
    solution = Solution()
    n = int(input("Enter the number of rows: "))
    m = int(input("Enter the number of columns: "))
    matrix = []
    print("Enter the elements of the matrix:")
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    print("Original Matrix:")
    for row in matrix:
        print(row)

    solution.setZeroes(matrix)

    print("\nMatrix after setting zeroes:")
    for row in matrix:
        print(row)

if __name__ == "__main__":
    main()
