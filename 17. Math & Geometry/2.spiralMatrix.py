#vsCode

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix:
            return res

        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1

        while left <= right and top <= bottom:
            # Traverse top row
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            # Traverse right column
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                # Traverse bottom row
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                # Traverse left column
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res

def main():
    solution = Solution()
    n = int(input("Enter the number of rows: "))
    m = int(input("Enter the number of columns: "))
    matrix = []
    print("Enter the elements of the matrix:")
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    result = solution.spiralOrder(matrix)
    print("Spiral order of the matrix:", result)

if __name__ == "__main__":
    main()
