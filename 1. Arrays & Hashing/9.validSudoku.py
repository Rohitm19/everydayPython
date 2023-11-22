#neetCode
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True

#vsCode
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                cell_val = input(f"Enter the value for cell [{r}][{c}] (or '.' for empty cell): ")
                if cell_val == ".":
                    continue
                if (
                    cell_val in rows[r]
                    or cell_val in cols[c]
                    or cell_val in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(cell_val)
                rows[r].add(cell_val)
                squares[(r // 3, c // 3)].add(cell_val)

        return True

def main():
    solution = Solution()
    board = []
    print("Enter the Sudoku board:")
    for i in range(9):
        row = input().split()
        board.append(row)
    is_valid = solution.isValidSudoku(board)
    if is_valid:
        print("The Sudoku board is valid.")
    else:
        print("The Sudoku board is not valid.")

if __name__ == "__main__":
    main()
