#vsCode

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                # save the topleft
                topLeft = matrix[top][l + i]

                # move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move top left into top right
                matrix[top + i][r] = topLeft
            r -= 1
            l += 1

def main():
    solution = Solution()
    n = int(input("Enter the dimension of the matrix: "))
    matrix = []
    print("Enter the elements of the matrix:")
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    solution.rotate(matrix)
    print("Matrix after rotation:")
    for row in matrix:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()
